node {
    checkout scm

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    def customImage = docker.build("calc-py:${env.BUILD_ID}")

    customImage.inside {
        sh 'pytest'
    }

    docker.withRegistry('https://dockerhub.com', 'Docker Hub Creds) {
            customImage.push()
            customImage.push('latest')
    }

}