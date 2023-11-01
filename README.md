# movie-kaiseki

## How to Create Form
1. write models.py
2. write form to templates/{projectname}/index.html
3. write view
4. put command to create migration file
```
python manage.py makemigrations nice
```
5. put command to migrate
```
python manage.py migrate
```
6. sqlite3 install & check move
7. enjoy!

## How to Migration
1. write models.py
2. put command to create migration file(auto create migrations/0001_initial.py)
```
python manage.py makemigrations nice
```
3. put command to migrate(auto create to sqlite table from 0001_initial.py)
```
python manage.py migrate
```