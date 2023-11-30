from agreement_state import AgreementState
from docx import Document
from nltk.tokenize import sent_tokenize
import shutil
import os
from utility import generate_file_name
from error_wrong_format import WrongFormat
from constants.error_state import ErrorAgreement
from core.processor_manager import ProcesorManager


class DocxPreprocessor:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_

    def process(self):
        data_ = self.agree.agreement_.text
        filename = generate_file_name() + '_' + data_.filename
        with open(f'{filename}', "wb") as buffer:
            shutil.copyfileobj(data_.file, buffer)
        try:
            input_document = Document(f'{filename}')
            text = []
            for paragraph in input_document.paragraphs:
                sentences = sent_tokenize(paragraph.text)
                text.append(sentences)
            os.remove(filename)
            self.agree.change_agreement_state(text)
            return ProcesorManager(self.agree).process()
        except Exception as e:
            print(e)
            self.agree.agreement_.agreement_error = ErrorAgreement.error_wrong_format
            return WrongFormat(self.agree).process()

