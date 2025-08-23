pipeline {
  agent any
  environment {
    IMAGE_NAME = "test-local-image"
    IMAGE_TAG = "latest"
    CONTAINER_NAME = "test-flask-container"
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
    stage('Cleanup Old Container') {
      steps {
        sh '''
          echo "== Stop & Remove old container (if exists) =="
          docker stop $CONTAINER_NAME || true
          docker rm $CONTAINER_NAME || true
        '''
      }
    }
    stage('Run New Container') {
      steps {
        sh '''
          echo "== Run new container =="
          docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME:$IMAGE_TAG
          docker ps | grep $CONTAINER_NAME
        '''
      }
    }
  }
}
