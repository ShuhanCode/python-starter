# 47. First Django Application (App)

<details>
  <summary> Slides: 47. First Django Application (App) </summary>

<p align="center" >
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/47_First-Django-Application-App_17.png" width="90%" > 
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

- mapping the view to the url in the `my_site/urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from my_app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('my_app/', include('my_app.urls')), # new  
    path('admin/', admin.site.urls),
]
```

-  add the `my_app` to the `my_site/settings.py`

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
      'my_app'
  ]

  ...

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

</details>

<details>
  <summary> Codebase: </summary>

-   [my_site](../../codebase/django-4/08-Introduction-to-Django/my_site/)


</details>


#  Resources for this lecture


-   [Slides: 06-Intro-to-Django-Framework.pdf](https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/resources/06-Intro-to-Django-Framework.pdf)


---

[Previous](./46_First-Django-Project.md) | [Next]()