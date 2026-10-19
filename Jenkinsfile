pipeline {
    agent any

    environment {
        STUDENT_NAME    = 'Nuradil'
        STUDENT_SURNAME = 'Tazhibayev'
        STUDENT_GROUP   = 'IT2-2310'
        STUDENT_ID      = '34608'
        IMAGE_NAME      = 'tazhibayev-nuradil-devops'
        CONTAINER_NAME  = 'tazhibayev-nuradil-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log -1 --oneline'
            }
        }

        stage('Build') {
            steps {
                echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"
                echo "Group: ${STUDENT_GROUP}"
                echo "Student ID: ${STUDENT_ID}"
                sh 'python3 -m py_compile app/app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'bash -n scripts/Tazhibayev_Nuradil_system.sh'
                sh 'python3 app/app.py'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
                sh 'docker images ${IMAGE_NAME}'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker rm -f ${CONTAINER_NAME} || true'
                sh '''
                    docker run \
                      -e STUDENT_NAME=${STUDENT_NAME} \
                      -e STUDENT_SURNAME=${STUDENT_SURNAME} \
                      -e STUDENT_GROUP=${STUDENT_GROUP} \
                      -e STUDENT_ID=${STUDENT_ID} \
                      --name ${CONTAINER_NAME} \
                      ${IMAGE_NAME}
                '''
            }
        }
    }

    post {
        success { echo 'Pipeline finished successfully' }
        failure { echo 'Pipeline failed' }
    }
}
