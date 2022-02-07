#!/bin/bash
TAG=ghcr.io/digitalcityscience/space-syntax
COMMAND="docker run --network=host --detach --rm -v "${PWD}"/workdir:/home/app/downloads ${TAG}"

while IFS= read -r line; do
  echo "Downloading: $line"
  $COMMAND $line &
done < "$1"

echo "All triggered"