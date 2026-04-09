import numpy as np
from app.ai.model_loader import load_model
from app.model.similarity_result_entity import SimilarityResult


def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def compute_similarity_score(target_word: str, predicted_word: str, topn: int = 1000):
    try:
        # 모델 로드 (이미 로드되어 있으면 재사용)
        model = load_model()

        # 단어 벡터 가져오기
        vec1 = model.get_word_vector(target_word)
        vec2 = model.get_word_vector(predicted_word)

        # 코사인 유사도 계산
        similarity = cosine_similarity(vec1, vec2)

        # 점수 변환 (-1 ~ 1 → -100 ~ 100)
        similarity_score =  str(round(similarity * 100, 2))

        # 유사한 단어 목록에서 ranking 찾기
        nearest = model.get_nearest_neighbors(target_word, k=topn)

        ranking = next(
            (i + 1 for i, (sim, word) in enumerate(nearest) if word == predicted_word),
            None
        )
        print(f"Predicted word: {predicted_word}, Ranking: {ranking}")
        
        return SimilarityResult(similarity_score=similarity_score, ranking=str(ranking))

    except Exception as e:
         raise e