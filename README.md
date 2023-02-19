# Job Lab  #
This repo contains the code for JobLab Repo 

## Branches
* There is  branch `main` public facing
* Feature branches will be used by developers to work on a new feature or bug fixes by taking a fresh branch from `main`


## Contributing

#### Technology Stack
* Python 3.9+ - [Official Download Link](https://www.python.org/downloads/)
* Django 4.0.2 - [Official Link](https://www.djangoproject.com/)
* Postgres -


#### Development Setup
##### Git & Clone Code
Write this command in the directory where you want to place the project 

```bash
git clone https://github.com/B0bby-Singh/JobLab.git
```

##### Virtual Environment
Create and activate virtual environment and then install the requirements. 
```bash

python3 -m venv .venv                    # First time
#windows
. ./.venv/Scripts/activate                # In every new terminal window
pip install -r requirements/base.txt          # First time, and if new package is added
```

##### Database 
```bash
# MacOS based settings
# mysql  -> write into your terminal to write commands ->Login into DB user
                                     # List of existing database
create database joblab;; # Confirm new database 
# The user according .envs/.sample.env
create user joblab_user with encrypted password 'joblab1234'
grant all preivilges on database joblab to joblab_user;

```

##### Database Migrations
For development environment setup,

```bash
python manage.py makemigrations
python manage.py migrate
```

#### INSERT SAMPLE DATA
```bash
# RUN THE FOLLOWINGS COMMANDS IN YOUR TERMINAL

python manage.py jobsdump
```

##### Run Application
```bash
python manage.py runserver

```

Access Website at: [localhost:8000](localhost:8000)


