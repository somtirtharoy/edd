#!/bin/bash -xe

# $1 = image tag generated by Jenkins
TAG="${1}"

# build the core image
DOCKER_BUILDKIT=1 docker build \
    --progress plain \
    --build-arg "EDD_VERSION=${TAG}" \
    --build-arg "NODE_VERSION=${TAG}" \
    -f ./docker/edd/core/Dockerfile \
    -t "jbei/edd-core:${TAG}" \
    .
