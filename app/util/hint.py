
import random

CHOSUNG = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"

JUNGSUNG = [
    "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ",
    "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ",
    "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ",
    "ㅡ", "ㅢ", "ㅣ"
]

JONGSUNG = [
    "", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ",
    "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ",
    "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ",
    "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"
]


# def extract_jamo(word: str):
#     result = []

#     for char in word:
#         if '가' <= char <= '힣':
#             code = ord(char) - ord('가')

#             chosung_index = code // 588
#             jungsung_index = (code % 588) // 28
#             jongsung_index = code % 28

#             result.append(CHOSUNG[chosung_index])
#             result.append(JUNGSUNG[jungsung_index])

#             if jongsung_index != 0:
#                 result.append(JONGSUNG[jongsung_index])

#         else:
#             result.append(char)

#     return result



def extract_jamo(word: str):
    chars = [char for char in word if '가' <= char <= '힣']

    if not chars:
        return None

    return random.choice(chars)