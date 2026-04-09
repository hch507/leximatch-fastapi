from fastapi import FastAPI
from fastapi import APIRouter
from app.model.common_result import ApiError, CommonResult, Payload
from app.service.similarity_service import get_similarity_result

router = APIRouter()

@router.get("/similarity")
def similarity(text1: str, text2: str):
    try:
        # Service 호출
        result = get_similarity_result(text1, text2)
        
        payload = Payload(data=result)
        response = CommonResult(
            resultCode="200",
            resultMsg="Success",
            payload=payload
        )
        return response

    except Exception as e:
        # 에러 발생 시 payload.error에 담기
        payload = Payload(error=ApiError(code="500", message=str(e)))
        response = CommonResult(
            resultCode="500",
            resultMsg="Failure",
            payload=payload
        )
        return response