
import re

KOREAN_WORD_PATTERN = re.compile(r"^[가-힣]+$")


def is_korean_word(word: str) -> bool:
    return bool(KOREAN_WORD_PATTERN.fullmatch(word))