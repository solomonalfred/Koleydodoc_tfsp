from agreement_state import AgreementState

class JSONPostprocessor:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_

    def process(self):
        json = []
        source = self.agree.agreement_.text
        tagged = self.agree.agreement_.agreement_marked
        for parag in range(len(source)):
            paragraph = []
            for sent in range(len(source[parag])):
                sentence = source[parag][sent]
                if tagged[parag][sent]:
                    paragraph.append(sentence)
            json.append(paragraph)
        self.agree.change_agreement_state(json)
        return self.agree