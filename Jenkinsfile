//BUILD_NUMBER 태그 붙이기 (leximatch-fastapi:15)
// latest도 함께 태그
// 롤백 기능 추가
// 테스트 컨테이너 추가
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                    docker build -t leximatch-fastapi .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop leximatch-fastapi || true
                    docker rm leximatch-fastapi || true

                    docker run -d \
                      --name leximatch-fastapi \
                      --network leximatch-net \
                      -p 8000:8000 \
                      -v /home/ubuntu/model:/app/app/ai/model \
                      leximatch-fastapi
                '''
            }
        }
    }
}