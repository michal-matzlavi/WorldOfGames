pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        bat 'docker image build . -t worldofgames_web'
      }
    }
    stage('Run') {
      steps {
        bat 'docker-compose up -d'
      }
    }
    stage('Test') {
      steps {
        bat 'python ./tests/e2e.py'
      }
    }
    stage('Finalize') {
      steps {
        bat 'docker-compose down'
      }
    }
  }
}