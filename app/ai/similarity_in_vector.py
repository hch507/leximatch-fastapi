import random
import numpy as np
from app.ai.vector_loader import load_vectors, get_word_vector
from app.core.error.error_code import ErrorCode
from app.core.filter.word_filter import is_korean_word
from app.model.similarity_result_entity import SimilarityResult
from app.model.hint_result_entity import HintResult
_NEAREST_CACHE = {}




def get_nearest_cached_in_vector(target_word: str, topn: int):
    key = f"{target_word}:{topn}"

    print(
        f"[캐시 조회] key={key}, cache_keys={list(_NEAREST_CACHE.keys())}",
        flush=True
    )

    if key not in _NEAREST_CACHE:
        print("유사단어 캐싱 생성 중...", flush=True)

        words, vectors, word_to_index = load_vectors()

        target_vec = get_word_vector(target_word)

        scores = vectors @ target_vec

        # 전체 정렬
        sorted_indices = np.argsort(-scores)

        nearest = []
        rank_map = {}

        rank = 1

        for idx in sorted_indices:
            word = words[idx]

            if word == target_word:
                continue

            # 한글 단어만 허용
            if not is_korean_word(word):
                continue

            score = float(scores[idx])

            nearest.append((score, word))
            rank_map[word] = rank
            print(
                f"[캐시 저장] rank={rank}, word={word}, score={round(score * 100, 2)}",
                flush=True
            )
            rank += 1

            if rank > topn:
                break

        _NEAREST_CACHE[key] = {
            "nearest": nearest,
            "rank_map": rank_map
        }

        print(
            f"유사단어 캐싱 생성 완료: {len(nearest)}개",
            flush=True
        )

    return _NEAREST_CACHE[key]

def get_random_hint_word(
    target_word: str,
    start_rank: int = 10,
    end_rank: int = 200,
    topn: int = 1000
):
    nearest_data = get_nearest_cached_in_vector(target_word, topn)

    nearest = nearest_data["nearest"]
    rank_map = nearest_data["rank_map"]

    target_range = nearest[start_rank - 1:end_rank]

    if not target_range:
        return None

    _, random_word = random.choice(target_range)
    
    # 유사도 계산
    vec1 = get_word_vector(target_word)
    vec2 = get_word_vector(random_word)

    similarity = float(np.dot(vec1, vec2))
    similarity_score = str(round(similarity * 100, 2))

    return HintResult(
        word=random_word,
        dist=similarity_score,
        ranking=str(rank_map[random_word])
    )
      
        



def compute_similarity_score_in_vector(target_word: str, predicted_word: str, topn: int = 1000):

    vec1 = get_word_vector(target_word)
    vec2 = get_word_vector(predicted_word)

    similarity = float(np.dot(vec1, vec2))
    similarity_score = str(round(similarity * 100, 2))

    nearest = get_nearest_cached_in_vector(target_word, topn)

    ranking = nearest["rank_map"].get(predicted_word)


    print(
        f"[직접검색] target={target_word}, input={predicted_word}, rank={ranking}",
        flush=True
    )

    return SimilarityResult(
        similarity_score=similarity_score,
        ranking=str(ranking) if ranking is not None else f"+{topn}"
    )
