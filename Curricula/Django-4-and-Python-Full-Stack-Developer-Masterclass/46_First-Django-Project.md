# 46. First Django Project

<details>
  <summary> Slides: 46. First Django Project </summary>

<p align="center" >
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_2.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_3.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_4.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_5.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_6.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_7.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_8.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_9.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_10.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_11.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_12.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_13.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_14.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_15.png" width="90%" > 
    <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_16.png" width="90%" >    

</p> 

</details>

<details>
  <summary> Install: Requirements </summary>

## Based on the Pip

1.  install python3-pip python3-venv

```bash
sudo apt install python3-pip python3-venv
```

2.   install Django 2.2.8
    
```bash 
pip3 install Django==2.2.8
```

3. install django rest framework 3.10.0

```bash
pip3 install djangorestframework==3.10 pyrogram aiohttp requests
```

## Based on the Conda

1. set up conda on linux

  ```bash
  export PATH="/home/rfnoc/anaconda3/bin:$PATH"
  ```

</details>

<details>
  <summary> Create: first project </summary>

- run the following command to start the server

```
python3 -m venv my_env
```

```
source my_env/bin/activate
```

-  create a project

```bash
django-admin startproject my_site
```

</details>


<details>
  <summary> Result: webpages capture </summary>

- run the following command to start the server

```bash
python3 manage.py runserver
```

<p align="center" >    
     <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_17.png" width="90%" > 
     <img src="https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/images/46_First-Django-Project_18.png" width="90%" > 
    
</p> 

</details>

<details>
  <summary> Codebase: </summary>

-   [my_site](../../codebase/django-4/08-Introduction-to-Django/my_site/)

</details>

#  Resources for this lecture


-   [Slides: 06-Intro-to-Django-Framework.pdf](https://python-ds.s3.us-west-1.amazonaws.com/Django-4-and-Python-Full-Stack-Developer-Masterclass/resources/06-Intro-to-Django-Framework.pdf)

-   [How To Install the Django Web Framework on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-20-04)



---

[Previous](./45_How-Django-Works.md) | [Next](./47_First-Django-Application-App.md)