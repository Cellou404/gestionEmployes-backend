# gestionEmployes-backend

# Introduction

The goal of this project is to provide a fully fonctionnal api that will be used in a __front-end__ framework

This project is written with django4 and python 3+.

![A screenshot](media/screenshot/project_screeshot1.png?raw=true "Title")

## Main features

* accounts app with custom user model

* User registration and logging

* employees app

* projects app

* tasks app

* Single requirements files

* PostgresSql database

# Usage

To use this project server side:
      
### No virtualenv ?

Make sure that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

Create virtualenv:

      $ python3 -m venv venv
      
      Name your virtualenv as you wish. venv, env, etc


If you don't have django installed for python 3 then run:

    $ pip3 install django
    
Install dependancies:

    $ pip install -r requirements.txt
    
 Run migrations:
 
    $ python manage.py makemigrations
    $ python manage.py migrate
    
Create a superuser:

    $ python manage.py createsuperuser
    
    follow instructions
    
And then test the project:

    $ python manage.py runserver 
