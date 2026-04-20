from pydantic import BaseModel

class SimilarityResult(BaseModel):
    similarity_score: str
    ranking: str