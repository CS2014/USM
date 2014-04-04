USM
===

Running a locally (This app runs similarly to all other Django apps):
1. Setup Python virtualenv
2. Install "local_requirements.txt" via pip
3. Django syncdb & migrate
4. run "python usm/manage.py runserver"

Heroku Running / Setup
==
This app is already prepared for a heroku deployment:
1. Add PostgreSQL database to the heroku app.
2. Ensure "DATABASE_URL" configuration is set.
3. git push
4. You're good to go!
