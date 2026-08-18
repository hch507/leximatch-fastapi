from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
WORDS_PATH = BASE_DIR / "valid_words.txt"
OUTPUT_SQL_PATH = BASE_DIR / "insert_words.sql"

BATCH_SIZE = 1000

with open(WORDS_PATH, "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

# 중복 제거
words = list(dict.fromkeys(words))

with open(OUTPUT_SQL_PATH, "w", encoding="utf-8") as f:

    f.write("-- 기존 데이터 삭제\n")
    f.write("DELETE FROM daily_word;\n")
    f.write("DELETE FROM word;\n\n")

    f.write("-- AUTO_INCREMENT 초기화\n")
    f.write("ALTER TABLE daily_word AUTO_INCREMENT = 1;\n")
    f.write("ALTER TABLE word AUTO_INCREMENT = 1;\n\n")

    f.write("-- 단어 삽입\n\n")

    for i in range(0, len(words), BATCH_SIZE):

        batch = words[i:i + BATCH_SIZE]

        values = []

        for word in batch:
            escaped = word.replace("'", "''")
            values.append(f"('{escaped}')")

        f.write("INSERT INTO word (content) VALUES\n")
        f.write(",\n".join(values))
        f.write(";\n\n")

print("SQL 생성 완료:", OUTPUT_SQL_PATH)
print("단어 수:", len(words))