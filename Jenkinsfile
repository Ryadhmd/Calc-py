node {
    checkout scm

    def customImage = docker.build("calc-py:${env.BUILD_ID}")

    customImage.inside {
        sh 'pytest'
    }
    docker.withRegistry('', 'bed905e0-659f-409e-afbb-c9efbc78ac20'){
        customImage.push()
    }

}