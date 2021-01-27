pipeline {
    agent any

    stages {
        stage('Docker-Build') {
            steps {
                sh '''docker build -f Dockerfile.R -t projectr .'''
            }
        }
        stage('Docker-Run1') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'projectr', passwordVariable: 'password', usernameVariable: 'user')]) {
                    // some block
                    sh "docker run -d -p 8787:8787 --name rstudio.dev -e USER=${user} -e PASSWORD=${password} -e ROOT=TRUE projectr"
                }
                
            }
        }

    stage('Docker-Run2') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'projectr', passwordVariable: 'password', usernameVariable: 'user')]) {
                    // some block
                    sh "docker run -d -p 8788:8788 --name rstudio.test -e USER=${user} -e PASSWORD=${password} -e ROOT=TRUE projectr"
                }
                
            }
        }

        stage('Docker-Test') {
            steps {
                echo 'Validating if container is running..!'
                sh 'docker ps | grep projectr | docker inspect'
            }
        }
    }
}
