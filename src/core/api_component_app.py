import os
from urllib.parse import urlencode
from uvicorn import Config, Server
import asyncio
import uuid
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import JSONResponse, FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from api_component_prepare_data import *
from api_component_api_constants import *

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def start_menu(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/file", response_class=FileResponse)
async def download_file(filename: str):
    file_path = os.path.join("../../files", filename)
    return FileResponse(file_path, filename=filename)

@app.get("/context", response_class=HTMLResponse)
async def context_find(request: Request):
    return templates.TemplateResponse("context.html", {"request": request})

@app.get("/risk", response_class=HTMLResponse)
async def context_find(request: Request):
    return templates.TemplateResponse("risk.html", {"request": request})

@app.post("/context/color", response_class=HTMLResponse)
async def context_find(
        request: Request,
        input_type: str = Form(...),
        input_text_data: str = Form(None),
        input_file_data: UploadFile = File(None),
        context: str = Form(None),
        output_type: str = Form(...)
):
    data = process_context(input_type, input_text_data, input_file_data, context, output_type)
    if data.agreement_.agreement_error != ERROR.OK:
        result = {
            "request": request,
            "msg": MSG_ERROR[data.agreement_.agreement_error]
        }
        return templates.TemplateResponse("error.html", result)
    if output_type == "json/simple":
        marked = marked_text(data.agreement_.text, data.agreement_.agreement_marked)
        result = {
            "request": request,
            "sentences": marked
        }
        return templates.TemplateResponse("text_response.html", result)
    elif output_type == "json/tagged":
        marked = tagged_sentences(data.agreement_.text, data.agreement_.agreement_marked)
        result = {
            "request": request,
            "sentences": marked
        }
        return templates.TemplateResponse("tagged_text_response.html", result)
    elif output_type == "file/docx":
        result = {
            "request": request,
            "url": f"/file?{urlencode({'filename': Path(data.agreement_.text.name).name})}"
        }
        return templates.TemplateResponse("file_response.html", result)
    else:
        return templates.TemplateResponse("error.html", {"request": request})


@app.post("/risk/color", response_class=HTMLResponse)
async def risk_find(
        request: Request,
        lang_type: str = Form(...),
        input_type: str = Form(...),
        input_text_data: str = Form(None),
        input_file_data: UploadFile = File(None),
        output_type: str = Form(...)
):
    data = process_risk(lang_type, input_type, input_text_data, input_file_data, output_type)
    if data.agreement_.agreement_error != ERROR.OK:
        result = {
            "request": request,
            "msg": MSG_ERROR[data.agreement_.agreement_error]
        }
        return templates.TemplateResponse("error.html", result)
    if output_type == "json/simple":
        marked = marked_text(data.agreement_.text, data.agreement_.agreement_marked)
        result = {
            "request": request,
            "sentences": marked
        }
        return templates.TemplateResponse("text_response.html", result)
    elif output_type == "json/tagged":
        marked = tagged_sentences(data.agreement_.text, data.agreement_.agreement_marked)
        result = {
            "request": request,
            "sentences": marked
        }
        return templates.TemplateResponse("tagged_text_response.html", result)
    elif output_type == "file/docx":
        result = {
            "request": request,
            "url": f"/file?{urlencode({'filename': Path(data.agreement_.text).name})}"
        }
        return templates.TemplateResponse("file_response.html", result)
    else:
        return templates.TemplateResponse("error.html", {"request": request})


if __name__ == "__main__":
    config = Config(
        app=app,
        host="0.0.0.0",
        port=8000
    )
    server = Server(config)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(server.serve())