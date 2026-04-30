from asyncio.log import logger
import pickle
import numpy as np
from app.core.error.error_code import ErrorCode

from app.core.exceptions.exceptions import InternalServerException, ServiceException, ValidationException

_words = None
_vectors = None
_word_to_index = None


def load_vectors():
    global _words, _vectors, _word_to_index

    if _vectors is None:
        try:
            print("벡터 로딩 중...")

            with open("app/ai/model/words.pkl", "rb") as f:
                _words = pickle.load(f)

            _vectors = np.load("app/ai/model/vectors.npy")

            _word_to_index = {
                word: i for i, word in enumerate(_words)
            }

            print("벡터 로딩 완료")

        except FileNotFoundError:
            raise InternalServerException(
                ErrorCode.MODEL_LOAD_FAIL,
                "벡터 파일을 찾을 수 없습니다.")

    return _words, _vectors, _word_to_index

def get_word_vector(word: str):
   
    if not word or not word.strip():
        raise ValidationException(
            ErrorCode.INVALID_INPUT,
            "단어가 비어있습니다."
        )

    words, vectors, word_to_index = load_vectors()

    idx = word_to_index.get(word)

    if idx is None:
        raise ValidationException(
            ErrorCode.WORD_NOT_IN_DICTIONARY,
            f"{word}는 사전에 없습니다."
        )

    return vectors[idx]


   