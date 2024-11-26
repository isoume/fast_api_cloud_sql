pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                sh """
                    sudo gcloud compute scp main.py worker-data-processing-dev:/home --zone=europe-west1-b
                """
            }
        }
    }
}