from agreement_state import AgreementState
from abc import ABC, abstractmethod

class StepState(ABC):

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_

    @abstractmethod
    def process(self, word=""):
        pass

