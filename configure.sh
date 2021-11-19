sudo apt-get install python3-venv
python3 -m venv venv
. /venv/bin/activate
pip3 install -r requirements-dev.txt
python3 manage.py runserver 0.0.0.0:8000

