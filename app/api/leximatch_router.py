from fastapi import FastAPI
from fastapi import APIRouter
from app.model.common_result import Api, Result
from app.service.cache_service import set_nearest_cache

from app.service.similarity_service import get_hint_result, get_similarity_result

router = APIRouter()


@router.get("/similarity")
def similarity(text1: str, text2: str):

        # Service 호출
        result = get_similarity_result(text1, text2)
        
        return Api(
            result = Result(
                resultCode=200,
                resultMessage="OK",
                resultDescription="success"
            ),
            body = result
        )

@router.get("/cache/warmup")
def set_cache(target_word : str):
   
        set_nearest_cache(target_word)
        return Api(
            result = Result(
                resultCode=200,
                resultMessage="OK",
                resultDescription="success"
            ),
            body = target_word
        )


@router.get("/hint")
def get_hint(target_word:str):
        result= get_hint_result(target_word)
       
        return Api(
            result = Result(
                resultCode=200,
                resultMessage="OK",
                resultDescription="success"
            ),
            body = result
        )
