from src.constants.language import Language
from src.constants.input_data_types import InputDataTypes
from src.constants.output_data_types import OutputDataTypes
from agreement_state import AgreementState
from docx_preprocessor import DocxPreprocessor
from text_preprocessor import TextPreprocessor
from error_low_prameters import LowParametrs
from src.constants.error_state import ErrorAgreement

class PreprocessorManager:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_

    def process(self):
        if self.agree.agreement_.agreement_error > 0:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_low_paramaters
            return LowParametrs(self.agree).process()
        elif self.agree.agreement_.text is None:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_low_paramaters
            return LowParametrs(self.agree).process()
        elif self.agree.agreement_.agreenent_language is None:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_low_paramaters
            return LowParametrs(self.agree).process()
        elif self.agree.agreement_.agreement_input_type is None:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_low_paramaters
            return LowParametrs(self.agree).process()
        elif self.agree.agreement_.agreement_output_type is None:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_low_paramaters
            return LowParametrs(self.agree).process()
        elif self.agree.agreement_.agreenent_context is None:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_low_paramaters
            return LowParametrs(self.agree).process()
        elif (self.agree.agreement_.agreenent_context is not None and self.agree.agreement_.agreenent_context)\
                and self.agree.agreement_.agreenent_context_text is None:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_low_paramaters
            return LowParametrs(self.agree).process()
        elif self.agree.agreement_.agreenent_language != Language.RUS\
                and self.agree.agreement_.agreenent_language != Language.ENG:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_low_paramaters
            return LowParametrs(self.agree).process()
        elif self.agree.agreement_.agreement_input_type != InputDataTypes.DOCX\
                and self.agree.agreement_.agreement_input_type != InputDataTypes.TEXT:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_low_paramaters
            return LowParametrs(self.agree).process()
        elif self.agree.agreement_.agreement_output_type != OutputDataTypes.DOCX\
                and self.agree.agreement_.agreement_output_type != OutputDataTypes.JSON\
                and self.agree.agreement_.agreement_output_type != OutputDataTypes.TAGGED_JSON:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_low_paramaters
            return LowParametrs(self.agree).process()
        elif self.agree.agreement_.agreement_input_type == InputDataTypes.TEXT:
            return TextPreprocessor(self.agree).process()
        elif self.agree.agreement_.agreement_input_type == InputDataTypes.DOCX:
            return DocxPreprocessor(self.agree).process()

