from agreement import Agreement

class AgreementState:

    def __init__(self, agree: 'Agreement' = Agreement()):
        self.agreement_ = agree

    def change_agreement_state(self, source):
        tmp = Agreement()
        tmp.text = source
        tmp.initial_text = self.agreement_.initial_text
        tmp.agreenent_language = self.agreement_.agreenent_language
        tmp.agreement_input_type = self.agreement_.agreement_input_type
        tmp.agreement_output_type = self.agreement_.agreement_output_type
        tmp.agreenent_context = self.agreement_.agreenent_context
        tmp.agreenent_context_text = self.agreement_.agreenent_context_text
        tmp.agreement_error = self.agreement_.agreement_error
        tmp.agreement_marked = self.agreement_.agreement_marked
        self.agreement_ = tmp

    def change_data(self, data: 'Agreement'):
        self.agreement_ = data
        self.agreement_.initial_text = data.text
