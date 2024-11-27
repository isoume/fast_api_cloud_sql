pipeline {
    agent any

    stages {
        stage('createEnvironment'){
            steps{
                sh """
                    sudo gcloud compute ssh worker-data-processing-dev --zone=europe-west1-b --project=doctolib-data-dev --command="mkdir -p /home/doctolib"
                """
            }
        }
        stage('MoveProject') {
            steps {

                sh """
                    sudo gcloud compute ssh worker-data-processing-dev --zone=europe-west1-b --project=doctolib-data-dev --command="mkdir -p /home/doctolib"
                """

                sh """
                    echo 'copying the files *.py'
                    sudo gcloud compute scp ./*.py worker-data-processing-dev:/home/doctolib --zone=europe-west1-b
                    echo 'copying the Dockerfile'
                    sudo gcloud compute scp Dockerfile worker-data-processing-dev:/home/doctolib --zone=europe-west1-b
                    echo 'copying the requirements.txt'
                    sudo gcloud compute scp requirements.txt worker-data-processing-dev:/home/doctolib --zone=europe-west1-b        
                    #nohup python3 /path/to/your_script.py > output.log
                """
            }
        }
        stage('BuildDocker'){
            steps{
                sh """
                    sudo gcloud compute ssh worker-data-processing-dev --zone=europe-west1-b --project=doctolib-data-dev --command="sudo docker build  /home/doctolib/Dockerfile -t api"
                """
            }
        }
    }
}