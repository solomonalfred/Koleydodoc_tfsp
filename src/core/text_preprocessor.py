from agreement_state import AgreementState
from nltk.tokenize import sent_tokenize
from src.core.processor_manager import ProcesorManager

class TextPreprocessor:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_

    def process(self):
        data_ = self.agree.agreement_.text
        while data_.find('\n\n') != -1:
            data_.replace('\n\n', '\n')
        data_ = data_.split('\n')
        text = []
        for paragraph in data_:
            sentences = sent_tokenize(paragraph)
            text.append(sentences)
        self.agree.change_agreement_state(text)
        return ProcesorManager(self.agree).process()

