pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '-e HOME=/tmp'
        }
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}
