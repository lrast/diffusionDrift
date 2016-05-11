
# My notes

## Installation

Requirements: python, pip, virtualenv  

1. git clone
2. Make and activate the virtualenv. bashaliases aliases activate to the current directory:
    + $ source bashaliases
    + $ activate
3. pip install -r requirements.txt  




### Running 
####Local:  

#####Any of the following work (with foreman installed):  
foreman start web  
foreman start  
./citeMapper.py  

####Heroku:  
heroku ps:scale web=1  
heroku open  





# Heroku's Guide 

## python-getting-started

A barebones Python app, which can easily be deployed to Heroku.

This application support the [Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) article - check it out.

### Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/).

```sh
$ git clone git@github.com:heroku/python-getting-started.git
$ cd python-getting-started
$ pip install -r requirements.txt
$ python manage.py migrate
$ foreman start web
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

### Deploying to Heroku

```sh
$ heroku create
$ git push heroku master
$ heroku run python manage.py migrate
$ heroku open
```

### Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)



