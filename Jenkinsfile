node {
    checkout scm

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    def customImage = docker.build("calc-py:${env.BUILD_ID}")

    customImage.inside {
        sh 'pytest'
    }

  
    customImage.push()
    

}