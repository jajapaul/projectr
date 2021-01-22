pipeline {
    agent any

    stages {
        stage('Dokcer-Build') {
            steps {
                sh '''docker build -f Dockerfile.R -t projectr .'''
            }
        }
        stage('Dokcer-Run') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'projectr', passwordVariable: 'password', usernameVariable: 'user')]) {
                    // some block
                    sh '''docker run -d -p 8787:8787 --name rstudiocontainer -e USER="${user}" -e PASSWORD="${password}" -e ROOT=TRUE projectr'''
                }
                
            }
        }
    }
}
