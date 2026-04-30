
from app.core.error.error_code import ErrorCode


class ServiceException(Exception):
    def __init__(self, error_code, description=None):
        self.code = error_code.code             # resultCode
        self.http_status = error_code.http_status # HTTP status
        self.message = error_code.message
        self.description = description or error_code.message
        
        
        
class ValidationException(ServiceException):
    def __init__(self, error_code, description=None):
        super().__init__(error_code, description)
        
        
class NotFoundException(ServiceException):
    def __init__(self, message: str = "데이터를 찾을 수 없습니다"):
        super().__init__(ErrorCode.NOT_FOUND, message)
        

class InternalServerException(ServiceException):
    def __init__(self, error_code, description=None):
        super().__init__(error_code, description)
        
