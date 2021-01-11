# shorty

A url shortener for and on kubernetes
## Pre requisites
- Following environment variables should be set before you start the app/server.
    - SHORTY_PG_HOST
    - SHORTY_PG_PORT
    - SHORTY_PG_USERNAME
    - SHORTY_PG_PASSWORD
    - SHORTY_PG_DB
    - DJANGO_SECRET_KEY
## Running docker image
If you are running a docker image then pass an env file `--env-file`
https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file
`docker rm shorty -f &&  docker build -t gajuambi/shorty -f .\Deployment\Dockerfile . && docker run --name shorty -it --env-file .env -p 8000:8000 gajuambi/shorty`

## Docker-compose [working]
`cd Deployment`
`doker-compose up`


