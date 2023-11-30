from agreement_state import AgreementState
from src.core.postprocessor_manager import PostprocessorManager

class WrongFormat:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_

    def process(self, word=""):
        return PostprocessorManager(self.agree).process()