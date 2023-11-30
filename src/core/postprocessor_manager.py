from agreement_state import AgreementState
from src.constants.output_data_types import OutputDataTypes
from json_tagged_postprocessor import TaggedJSONPostprocessor
from json_postprocessor import JSONPostprocessor
from docx_postprocesor import DocxPostprocessor
from error_postprocessor import ErrorPostprocessor

class PostprocessorManager:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_

    def process(self):
        if self.agree.agreement_.agreement_output_type == OutputDataTypes.DOCX\
                and self.agree.agreement_.agreement_error == 0:
            return DocxPostprocessor(self.agree).process()
        elif self.agree.agreement_.agreement_output_type == OutputDataTypes.JSON\
                and self.agree.agreement_.agreement_error == 0:
            return JSONPostprocessor(self.agree).process()
        elif self.agree.agreement_.agreement_output_type == OutputDataTypes.TAGGED_JSON\
                and self.agree.agreement_.agreement_error == 0:
            return TaggedJSONPostprocessor(self.agree).process()
        else:
            return ErrorPostprocessor(self.agree).process()