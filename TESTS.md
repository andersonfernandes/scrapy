# Info about test generation

Run the following to start the docker container:

- `docker compose build`
- `docker compose run --rm app bash`

Inside the container run:
- `pynguin --project-path ./<FOLDER> --output-path ./pynguin_tests/<FOLDER> --module-name <MODULE>`
