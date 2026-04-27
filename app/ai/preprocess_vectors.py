import fasttext
import numpy as np
import pickle

BIN_PATH = "app/ai/model/cc.ko.300.bin"
WORDS_PATH = "app/ai/model/words.pkl"
VECTORS_PATH = "app/ai/model/vectors.npy"

MAX_WORDS = 100000


def build_small_vector_files():
    print("모델 로딩 중...", flush=True)
    model = fasttext.load_model(BIN_PATH)
    print("모델 로딩 완료", flush=True)
    source_words = model.get_words(on_unicode_error="ignore")[:MAX_WORDS]
    print(f"추출 대상 단어 수: {len(source_words)}", flush=True)
    
    

    words = []
    vectors = []

    for i, word in enumerate(source_words):
        try:
            vector = model.get_word_vector(word).astype(np.float32)

            norm = np.linalg.norm(vector)
            if norm != 0:
                vector = vector / norm

            # 반드시 동시에 저장
            words.append(word)
            vectors.append(vector)

        except Exception as e:
            print("skip:", word, e)

        if (i + 1) % 10000 == 0:
            print(f"{i + 1}개 처리 완료")

    # 검증
    assert len(words) == len(vectors), "words 와 vectors 개수가 다릅니다."

    vectors_np = np.vstack(vectors).astype(np.float32)

    with open(WORDS_PATH, "wb") as f:
        pickle.dump(words, f)

    np.save(VECTORS_PATH, vectors_np)

    print("저장 완료")
    print("words:", len(words))
    print("vectors shape:", len(vectors_np))


if __name__ == "__main__":
    build_small_vector_files()