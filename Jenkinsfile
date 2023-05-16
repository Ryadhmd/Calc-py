node {
    checkout scm

    def customImage = docker.build("calc-py:${env.BUILD_ID}")

    customImage.inside {
        sh 'pytest'
    }
    docker.withRegistry('', 'Dockerhub'){
        customImage.push()
    }

}