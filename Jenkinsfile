pipeline {
    agent any

    stages {
        stage('Clone source') {
            steps {
                git url: 'https://github.com/alex-pancho/qalight_py_010825', branch: 'main'
            }
        }
        stage('Build and activate venv') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip==24.3.1
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -s -v "$WORKSPACE/lesson_18" --junitxml=$WORKSPACE/report.xml
                '''
                junit '**/report.xml'
            }
        }
    }
}