pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'github-gist-api'
    }

    stages {
        stage('Clone Repository') {
            steps {
                sh ''' 
                git pull 'https://${github}@github.com/ayush2882/equal-experts.git'
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'python -m unittest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Push Docker Image to Local Registry') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").push()
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                kubernetesDeploy(kubeconfigId: 'minikube-kubeconfig', configs: 'k8s-manifests')
            }
        }
    }
}
