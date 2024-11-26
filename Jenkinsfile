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
        stage('createEnvironment'){
            steps{
                sh """
                    sudo gcloud compute ssh worker-data-processing-dev --zone=europe-west1-b --project=doctolib-data-dev --command="mkdir -p /home/doctolib"
                """
            }
        }
        stage('Deploy') {
            steps {
                sh """
                    sudo gcloud compute scp ./*.py worker-data-processing-dev:/home/doctolib --zone=europe-west1-b
                    sudo gcloud compute scp Dockerfile worker-data-processing-dev:/home/doctolib --zone=europe-west1-b                    sudo gcloud compute scp ./*.py worker-data-processing-dev:/home/doctolib --zone=europe-west1-b
                    sudo gcloud compute scp requirements.txt worker-data-processing-dev:/home/doctolib --zone=europe-west1-b        
                    #nohup python3 /path/to/your_script.py > output.log
                """
            }
        }
    }
}