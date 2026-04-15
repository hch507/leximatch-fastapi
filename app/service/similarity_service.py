# from fastapi import HTTPException
from app.ai.model_loader import load_model
from app.ai.similarity import compute_similarity_score, get_nearest_cached
from app.model.total_result_entity import TatalResult


# Service 레벨에서 load_model 래핑
def load_model_service():
    """Service에서 모델 로드 호출"""
    load_model()
    target_word = "사과" 
    topn = 1000

    get_nearest_cached( target_word, topn)

    print(f"캐시 워밍 완료: {target_word}")
    

def get_similarity_result(keyword: str, userInput: str):
    

    result = compute_similarity_score(keyword, userInput)
    print(f"Predicted word: {keyword}, input: {userInput}, dist: {result.similarity_score} ,rank : {result.ranking}")
    return TatalResult(
        keyword=keyword,
        userInput=userInput,
        dist=result.similarity_score,
        ranking = result.ranking
    )
