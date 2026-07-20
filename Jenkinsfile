pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check') {
            steps {
                sh 'echo "GitHub 연동 성공!"'
                sh 'pwd'
                sh 'ls -la'
            }
        }
    }
}