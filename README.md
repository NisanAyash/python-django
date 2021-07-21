# Python Basics:
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
Setup: 
```
cd project
pipenv install django
django-admin # all admin commands (create project etc etc...)
django-admin startproject homework . # start django project
python manage.py runserver __port__  # port is optional paramater

# update in the settings the interpreter path (ctrl + shift + p then "select interpreter" 
pipenv --venv # get the path of venv environment 

python manage.py startapp playground

# create urls file on playground
```
