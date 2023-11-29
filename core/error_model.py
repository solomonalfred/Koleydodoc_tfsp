from agreement_state import AgreementState
from core.postprocessor_manager import PostprocessorManager

class BrokenModel:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_

    def process(self, word=""):
        return PostprocessorManager(self.agree).process()