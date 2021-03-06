# shorty

A url shortener for and on kubernetes. Please use a nginx for https/tls for the same.
## Pre requisites
- Following environment variables should be set before you start the app/server.
    - SHORTY_PG_HOST
    - SHORTY_PG_PORT
    - SHORTY_PG_USERNAME
    - SHORTY_PG_PASSWORD
    - SHORTY_PG_DB
    - DJANGO_SECRET_KEY
## Running docker image [working]
If you are running a docker image then pass an env file `--env-file`
https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file
#### windows
`docker rm shorty -f &&  docker build -t gajuambi/shorty:latest -f .\Deployment\Dockerfile . && docker run --name shorty -it --env-file .env -p 80:8000 gajuambi/shorty`

#### linux
`docker rm shorty -f && docker build -t gajuambi/shorty:latest -f ./Deployment/Dockerfile . && docker run --name shorty -it --env-file .env -p 80:8000 gajuambi/shorty`


## Docker-compose [working]
`cd Deployment`
`doker-compose up`

## k8s/helm [needs testing]
- Get into the directory shorty/Deployment/k8s/helm
- Replace the values to be set from the following helm command `helm install shorty shorty --set "SHORTY_PG_DB=dbname,SHORTY_PG_USERNAME=dbuser,SHORTY_PG_PASSWORD=dbpassword,SHORTY_PG_HOST=dbhost,SHORTY_PG_PORT=5432,DJANGO_SECRET_KEY=djangosecretkey"`


