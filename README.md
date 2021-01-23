# SoftwareDev
ECM2434 Group D Project

## Setup

First set up you python virtual environment.

`python -m venv .venv`

and activate it

`.venv\Scripts\activate.bat` or `.venv/bin/activate`

Then install python dependencies:

```
pip install -r requirements.txt
```

Do your migrations (create your development database):

```
python manage.py migrate
```

Next install the VueJS stuff:

Note: Hiba please edit this because I dunno how to set up the vue directories

```shell script
cd frontend\vue-frontend
npm install
```
