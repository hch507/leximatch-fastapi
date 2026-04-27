# from fastapi import HTTPException
from app.ai.model_loader import load_model
from app.ai.similarity import compute_similarity_score, get_nearest_cached
from app.ai.similarity_in_vector import compute_similarity_score_in_vector
from app.ai.vector_loader import load_vectors
from app.core.exceptions.exceptions import InternalServerException, ValidationException
from app.model.total_result_entity import TatalResult



# Service 레벨에서 load_model 래핑
def load_model_service():
    """Service에서 모델 로드 호출"""
    load_model()
    
def load_vector_service():
    """Service에서 vector 로드 호출"""
    load_vectors()


    

def get_similarity_result(keyword: str, userInput: str):
    
    if not keyword or not userInput:
        raise ValidationException("keyword 또는 userInput이 비어있습니다")
    
    
    try:
        result = compute_similarity_score_in_vector(keyword, userInput)

        return TatalResult(
            keyword=keyword,
            userInput=userInput,
            dist=result.similarity_score,
            ranking=result.ranking
        )

    except Exception as e:
        raise InternalServerException(f"유사도 계산 실패: {str(e)}")
