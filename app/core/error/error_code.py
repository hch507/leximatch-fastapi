from enum import Enum



from enum import Enum
from fastapi import status

class ErrorCode(Enum):
    OK = (200, status.HTTP_200_OK, "SUCCESS")

    INVALID_INPUT = (4001, status.HTTP_200_OK, "INVALID_INPUT")
    WORD_NOT_IN_DICTIONARY = (4003, status.HTTP_200_OK, "WORD_NOT_IN_DICTIONARY")
    
    NOT_FOUND = (4040, status.HTTP_200_OK, "NOT_FOUND_DATA")
    
    INTERNAL_SERVER_ERROR = (5000, status.HTTP_200_OK, "SERVER_ERROR")
    MODEL_LOAD_FAIL = (5001, status.HTTP_200_OK, "MODEL_LOAD_FAIL")

    def __init__(self, code, http_status, message):
        self.code = code
        self.http_status = http_status
        self.message = message