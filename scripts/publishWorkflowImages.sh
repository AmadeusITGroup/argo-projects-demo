#/bin/sh

DOCKER_REGISTRY=registry.127.0.0.1.nip.io:80
PROJECT=argo-projects

buildAndPublish() {
    echo "Building and publishing $1"
    docker build "workflow-resources/$1" -t  ${DOCKER_REGISTRY}/${PROJECT}/$1:latest
    docker push ${DOCKER_REGISTRY}/${PROJECT}/$1:latest
    docker rmi -f ${DOCKER_REGISTRY}/${PROJECT}/$1:latest
}

buildAndPublish "test-campaign"
buildAndPublish "git-promotion"