#/bin/sh

docker build test-campaign/ -t  registry.127.0.0.1.nip.io:80/argoprojects/test-campaign:latest
docker push registry.127.0.0.1.nip.io:80/argoprojects/test-campaign:latest
docker rmi -f registry.127.0.0.1.nip.io:80/argoprojects/test-campaign:latest