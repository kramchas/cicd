pipeline {
  agent any

  stages {

    stage ('Build') {
      steps {
        sh 'docker build -t jenkins .'
        sh 'docker tag jenkins kramchas/fastapi:latest'
      }
    }

    stage ('Push'){
      steps{
        sh 'docker push kramchas/fastapi:latest'
      }
    }

    stage ('deploy'){
      steps{
        //ssh -o StrictHostKeyChecking=no vagrant@192.168.56.10
        sh 'docker run -d --name jenkins -p 8000:8000 kramchas/fastapi:latest'
      }
    }
  }
}

