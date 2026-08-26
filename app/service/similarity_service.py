# from fastapi import HTTPException
import random

from app.ai.model_loader import load_model
from app.ai.similarity import compute_similarity_score, get_nearest_cached
from app.ai.similarity_in_vector import compute_similarity_score_in_vector, get_random_hint_word
from app.ai.vector_loader import load_vectors
from app.core.error.error_code import ErrorCode
from app.core.exceptions.exceptions import InternalServerException, ServiceException, ValidationException
from app.model.initial_hint_result_entity import InitialHintResult
from app.model.total_result_entity import TatalResult
from app.util.hint import extract_jamo



# Service 레벨에서 load_model 래핑
def load_model_service():
    """Service에서 모델 로드 호출"""
    load_model()
    
def load_vector_service():
    """Service에서 vector 로드 호출"""
    try:
        load_vectors()
    except ServiceException :
        raise
    
    except Exception :
        raise InternalServerException(ErrorCode.INTERNAL_SERVER_ERROR,"벡터 로딩 실패")


    

def get_similarity_result(keyword: str, userInput: str):
    
    if not keyword or not userInput:
        raise ValidationException(ErrorCode.INVALID_INPUT,"keyword 또는 userInput이 비어있습니다")
    
    
    try:
        result = compute_similarity_score_in_vector(keyword, userInput)

        return TatalResult(
            keyword=keyword,
            userInput=userInput,
            dist=result.similarity_score,
            ranking=result.ranking
        )
    except ServiceException :
        raise
    
    except Exception:
        raise InternalServerException(ErrorCode.INTERNAL_SERVER_ERROR,f"유사도 계산 실패:")


def get_hint_result(
        keyword: str, 
        min_rank: int,
        max_rank: int
    ):
    
    print(
        f"[힌트 요청] keyword={keyword}, "
        f"min_rank={min_rank}, "
        f"max_rank={max_rank}"
    )
    if not keyword:
        raise ValidationException(
            ErrorCode.INVALID_INPUT,
            "keyword가 비어있습니다"
        )

    try:
        result = get_random_hint_word(
            target_word=keyword,
            start_rank=min_rank,
            end_rank=max_rank
        )

        return result

    except ServiceException:
        raise

    except Exception:
        raise InternalServerException(
            ErrorCode.INTERNAL_SERVER_ERROR,
            "힌트 조회 실패"
        )

def get_initial_hint_result(keyword: str):

    print(f"[글자 힌트 요청] keyword={keyword}")
   
    if not keyword:
        raise ValidationException(
            ErrorCode.INVALID_INPUT,
            "keyword가 비어있습니다"
        )

    try:
        jamos = extract_jamo(keyword)
    
        if not jamos:
            raise ValidationException(
                ErrorCode.INVALID_INPUT,
                "한글 단어가 아닙니다"
            )

        return InitialHintResult(
            initial=random.choice(jamos)
        )


    except ServiceException:
        raise

    except Exception:
        raise InternalServerException(
            ErrorCode.INTERNAL_SERVER_ERROR,
            "글자 힌트 조회 실패"
        )