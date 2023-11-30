from core.preprocessor_manager import PreprocessorManager
from agreement import Agreement
from agreement_state import AgreementState

class Core:

    def __init__(self):
        self.source = AgreementState(Agreement())

    def process(self, data: 'Agreement'):
        self.source.change_data(data)
        return PreprocessorManager(self.source).process()


