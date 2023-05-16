node {
    checkout scm

    def customImage = docker.build("ryadhamdini/calc-py:${env.BUILD_ID}")

    customImage.inside {
        sh 'pytest'
    }
    docker.withRegistry('https://index.docker.io/v1/', 'bed905e0-659f-409e-afbb-c9efbc78ac20'){
        customImage.push()
    }
}