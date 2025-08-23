pipeline {
  agent any
  environment {
    IMAGE_NAME = "test-local-image"
    IMAGE_TAG = "latest"
  }
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/wonil-infra/test.git', branch: 'main'
      }
    }
    stage('Docker Build') {
      steps {
        sh '''
          echo "== Docker build =="
          docker build -t $IMAGE_NAME:$IMAGE_TAG .
          docker images | grep $IMAGE_NAME
        '''
      }
    }
  }
}
