# 120. Django Level One - Part Five - Challenge Solutions

<details>
  <summary> Create: django application </summary>

- run the following command to start the server

```
python3 -m venv my_env
```

```
source my_env/bin/activate
```

-  create a project

```bash
django-admin startproject new_ProTwo
```  

-  create a django application

```
cd new_ProTwo
```

```bash
python manage.py startapp new_appTwo
```

-  create a view in the `new_appTwo/views.py`

```python

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project</em>")
```

- mapping the view to the url in the `new_ProTwo/urls.py`

```python
from django.contrib import admin
from django.urls import path
from new_appTwo import views

urlpatterns = [
    path('', views.index, name="index"),  
    path('admin/', admin.site.urls),
]
```

-  add the `new_appTwo` to the `new_ProTwo/settings.py`

```python

...

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'new_appTwo'
]

...

```

</details>


<details>
  <summary> Result: webpages capture </summary>

- run the following command to start the server

```
python3 -m venv my_env
```

```
source my_env/bin/activate
```

```
python3 manage.py runserver
```
<p align="center" >
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/120_Django-Level-One-Part-Five-Challenge-Solutions.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/120_Django-Level-One-Part-Five-Challenge-Solutions_2.png" width="90%" > 

</p> 

</details>

<details>
  <summary> Codebase: </summary>

-   [Codebase: new_ProTwo](../../codebase/python-django/Django_Level_One/new_ProTwo/)

</details>

##  Resources for this lecture


-   [Slides: Django Level One.pdf](https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/Resources/Django+Level+One.pdf)

-   [How To Install the Django Web Framework on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-20-04)


---

[Previous](./119_Django-Level-One-Part-Four-Challenge-Task.md) | [Next](./121_Django-Level-One-Part-Six-Views.md)