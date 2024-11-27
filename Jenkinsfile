pipeline {
    agent any
    parameters {
        string(name: 'HOST', defaultValue: '10.38.0.3', description: 'Server')
        string(name: 'API_PASSWORD', description: 'Server')
    }
    stages {
        stage('createEnvironment'){
            steps{
                sh """
                    sudo gcloud compute ssh worker-data-processing-1-dev --zone=europe-west1-b --project=doctolib-data-dev --command="mkdir -p /home/doctolib"
                """
            }
        }
        stage('MoveProject') {
            steps {
                sh """
                    echo 'copying the files *.py'
                    sudo gcloud compute scp ./*.py worker-data-processing-1-dev:/home/doctolib --zone=europe-west1-b
                    echo 'copying the Dockerfile'
                    sudo gcloud compute scp Dockerfile worker-data-processing-1-dev:/home/doctolib --zone=europe-west1-b
                    echo 'copying the requirements.txt'
                    sudo gcloud compute scp requirements.txt worker-data-processing-1-dev:/home/doctolib --zone=europe-west1-b        
                    #nohup python3 /path/to/your_script.py > output.log
                """
            }
        }
        stage('BuildDocker'){
            steps{
                sh """
                    sudo gcloud compute ssh worker-data-processing-1-dev --zone=europe-west1-b\
                        --project=doctolib-data-dev \
                        --command="sudo docker build --build-arg PASSWORD=${API_PASSWORD} --build-arg HOST=${HOST} -t api /home/doctolib/"
                """
            }
        }
        stage("CleanOlderContainer"){
            steps{
                sh """
                    sudo gcloud compute ssh worker-data-processing-1-dev --zone=europe-west1-b\
                        --project=doctolib-data-dev \
                        --command="'sudo docker ps -a -q | xargs sudo docker rm -f'"
                """
            }
        }
        stage("DeployDocker"){
            steps{
                sh """
                    sudo gcloud compute ssh worker-data-processing-1-dev --zone=europe-west1-b\
                        --project=doctolib-data-dev \
                        --command="sudo docker run -d -p 8000:8000 api"
                """
            }
        }
    }
}