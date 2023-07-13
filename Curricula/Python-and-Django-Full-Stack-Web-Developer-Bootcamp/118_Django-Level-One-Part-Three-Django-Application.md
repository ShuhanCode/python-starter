# 118. Django Level One - Part Three - Django Application

<details>
  <summary> Slides: 118. Django Level One - Part Three - Django Application </summary>

<p align="center" >
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_2.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_3.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_4.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_5.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_6.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_7.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_8.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_9.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_10.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_11.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_12.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_13.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_14.png" width="90%" > 

</p> 

</details>

<details>
  <summary> Create: first django application </summary>

-  create a django application

```bash
python manage.py startapp new_app
```

-  add the new app to the `new_project/settings.py`

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
    'new_app'
]

...

```

-  create a view in the `new_app/views.py`

```python

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

```

- mapping the view to the url in the `new_project/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from new_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('new_app/', include('new_app.urls')),
    path('admin/', admin.site.urls),
]
```

</details>


<details>
  <summary> Result: webpages capture </summary>

- run the following command to start the server

```bash
sudo apt install python3-pip python3-venv
```

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
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/images/118_Django-Level-One-Part-Three-Django-Application_15.png" width="90%" > 

</p> 

</details>

<details>
  <summary> Codebase: </summary>

-   [Codebase: first_project](../../codebase/python-django/Django_Level_One/first_project/)

</details>

#  Resources for this lecture


-   [Slides: Django Level One.pdf](https://python-ds.s3.us-west-1.amazonaws.com/Python-and-Django-Full-Stack-Web-Developer-Bootcamp/Resources/Django+Level+One.pdf)

-   [How To Install the Django Web Framework on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-20-04)


---

[Previous](./117_Django-Level-One-Part-Two-Django-Project.md) | [Next](./119_Django-Level-One-Part-Four-Challenge-Task.md)