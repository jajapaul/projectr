pipeline {
    agent any

    stages {
        stage('Dokcer-Build') {
            steps {
                sh '''docker build -f Dockerfile -t projectr .'''
            }
        }
        stage('Dokcer-Run') {
            steps {
                sh '''docker run -d -p 8787:8787 --name rstudiocontainer -e USER='admin' -e PASSWORD='admin' -e ROOT=TRUE projectr'''
            }
        }
    }
}
