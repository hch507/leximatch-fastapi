
class ServiceException(Exception):
    def __init__(self, message: str, code : int ):
        super().__init__(message)
        self.message = message
        self.code = code
        
        
class ValidationException(ServiceException):
    def __init__(self, message: str = "잘못된 요청입니다"):
        super().__init__(message, 400)
        
        
class NotFoundException(ServiceException):
    def __init__(self, message: str = "데이터를 찾을 수 없습니다"):
        super().__init__(message, 404)
        

class InternalServerException(ServiceException):
    def __init__(self, message="서버 오류"):
        super().__init__(message, 500)