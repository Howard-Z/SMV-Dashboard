Receives MQTT data from SMV on-board DAQ and stores it to a database.
INSTALLATION:
- site is in development.
- pip install -r requirements.txt
- python manage.py runserver
TO USE:
- set topics in list format, views.py line 8

/smv/

Things to Consider: the sqlite file is the entire db, should we really be commiting this to gh?
