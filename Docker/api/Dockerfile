FROM python:3.8-slim

WORKDIR /

COPY ./requirements.txt ./req.txt

RUN pip3 install fastapi uvicorn python-multipart Jinja2 requests numpy tqdm python-docx spacy redis sentence-transformers \
    && pip3 install torch==2.1.1+cpu -f https://download.pytorch.org/whl/torch_stable.html


RUN python3 -m spacy download ru_core_news_lg
RUN python3 -m spacy download en_core_web_lg
RUN python3 -m nltk.downloader punkt

COPY . .

ENV PYTHONPATH "/"

WORKDIR core

CMD ["python3", "api_component_app.py"]
