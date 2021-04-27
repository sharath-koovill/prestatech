Dependencies:
$ pip install python
$ pip instal django
$ pip install djangorestframework
$ pip install djangorestframework-jsonapi
$ pip install django-filter
$ pip install sqlalchemy

First Step:
The algorithm is placed under princessapi->shortestpath.py->process(grid, grid_size)

Second Step:
API:
http://127.0.0.1:8000/mario/api/get_shortest_path?grid=-----,p-x--,-----,x---m,----x&grid_size=5
response:
[{"error_flag": "FALSE", "paths": "[('UP', 'LEFT', 'LEFT', 'LEFT', 'UP', 'LEFT')]"}]

The database being used is sqlite db and orm is SQLAlchemy.

Third Step:
I have used Django to have an interactive simple page.
Web:
http://127.0.0.1:8000/mario/

Project Name: Mario
Api App: princessapi
Web app: princess

Test:
python manage.py test