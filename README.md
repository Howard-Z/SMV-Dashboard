Receives MQTT data from SMV on-board DAQ and stores it to a database. \
INSTALLATION: 
- site is in development.
- pip install -r requirements.txt
- python manage.py runserver \
Site Paths: 
- /dashboard: dashboard
- /dashboard/map: map display, in progress
- /admin: admin console
- /static: static files, served via Apache
- /ws: websocket, served via daphne