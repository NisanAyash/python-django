## Python Basics:
```.py
a = 'hello'
a.upper() # 'HELLO'
a = True
a = None
stringify = str(5) # '5'
a = hello 
string_concat = f"{a} lorem ipsum" # hello lorem ipsum

```

```.py
a = 1 
if a > 0:
   print("greater")
elif (a < 0): 
  print("error")
else:
   print("less than")
```

```py
def add(x,y):
  return x + y
```


```py
a = "python"
a[0] # p 
a[2]  # t
a[0] + a[2] // pt

tup = (1,2,3)
len(tup) # 3

list = [3,2,1]
ls # [3,2,1]
ls.append(4) # [3,2,1,4]
ls.sort() # [1,2,3,4]

set = {1,2,3,4} 
set.add(4) # {1,2,3,4} 
3 in set # TRUE 

dict = {1:'one', 2:'two'}
dict[1] # one
```

```py
for i in dict:
  print(i) # 1, 2

# list of tuples
for i in dict.items():
  print(i) # 1, 2

for i in range(10): 
  print(i)  # 0,1,2,3,4,5,6,7,8,9

colors = ["blue", "red"]
for color in colors: 
  print(color) # blue. red
```
```py
  class Dog():
    def __init__(self, name): # constructor
       self.name = name

dogInstance = Dog("jhon") 
print(dogInstance.name) # jhon

class Doodle(Dog):
    def __init__(self, name, curly):
      super().__init__(name)
      self.curly = curly

doodleInstance = Dog("jhon", True)
print(doodleInstance.name) # jhon
print(doodleInstance.curly) # True
```

# Django
## Setup: 
```
cd project
pipenv install django
django-admin # all admin commands (create project etc etc...)
django-admin startproject homework . # start django project
python manage.py runserver __port__  # port is optional paramater

# update in the settings the interpreter path (ctrl + shift + p then "select interpreter" 
pipenv --venv # get the path of venv environment 

# Install packages (!required)
python manage.py startapp playground
python manage.py startapp store
python manage.py startapp tags
python manage.py startapp anyapp
```

## Mapping urls 

```py
# Mapping urls to functions

## go to views file and create api-end point 
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(req): 
    return HttpResponse('Hello world!')


def say_goodbye(req): 
    x = 1
    y = 2
    return HttpResponse('Goodbye')


## create urls file in playground direction

from django.urls import path
from . import views

# Url config
urlpatterns = [
    path('hello/', views.say_hello),
    path('bye/', views.say_goodbye)
]

## go to urls file into ur project and add the playground to urls like the example below

from django.contrib import admin
from django.urls import path, include


# playground/hello
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls'))
]
```

## Model
```py
## go to models file and add models..

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateTimeField(null=True)
```

```
# install pydot
pip install pydot
pythob manage.py gtaph_models --pytid core -o a.png
```

