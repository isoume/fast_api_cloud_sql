pipeline {
    agent any
    parameters {
        string(name: 'HOST', defaultValue: '10.38.0.3', description: 'Server')
        string(name: 'API_PASSWORD', description: 'API_PASSWORD')
        string(name: 'DATA_BASE_NAME', description: 'DATA_BASE_NAME')
        string(name: 'PROJECT_ID', description: 'PROJECT_ID')
        string(name: 'VM_NAME', description: 'VM_NAME')
        string(name: 'VM_ZONE', description: 'VM_ZONE')
    }
    stages {
        stage('createEnvironment'){
            steps{
                sh """
                    sudo gcloud compute ssh ${VM_NAME} --zone=${VM_NAME} --project=${PROJECT_ID} --command="mkdir -p /home/doctolib"
                """
            }
        }
        stage('MoveProject') {
            steps {
                sh """
                    echo 'copying the files *.py'
                    sudo gcloud compute scp ./*.py ${VM_NAME}:/home/doctolib --zone=${VM_NAME}
                    echo 'copying the Dockerfile'
                    sudo gcloud compute scp Dockerfile ${VM_NAME}:/home/doctolib --zone=${VM_NAME}
                    echo 'copying the requirements.txt'
                    sudo gcloud compute scp requirements.txt ${VM_NAME}:/home/doctolib --zone=${VM_NAME}      
                """
            }
        }
        stage('BuildDocker'){
            steps{
                sh """
                    sudo gcloud compute ssh ${VM_NAME} --zone=${VM_NAME}\
                        --project=${PROJECT_ID} \
                        --command="sudo docker build --build-arg PASSWORD=${API_PASSWORD} --build-arg HOST=${HOST} -t api /home/doctolib/"
                """
            }
        }
        stage("CleanOlderContainer"){
            steps{
                sh """
                    sudo gcloud compute ssh ${VM_NAME} --zone=${VM_NAME}\
                        --project=${PROJECT_ID} \
                        --command="sudo docker ps -a -q | xargs -r sudo docker rm -f > /dev/null 2>&1"
                """
            }
        }
        stage("DeployDocker"){
            steps{
                sh """
                    sudo gcloud compute ssh ${VM_NAME} --zone=${VM_NAME}\
                        --project=${PROJECT_ID} \
                        --command="sudo docker run -e DATA_BASE_NAME=${DATA_BASE_NAME} -e PASSWORD=${API_PASSWORD} -e HOST=${HOST} -d -p 8000:8000 api"
                """
            }
        }
    }
}