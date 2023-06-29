# CRUD-Web-App
How to run app in Linux.
## How to clone repository
```
$ mkdir CRUD-Web-App
$ cd CRUD-Web-App
$ git clone https://github.com/JakubKosakowski/CRUD-Web-App.git .
```

## How to create virtual environments
```
$ python -m venv env(when you're in CRUD-Web-App directory)
$ source evn/bin/activate
$ pip install -r requirements.txt
```

## How to run app
```
$ python app.py (or from interpreter)
```
or
```
$ export FLASK_APP=app.py
$ export FLASK_DEBUG=1
$ flask run
```
