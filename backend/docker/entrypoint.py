#!/usr/bin/env python

from subprocess import call

# call migrate, and load initial data before we runserver
call(["python3", "manage.py", "migrate"])
call(["python3", "manage.py", "loaddata", "initial_data.json"])
call(["python3", "manage.py", "runserver", "0.0.0.0:8000"])
