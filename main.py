from app.service.similarity_service import get_similarity_result

if __name__ == "__main__":
    # 테스트용 입력
    target = "바나나"
    predicted = "망고"

    # service 직접 호출
    result = get_similarity_result(target, predicted)

    print("=== Service 호출 결과 ===")
    print(result)