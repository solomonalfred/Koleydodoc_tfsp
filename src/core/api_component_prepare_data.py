from api_component_api_constants import Tags, APIInputDataTypes, APILanguage, ERROR, APIOutputDataTypes
from core.core_object import Core
from core.agreement import Agreement
from constants.language import Language
from constants.input_data_types import InputDataTypes
from constants.output_data_types import OutputDataTypes
from fastapi import Form, UploadFile, File


def tagged_sentences(sent, tag):
    result = list()
    for sentence in range(len(sent)):
        for i in range(len(sent[sentence])):
            if tag[sentence][i] == Tags.NEUTRAL:
                tag_ = "N"
            else:
                tag_ = "W"
            data = {
                "tag": tag_,
                "sentence": sent[sentence][i]
            }
            result.append(data)
    return result

def marked_text(sent, tag):
    result = list()
    for sentence in sent:
        for i in sentence:
            result.append(i)
    return result

def process_context(
        input_type: str,
        input_text_data: str,
        input_file_data: UploadFile = File(None),
        context: str = Form(None),
        output_type: str = Form(...)
):
    data = Agreement()
    if input_type == APIInputDataTypes.TEXT_TEXT:
        data.agreement_input_type = InputDataTypes.TEXT
        data.text = input_text_data
    elif input_type == APIInputDataTypes.FILE_DOCX:
        data.agreement_input_type = InputDataTypes.DOCX
        data.text = input_file_data
    else:
        data.agreement_error = ERROR.BAD_INPUT
    data.agreenent_context = True
    data.agreenent_context_text = context
    if output_type == APIOutputDataTypes.FILE_DOCX:
        data.agreement_output_type = OutputDataTypes.DOCX
    elif output_type == APIOutputDataTypes.JSON_SIMPLE:
        data.agreement_output_type = OutputDataTypes.JSON
    elif output_type == APIOutputDataTypes.JSON_TAGGED:
        data.agreement_output_type = OutputDataTypes.TAGGED_JSON
    else:
        data.agreement_error = ERROR.BAD_INPUT
    data.agreenent_language = Language.RUS
    result = Core().process(data)
    return result

def process_risk(
        lang_type: str,
        input_type: str,
        input_text_data: str,
        input_file_data: UploadFile = File(None),
        output_type: str = Form(...)
):
    data = Agreement()
    if lang_type == APILanguage.RUS:
        data.agreenent_language = Language.RUS
    elif lang_type == APILanguage.ENG:
        data.agreenent_language = Language.ENG
    else:
        data.agreement_error = ERROR.BAD_INPUT

    if input_type == APIInputDataTypes.TEXT_TEXT:
        data.agreement_input_type = InputDataTypes.TEXT
        data.text = input_text_data
    elif input_type == APIInputDataTypes.FILE_DOCX:
        data.agreement_input_type = InputDataTypes.DOCX
        data.text = input_file_data
    else:
        data.agreement_error = ERROR.BAD_INPUT

    data.agreenent_context = False

    if output_type == APIOutputDataTypes.FILE_DOCX:
        data.agreement_output_type = OutputDataTypes.DOCX
    elif output_type == APIOutputDataTypes.JSON_SIMPLE:
        data.agreement_output_type = OutputDataTypes.JSON
    elif output_type == APIOutputDataTypes.JSON_TAGGED:
        data.agreement_output_type = OutputDataTypes.TAGGED_JSON
    else:
        data.agreement_error = ERROR.BAD_INPUT

    data.agreenent_language = Language.RUS
    result = Core().process(data)
    return result
