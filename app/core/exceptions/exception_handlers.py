
from http.client import HTTPException
from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.exceptions.exceptions import ServiceException

from app.model.common_result import Api, Result

def register_exception_handlers(app):

    @app.exception_handler(ServiceException)
    def service_exception_handler(request: Request, exc: ServiceException):
        return JSONResponse(
            status_code=exc.code,
            content=Api(
                result=Result(
                    resultCode=exc.code,
                    resultMessage="ERROR",
                    resultDescription=exc.message
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
                    resultCode=str(exc.status_code),
                    resultMessage="ERROR",
                    resultDescription=exc.detail
                ),
                body=None
            ).dict()
        )
    
    def global_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content=Api(
                result=Result(
                    resultCode="500",
                    resultMessage="ERROR",
                    resultDescription=str(exc)
                ),
                body=None
            ).dict()
        )