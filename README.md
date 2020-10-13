# django-blog-with-forum
The project persists two goals: firstly, this is an example how to build simple web applications, such as blog or forum, using [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/), and secondly, how to combine Django and [Docker](https://www.docker.com/) in web development.

The project of website contains Django back-end, Postgres database and uses Uikit front-end framework in templates.</br>


## How to use this project?
 1) Create a folder for project:
```
$ mkdir project && cd project
```
2) Clone git repository in created folder:
```
$ git clone https://github.com/ivanlohvyn/django-blog-with-forum.git
```
3) Update the environment variables in the docker-compose.yml and .env.dev files for your needs.

4) Build the images:

```
docker-compose build
```
5) Run the containers:
```
docker-compose up
```



### Notes
The project is still in development, so in the future he will be contain update and delete options to blog posts (to complete CRUD functionality), and code will be refactored according DRY principle also. Everyone welcome with ideas how to improve this project)
