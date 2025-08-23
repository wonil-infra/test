pipeline {
  agent any
  environment {
    IMAGE_NAME = "test-local-image"
    IMAGE_TAG = "latest"
    CONTAINER_NAME = "test-flask-container"
    EXTERNAL_PORT = "5001"
    INTERNAL_PORT = "5000"
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
          docker run -d --name $CONTAINER_NAME -p $EXTERNAL_PORT:$INTERNAL_PORT $IMAGE_NAME:$IMAGE_TAG
        '''
      }
    }
    stage('Check Health') {
      steps {
        sh '''
          echo "== Curl check =="
          sleep 3
          curl -f http://localhost:$EXTERNAL_PORT || echo "Flask not responding"
        '''
      }
    }
    stage('Print Container Logs') {
      steps {
        sh '''
          echo "== Container logs =="
          docker logs $CONTAINER_NAME || true
        '''
      }
    }
  }
}
