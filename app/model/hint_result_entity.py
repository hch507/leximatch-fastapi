from pydantic import BaseModel
class HintResult(BaseModel):
    word : str
    similarity_score: str
    ranking: str