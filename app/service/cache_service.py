
from app.ai.similarity import get_nearest_cached
from app.ai.similarity_in_vector import get_nearest_cached_in_vector
from app.core.exceptions.exceptions import InternalServerException


    
def set_nearest_cache(target_word: str = "사과", topn: int = 1000):
    try:
        get_nearest_cached_in_vector(target_word, topn)
        print(f"캐시 워밍 완료: {target_word}")
    except Exception as e:
        raise InternalServerException(f"캐시 생성 실패: {str(e)}")