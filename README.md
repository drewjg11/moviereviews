# README #

This README would normally document whatever steps are necessary to get your application up and running.

## What is this repository for? ##

Django project template for Full Stack N-Site.

## How do I get set up? ##

1. Install [docker](https://docs.docker.com/get-docker/) by following the steps in the link provided.
1. Install [python3](https://www.python.org/downloads/) by following the steps in the link provided.
1. Clone the repository to your computer.
    ```shell script
    git clone [TODO: REPLACE WITH REPO URL] /local/project/path
    ``` 
1. Go to the project directory and change the branch to `development`
    cd /local/project/path
    git checkout development
    git pull
    ``` 
1. Run the following command to set up your new environment.
    ```shell script
    make touch-pristine-project
    ```
1. Run the following command.
    ```shell script
    make docker-upb
    ```
   *After initial run, you should only need to run `make docker-up`. The `make docker-upb` is only necessary when 
   needing to rebuild containers, for example if you update pip requirements.*
1. You should now be able to interact with the application by visiting [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Makefile ##

**Commands prefixed with `devops-` should not be modified or changed in any way 
as they are used specifically for deployment purposes.**

Helpful commands have been added to the Makefile within this project.
Feel free to add any command which makes development easier for you.

### Common recipes ###

#### Seeding local database ####
 ```shell script
make django-database-seed
```

