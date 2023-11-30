from agreement_state import AgreementState
from constants.tags import Tags
from torchtext.data.utils import get_tokenizer
from constants.variables import DATA_FOLDER
import torch
from torch import nn
import pickle
import os
from constants.language import Language


class TextClassificationModel(nn.Module):

    def __init__(self, vocab_size, embed_dim, num_class):
        super(TextClassificationModel, self).__init__()
        self.embedding = nn.EmbeddingBag(vocab_size, embed_dim, sparse=True)
        self.fc = nn.Linear(embed_dim, num_class)
        self.init_weights()

    def init_weights(self):
        initrange = 0.5
        self.embedding.weight.data.uniform_(-initrange, initrange)
        self.fc.weight.data.uniform_(-initrange, initrange)
        self.fc.bias.data.zero_()

    def forward(self, text, offsets):
        embedded = self.embedding(text, offsets)
        return self.fc(embedded)

class RiskAIModel:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_
        self.broken_model = False
        if self.agree.agreement_.agreenent_language == Language.RUS:
            path = os.path.join(DATA_FOLDER, 'binary_model.pth')
            # path = "/home/solomon/PycharmProjects/state_core/data/binary_model_eng.pth"
            self._tokenizer = get_tokenizer('spacy', language='ru_core_news_lg')
        else:
            path = os.path.join(DATA_FOLDER, 'binary_model_eng.pth')
            # path = "/home/solomon/PycharmProjects/state_core/data/binary_model.pth"
            self._tokenizer = get_tokenizer('spacy', language='en_core_web_lg')
        self._model = torch.load(path)
        path = os.path.join(DATA_FOLDER, 'binary_vocab.pickle')
        self._vocab = pickle.load(open(path, 'rb'))
        '''
        try:
            if self.agree.agreement_.agreenent_language == Language.RUS:
                path = os.path.join(DATA_FOLDER, 'binary_model.pth')
                # path = "data/binary_model_eng.pth"
                self._tokenizer = get_tokenizer('spacy', language='ru_core_news_lg')
            else:
                path = os.path.join(DATA_FOLDER, 'binary_model_eng.pth')
                # path = "data/binary_model.pth"
                self._tokenizer = get_tokenizer('spacy', language='en_core_web_lg')
            self._model = torch.load(path)
            path = os.path.join(DATA_FOLDER, 'binary_vocab.pickle')
            self._vocab = pickle.load(open(path, 'rb'))
        except:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_model
            self.broken_model = True
        '''
    def show_model_state(self):
        return self.broken_model

    def process(self, word="") -> int:
        text_pipeline = lambda x: self._vocab(self._tokenizer(x))
        with torch.no_grad():
            sentence = torch.tensor(text_pipeline(word))
            output = self._model(sentence, torch.tensor([0])).squeeze(0)
            output = torch.nn.functional.softmax(output, dim=0)
            if output[output.argmax(0)] > 0.80 and output.argmax(0) == 1:
                return Tags.WARNING
            return Tags.NEUTRAL

# test = Agreement()
# test.agreenent_language = Language.RUS
# RiskAIModel(AgreementState(test))