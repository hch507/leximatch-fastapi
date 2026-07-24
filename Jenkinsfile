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

        // stage('Deploy') {
        //     steps {
        //         sh '''
        //             docker stop leximatch-fastapi || true
        //             docker rm leximatch-fastapi || true

        //             docker run -d \
        //               --name leximatch-fastapi \
        //               --network ai-net\
        //               --restart unless-stopped \
        //               -v /home/ubuntu/model:/app/app/ai/model \
        //               leximatch-fastapi
        //         '''
        //     }
        // }
        stage('Deploy') {
            steps {
                sh '''
                    docker stop leximatch-fastapi-1 || true
                    docker rm leximatch-fastapi-1 || true
                    docker stop leximatch-fastapi-2 || true
                    docker rm leximatch-fastapi-2 || true

                    # FastAPI 1
                    docker run -d \
                      --name leximatch-fastapi-1 \
                      --network ai-net \
                      --restart unless-stopped \
                      -v /home/ubuntu/model:/app/app/ai/model \
                      leximatch-fastapi:latest

                    # FastAPI 2
                    docker run -d \
                      --name leximatch-fastapi-2 \
                      --network ai-net \
                      --restart unless-stopped \
                      -v /home/ubuntu/model:/app/app/ai/model \
                      leximatch-fastapi:latest

                    docker image prune -f
                '''
            }
        }

    }
}