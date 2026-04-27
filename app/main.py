from fastapi import FastAPI
from app.api.leximatch_router import router as leximatch_router
from app.core.exceptions.exception_handlers import register_exception_handlers
from app.service.similarity_service import load_model_service, load_vector_service

app = FastAPI()

# 라우터 등록
app.include_router(leximatch_router)
register_exception_handlers(app)

@app.on_event("startup")
def startup_event():
    print("서버 시작! Service 통해 모델 미리 로드")
    load_vector_service()
    # load_model_service()
    
    