from pydantic import BaseModel


class InitialHintRequest(BaseModel):
    answer: str