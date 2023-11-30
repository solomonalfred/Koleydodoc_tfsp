from agreement_state import AgreementState
from nltk.tokenize import word_tokenize
from context_ai_model import ContextAIModel
from error_model import BrokenModel
from src.core.postprocessor_manager import PostprocessorManager

class ContextBasedProcessor:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_
        self.__context_processor = ContextAIModel(self.agree)
        self.broken_model = False
        if self.__context_processor.show_model_state():
            self.broken_model = True

    def process(self):
        if self.broken_model:
            return BrokenModel(self.agree).process()
        else:
            self.__context_processor.encode_context(self.agree.agreement_.agreenent_context_text)
            text = []
            for paragraph in self.agree.agreement_.text:
                paragraph_tag = []
                for sentence in paragraph:
                    words = word_tokenize(sentence)
                    dist = 0.0
                    for word in words:
                        dist = self.__context_processor.process(word)
                        if dist:
                            break
                    paragraph_tag.append(dist)
                text.append(paragraph_tag)
            self.agree.agreement_.agreement_marked = text
            return PostprocessorManager(self.agree).process()
