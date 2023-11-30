from agreement_state import AgreementState
from risk_ai_model import RiskAIModel
from error_model import BrokenModel
from src.core.postprocessor_manager import PostprocessorManager


class RiskProcessor:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_
        self.__ai_model = RiskAIModel(self.agree)
        self.broken_model = False
        if self.__ai_model.show_model_state():
            self.broken_model = True

    def process(self):
        if self.broken_model:
            return BrokenModel(self.agree).process()
        else:
            text = []
            for paragraph in self.agree.agreement_.text:
                paragraph_tag = []
                for sentence in paragraph:
                    label = self.__ai_model.process(sentence)
                    paragraph_tag.append(label)
                text.append(paragraph_tag)
            self.agree.agreement_.agreement_marked = text
            return PostprocessorManager(self.agree).process()
