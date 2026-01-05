pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pytest'
            }
        }

        stage('Run App') {
            steps {
                sh 'python app.py'
            }
        }
    }
}

