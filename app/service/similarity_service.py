# from fastapi import HTTPException
from app.ai.model_loader import load_model
from app.ai.similarity import compute_similarity_score
from app.model.total_result_entity import TatalResult


# Service 레벨에서 load_model 래핑
def load_model_service():
    """Service에서 모델 로드 호출"""
    return load_model()

def get_similarity_result(keyword: str, userInput: str):
    

    result = compute_similarity_score(keyword, userInput)
    print(f"Predicted word: {keyword}, input: {userInput}, dist: {result.similarity_score} ,rank : {result.ranking}")
    return TatalResult(
        keyword=keyword,
        userInput=userInput,
        dist=result.similarity_score,
        ranking = result.ranking
    )
