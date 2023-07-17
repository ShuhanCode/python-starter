# 47. First Django Application (App)

<details>
  <summary> Slides: 47. First Django Application (App) </summary>

<p align="center" >
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_2.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_3.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_4.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_5.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_6.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_7.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_8.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_9.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_10.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_11.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_12.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_13.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_14.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_15.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_16.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_17.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_18.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_19.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_20.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_21.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_22.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_23.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_24.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_25.png" width="90%" > 

</p> 

</details>

<details>
  <summary> Create: first django application </summary>

-  create a django application

```bash
python manage.py startapp my_app
```

-  create a view in the `my_app/views.py`

```python

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("HELLO THIS IS A VIEW INSIDE MY_APP")
```

- add the `urls.py` file under `my_app`:  `my_app/url.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # /my_app --> PROJECT my_app/urls.py
]
```

- mapping the view to the url in the PROJECT `urls.py` -- `my_site/urls.py`

```python
"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_app import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('my_app/', include('my_app.urls')), # /my_app --> my_app/urls.py 
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
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_000.png" width="90%" >     

</p> 

**Note:** error casued by `path('my_app/', include('my_app.urls'))` in the `my_site/urls.py`, need add the `urls.py` file under `my_app`:  `my_app/url.py`

- add the `urls.py` file under `my_app`:  `my_app/url.py`

  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```

- then, run the following command to start the server again

```
python3 manage.py runserver
```

<p align="center" >
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_001.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_002.png" width="90%" > 

</p> 

## Exploring urls path

-  `my_site/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from my_app import views

urlpatterns = [
    # path('', views.index, name="index"), # NOTE: comment out this line
    path('my_app/', include('my_app.urls')),  
    path('admin/', admin.site.urls),
]
```

```
python3 manage.py runserver
```

<p align="center" >
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_003.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_004.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_005.png" width="90%" > 

</p> 

</details>

<details>
  <summary> Codebase: </summary>

-   [my_site](../../codebase/django-4/08-Introduction-to-Django/my_site/)


</details>


#  Resources for this lecture


-   [Slides: 06-Intro-to-Django-Framework.pdf](https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/resources/06-Intro-to-Django-Framework.pdf)


---

[Previous](./46_First-Django-Project.md) | [Next](./48_Introduction-to-URLs-Views-and-Routing.md)