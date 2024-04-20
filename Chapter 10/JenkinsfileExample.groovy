
pipeline {
    agent any

    stages {
        stage('Check Data Quality') {
            steps {
                sh 'python scripts/data_validation.py'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python scripts/train_model.py'
            }
        }
        stage('Test Model') {
            steps {
                sh 'python scripts/test_model.py'
            }
        }
        stage('Deploy Model') {
            steps {
                sh 'python scripts/deploy_model.py'
            }
        }
    }
    post {
        success {
            echo 'The pipeline succeeded!'
        }
        failure {
            echo 'The pipeline failed.'
        }
    }
}
