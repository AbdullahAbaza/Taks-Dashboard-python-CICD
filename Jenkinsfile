pipeline {
    agent any
    environment {

        DOCKER_IMAGE = "abdullahabaza/task-manager"
        //VERSION = "${env.BUILD_NUMBER}"
	    ARGOCD_SERVER = 'localhost:8082'
        ARGOCD_USER = 'admin'
        ARGOCD_PASSWORD = 'Q2feDsWxNgHZvZeQ'
        ARGOCD_APP_NAME = 'task-manager-cicd'
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/AbdullahAbaza/Taks-Dashboard-python-CICD.git'
            }
        }

        stage('Dockerize') {
            steps {
                sh 'docker compose build'
            }
        }
        stage('Push to dockerhub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub_cred', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                    sh 'docker push ${DOCKER_IMAGE}:latest'
                    sh 'docker logout'

                }
            }
            
        }

       /* stage('Update Kubernetes Deployment') {
            steps {
                script {
                    // Set the new image in the Kubernetes manifests
                    sh """
                    kubectl set image deployment/task-manager app=$DOCKER_IMAGE:latest
                    kubectl rollout restart deployment/task-manager
                    """
                }
            }
        }*/

        stage('Sync with ArgoCD') {
            steps {
                script {
                    // Trigger ArgoCD to sync the application
                    sh """
                    argocd login $ARGOCD_SERVER --username $ARGOCD_USER --password $ARGOCD_PASSWORD --insecure
                    argocd app sync $ARGOCD_APP_NAME
                    """
                }
            }
        }

   }
}
