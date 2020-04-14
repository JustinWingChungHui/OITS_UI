# OITS_UI

## Requirements
 - Python3
 - Pip (for python 3)
 - VirtualenvWrapper

## Installation
Clone the repository, and change directory into the cloned repository.

Create a virtual env using python 3

```bash
mkvirtualenv OITS_UI --python=/usr/bin/python3.6
```

Install the Python requirements from the `requirements.txt`
```bash
pip install -r requirements.txt
```

Copy `OITS_UI\config.py-example` to `OITS_UI\config.py`
And edit `OITS_UI\config.py` to suit your own server settings

Create the database
```bash
python manage.py migrate
```

Run the web app
```bash
python manage.py runserver
```


Run the OITS runner in a spearate thread
```bash
python manage.py oits_runner
```
