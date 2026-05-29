import re
import fasttext
import numpy as np
import pickle

BIN_PATH = "app/ai/model/cc.ko.300.bin"
WORDS_PATH = "app/ai/model/words.pkl"
VECTORS_PATH = "app/ai/model/vectors.npy"

MAX_WORDS = 200000
KOREAN_PATTERN = re.compile(r"^[가-힣]+$")

MAX_SKIP_LOG = 100


def build_small_vector_files():
    print("모델 로딩 중...", flush=True)
    model = fasttext.load_model(BIN_PATH)
    print("모델 로딩 완료", flush=True)

    source_words = model.get_words(on_unicode_error="ignore")
    print(f"전체 원본 단어 수: {len(source_words)}", flush=True)

    words = []
    vectors = []

    skip_count = 0
    error_count = 0

    for i, word in enumerate(source_words):

        if len(words) >= MAX_WORDS:
            break

        if not KOREAN_PATTERN.match(word):
            if skip_count < MAX_SKIP_LOG:
                print(f"[SKIP] {word}")
            skip_count += 1
            continue

        try:
            vector = model.get_word_vector(word).astype(np.float32)

            norm = np.linalg.norm(vector)
            if norm != 0:
                vector = vector / norm

            words.append(word)
            vectors.append(vector)

        except Exception as e:
            print(f"[ERROR] {word}: {e}")
            error_count += 1
            continue

        if len(words) % 10000 == 0:
            print(f"{len(words)}개 저장 완료 / 원본 {i + 1}개 확인")

    assert len(words) == len(vectors), "words 와 vectors 개수가 다릅니다."

    vectors_np = np.vstack(vectors).astype(np.float32)

    with open(WORDS_PATH, "wb") as f:
        pickle.dump(words, f)

    np.save(VECTORS_PATH, vectors_np)

    print("저장 완료")
    print("저장 단어 수:", len(words))
    print("vectors shape:", vectors_np.shape)
    print("제외 단어 수:", skip_count)
    print("에러 단어 수:", error_count)


if __name__ == "__main__":
    build_small_vector_files()