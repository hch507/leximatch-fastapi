import pickle
import numpy as np

_words = None
_vectors = None
_word_to_index = None


def load_vectors():
    global _words, _vectors, _word_to_index

    if _vectors is None:
        print("벡터 로딩 중...")

        with open("app/ai/model/words.pkl", "rb") as f:
            _words = pickle.load(f)

        _vectors = np.load("app/ai/model/vectors.npy")

        _word_to_index = {
            word: i for i, word in enumerate(_words)
        }

        print("벡터 로딩 완료")

    return _words, _vectors, _word_to_index

def get_word_vector(word: str):
    words, vectors, word_to_index = load_vectors()

    idx = word_to_index.get(word)

    if idx is None:
        return None

    return vectors[idx]