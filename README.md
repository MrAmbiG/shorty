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
## Running docker image [currently not working]
If you are running a docker image then pass a env file `--env-file`
https://docs.docker.com/engine/reference/commandline/run/#set-environment-variables--e---env---env-file
`docker run --name shorty -it --env-file .env  gajuambi/shorty -p 8001:8001`

## Docker-compose [working]
`cd Deployment`
`doker-compose up`
