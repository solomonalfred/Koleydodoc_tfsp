from agreement_state import AgreementState
from risk_ai_processor import RiskProcessor
from context_based_processor import ContextBasedProcessor

class ProcesorManager:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_

    def process(self):
        if self.agree.agreement_.agreenent_context:
            return ContextBasedProcessor(self.agree).process()
        else:
            return RiskProcessor(self.agree).process()
