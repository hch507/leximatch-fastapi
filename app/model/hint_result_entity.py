from pydantic import BaseModel
class HintResult(BaseModel):
    word : str
    dist: str
    ranking: str