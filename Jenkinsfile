pipeline {
    agent any

    stages {
        stage('Dokcer-Build') {
            steps {
                sh '''docker build -f Dockerfile -t projectr .'''
            }
        },
        stage('Dokcer-Run') {
            steps {
                sh '''docker run -d -p 8787:8787 --name myContainerName -e USER='admin' -e PASSWORD='password' -e ROOT=TRUE projectr'''
            }
        }
    }
}
