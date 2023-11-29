from agreement_state import AgreementState

class TaggedJSONPostprocessor:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_

    def process(self):
        return self.agree