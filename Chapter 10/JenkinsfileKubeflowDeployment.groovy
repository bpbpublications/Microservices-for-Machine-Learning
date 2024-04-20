
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                sh 'docker build -t my-model:$BUILD_NUMBER .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing the built model...'
                sh 'docker run my-model:$BUILD_NUMBER /bin/sh -c "python test.py"'
            }
        }
        stage('Deploy to Kubeflow') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying to Kubeflow...'
                sh 'python deploy_to_kubeflow.py $BUILD_NUMBER'
            }
        }
    }
}
