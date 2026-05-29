from pathlib import Path
import pickle
from collections import Counter

BASE_DIR = Path(__file__).resolve().parent
WORDS_DIR = BASE_DIR / "words"
VOCAB_PATH = Path("app/ai/model/words.pkl")

with open(VOCAB_PATH, "rb") as f:
    vocab = set(pickle.load(f))

all_words = []

for txt_file in WORDS_DIR.glob("*.txt"):
    with open(txt_file, encoding="utf-8") as f:
        words = [
            line.strip()
            for line in f
            if line.strip()
        ]

    print(f"{txt_file.name}: {len(words)}개")
    all_words.extend(words)

counter = Counter(all_words)

duplicates = [
    word for word, count in counter.items()
    if count > 1
]

unique_words = list(dict.fromkeys(all_words))

valid_words = []
invalid_words = []

for word in unique_words:
    if word in vocab:
        valid_words.append(word)
    else:
        invalid_words.append(word)

print("전체 단어 수:", len(all_words))
print("중복 제거 후:", len(unique_words))
print("중복 단어 수:", len(duplicates))
print("사용 가능:", len(valid_words))
print("사용 불가:", len(invalid_words))

OUTPUT_PATH = BASE_DIR / "valid_words.txt"

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    for word in valid_words:
        f.write(f"{word}\n")

print(f"\n저장 완료: {OUTPUT_PATH}")
print(f"저장된 단어 수: {len(valid_words)}")

print("\n==============================")
print("중복 단어 목록")
print("==============================")

for word in sorted(duplicates):
    print(word)

print("\n==============================")
print("사용 불가 단어 목록")
print("==============================")

for word in sorted(invalid_words):
    print(word)