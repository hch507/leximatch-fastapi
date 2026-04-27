import numpy as np
from app.ai.vector_loader import load_vectors, get_word_vector
from app.model.similarity_result_entity import SimilarityResult

_NEAREST_CACHE = {}


def get_nearest_cached_in_vector(target_word: str, topn: int):
    key = f"{target_word}:{topn}"

    print("유사단어 캐싱 확인...", flush=True)

    if key not in _NEAREST_CACHE:
        print("유사단어 캐싱 생성 중...", flush=True)

        words, vectors, word_to_index = load_vectors()

        target_vec = get_word_vector(target_word)

        if target_vec is None:
            raise ValueError(f"사전에 없는 단어입니다: {target_word}")

        # vectors는 이미 normalize 되어 있으므로 dot product = cosine similarity
        scores = vectors @ target_vec

        # 자기 자신까지 포함될 수 있어서 topn + 1
        top_indices = np.argsort(-scores)[:topn + 1]

        nearest = []
        rank_map = {}

        rank = 1

        for idx in top_indices:
            word = words[idx]

            if word == target_word:
                continue

            score = float(scores[idx])

            nearest.append((score, word))
            rank_map[word] = rank

            rank += 1

            if rank > topn:
                break

        _NEAREST_CACHE[key] = {
            "nearest": nearest,
            "rank_map": rank_map
        }

        print("유사단어 캐싱 생성 완료", flush=True)
        
        print(f"\n[{target_word}] 유사단어 TOP {topn}")
        for i, (score, word) in enumerate(nearest, start=1):
            print(f"{i:4d}위 | {word:<20} | score={score:.4f}")

    return _NEAREST_CACHE[key]


def compute_similarity_score_in_vector(target_word: str, predicted_word: str, topn: int = 1000):
    try:
        print("STEP 1", flush=True)

        vec1 = get_word_vector(target_word)
        vec2 = get_word_vector(predicted_word)

        if vec1 is None:
            raise ValueError(f"사전에 없는 단어입니다: {target_word}")

        if vec2 is None:
            raise ValueError(f"사전에 없는 단어입니다: {predicted_word}")

        print("STEP 2", flush=True)

    
        similarity = float(np.dot(vec1, vec2))

        similarity_score = str(round(similarity * 100, 2))

        print("STEP 3", flush=True)

        nearest = get_nearest_cached_in_vector(target_word, topn)

        ranking = nearest["rank_map"].get(predicted_word)

        print("STEP 4", flush=True)
        print(f"Predicted word: {predicted_word}, Ranking: {ranking}", flush=True)

        return SimilarityResult(
            similarity_score=similarity_score,
            ranking=str(ranking) if ranking is not None else f"+{topn}"
        )

    except Exception as e:
        print("ERROR OCCURRED:", e, flush=True)
        raise e