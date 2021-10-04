# Required Settings 
### Create file: /etc/django-conf-files/vumatel_installations.json

The json file needs to contain the following parameters:
- DEBUG: <true/False> (Determines Prod/Dev)
- SECRET_KEY: django-secret-key

These parameters are needed by the django.conf.settings file

#Required libraries
### Create a virtual environment to isolate our package dependencies locally
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

###Install required libraries
pip install -r requirements