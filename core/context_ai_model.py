from sentence_transformers import SentenceTransformer
from constants.tags import Tags
from constants.variables import DATA_FOLDER
from agreement_state import AgreementState
import numpy as np
import pickle
import os


class ContextAIModel:

    def __init__(self, agree_: 'AgreementState'):
        self.agree = agree_
        self.broken_model = False
        self.context_encode = None
        self._model = SentenceTransformer('all-MiniLM-L6-v2')
        path = os.path.join(DATA_FOLDER, 'vectors.pickle')
        self._vocab = pickle.load(open(path, 'rb'))
        self._vocab_size = len(self._vocab)
        '''
        try:
            self._model = SentenceTransformer('all-MiniLM-L6-v2')
            path = os.path.join(DATA_FOLDER, 'vectors.pickle')
            self._vocab = pickle.load(open(path, 'rb'))
            self._vocab_size = len(self._vocab)
        except:
            self.agree.agreement_.agreement_error = ErrorAgreement.error_model
            self.broken_model = True
        '''


    def encode_context(self, context: str):
        self.context_encode = self._model.encode(context.strip())
        return self._model.encode(context.strip())

    def show_model_state(self):
        return self.broken_model

    def encode_word(self, word):
        if word in self._vocab:
            return self._vocab[word]
        else:
            vector = self._model.encode(word)
            self._vocab[word] = vector
            return vector

    def _calculate_cosine_distance(self, vector_1: np.array, vector_2: np.array) -> float:
        tmp1 = np.sum(vector_1 * vector_2)
        tmp2 = np.sqrt(np.sum(vector_1 ** 2))
        tmp3 = np.sqrt(np.sum(vector_2 ** 2))
        return 1 - (tmp1 / (tmp2 * tmp3))

    def process(self, word="") -> float:
        encoded_word = self.encode_word(word)
        dist = self._calculate_cosine_distance(encoded_word, self.context_encode)
        if dist < 0.2:
            return Tags.WARNING
        return Tags.NEUTRAL

# ContextAIModel(AgreementState(Agreement()))