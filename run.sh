#!/bin/sh
docker run -v $(pwd)/workspace:/workspace -i -t --network host --entrypoint /bin/bash debian-msf-local:latest
