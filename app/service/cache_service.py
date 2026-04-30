
from app.ai.similarity import get_nearest_cached
from app.ai.similarity_in_vector import get_nearest_cached_in_vector
from app.core.error.error_code import ErrorCode
from app.core.exceptions.exceptions import InternalServerException, ServiceException


    
def set_nearest_cache(target_word: str = "사과", topn: int = 1000):
    try:
        get_nearest_cached_in_vector(target_word, topn)
        print(f"캐시 워밍 완료: {target_word}")
        
    except ServiceException :
        raise
    except Exception as e:
        raise InternalServerException(ErrorCode.INTERNAL_SERVER_ERROR,f"캐시 생성 실패: {str(e)}")