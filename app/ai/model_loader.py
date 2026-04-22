import fasttext

from app.core.exceptions.exceptions import InternalServerException 
model_path = "app/ai/model/cc.ko.300.bin"

ft_model = None

def load_model():
    global ft_model
    try:
        if ft_model is None:
            print("모델 로딩 중...")
            ft_model = fasttext.load_model(model_path)
            print("모델 로딩 완료")
        return ft_model
    except Exception:
       raise InternalServerException("모델 로딩 실패")
