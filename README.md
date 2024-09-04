init dev environment, create a virtual environment to manage dependencies 
and then activate it

```bash
python -m venv venv
source venv/bin/activate
```

now install django on the venv

```bash
python -m pip install Django
```

and start the project

```bash
django-admin startproject potatoblog .
python manage.py runserver
```

add app

```bash
python manage.py startapp blog
```

and register it

```bash
python manage.py makemigrations blog
python manage.py migrate blog
python manage.py migrate 
```

create admin 

```bash
python manage.py createsuperuser
```

