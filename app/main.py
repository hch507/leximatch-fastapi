from fastapi import FastAPI
from app.api.leximatch_router import router as leximatch_router
from app.service.similarity_service import load_model_service

app = FastAPI()

# 라우터 등록
app.include_router(leximatch_router)

@app.on_event("startup")
def startup_event():
    print("서버 시작! Service 통해 모델 미리 로드")
    load_model_service()