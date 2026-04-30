
from http.client import HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions.exceptions import ServiceException

from app.model.common_result import Api, Result

def register_exception_handlers(app):

    @app.exception_handler(ServiceException)
    def service_exception_handler(request: Request, exc: ServiceException):
        return JSONResponse(
            status_code=exc.http_status,
            content=Api(
                result=Result(
                    resultCode=exc.code,
                    resultMessage=exc.message,
                    resultDescription=exc.description
                ),
                body=None
            ).dict()
        )

    @app.exception_handler(HTTPException)
    def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content=Api(
                result=Result(
                    resultCode=exc.status_code,
                    resultMessage="HTTP_ERROR",
                    resultDescription=str(exc.detail)
                ),
                body=None
            ).dict()
        )

    
    @app.exception_handler(Exception)
    def global_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=Api(
                result=Result(
                    resultCode=ErrorCode.INTERNAL_SERVER_ERROR.code,
                    resultMessage=ErrorCode.INTERNAL_SERVER_ERROR.message,
                    resultDescription="서버 오류가 발생했습니다"
                ),
                body=None
            ).dict()
        )