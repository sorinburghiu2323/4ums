# SoftwareDev
ECM2434 Group D Project

## Setup

First set up you python virtual environment.

`python -m venv .venv`

and activate it

`.venv\Scripts\activate.bat` or `.venv/bin/activate`

Then install python dependencies:
```
pip install -r requirements-nondeploy.txt
```

Do your migrations (create your development database):
```
python manage.py migrate
```

Run the django server using:
```
python manage.py runserver
```

### Next install the VueJS frontend dependencies:


```shell script
cd frontend
npm install
```
Note: When you pull changes that others have made, you may want to do `npm install` again to ensure any additional dependencies have been added.

Now to build the frontend, there are two ways:

Watches for any changes in the filetree and recompiles when detects a change
```
npm run watch
```

Compiles and minifies for production
```
npm run build
```

## Need some test data?

Run the bootstrap to autogenerate some dummy data using:
```
python manage.py bootstrap
```
Note: Do this after migrating for the first time.

## Before your push...

Make sure you apply black to the root of the project using:
```
black .
```

## Having a migration error?

This may be due to a database update. Simply drop you current database and create a new one as follows:
1. Delete `db.sqlite3` file
2. Run `python manage.py migrate`
