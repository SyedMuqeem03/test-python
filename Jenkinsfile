pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 --version
                python3 -m pip --version || python3 -m ensurepip
                python3 -m pip install --upgrade pip
                python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Run tests here"
            }
        }

        stage('Run App') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
