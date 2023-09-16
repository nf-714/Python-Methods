print("Hello World")
#String concatentation
print("Hello" + " " + "World")
#String multiplication
print("Hello" * 3)
#String indexing
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])
#String slicing
print("Hello"[0:3])
print("Hello"[1:4]) 
print("Hello"[2:5])

#Formatted Strings
name = "John"
age = 30
print(f"Hello, {name}. You are {age}.")
print("Hello, {}. You are {}.".format(name, age))
print("Hello, " + name + ". You are " + str(age) + ".")
print("Hello, %s. You are %d." % (name, age))
#Formatted String


#String Methods
string = "Hello World"
print(string.upper()) #HELLO WORLD
print(string.lower()) #hello world
print(string.capitalize()) #Hello world
print(string.swapcase()) #hELLO wORLD -
print(string.replace("Hello", "Goodbye")) #Goodbye World
print(string.count("l")) #3
print(string.find("World")) #6
print(string.split(" ")) #['Hello', 'World']
print(string.strip()) #Hello World
print(string.lstrip()) #Hello World
print(string.rstrip()) #Hello World
print(string.startswith("Hello")) #True
print(string.endswith("World")) #True
print("-------------String Methods Output-------------")
#String Methods

#List Methods
list = [1,2,3,4,5,6,7,8,9,10]
print("-------------List Methods Output-------------")
print(list.append(11)) #None O(1)
print(list) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(list.pop()) #11 O(1)
print(list) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list.pop(0)) #1 O(n)
print(list) #[2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list.remove(10)) #None
print(list) #[2, 3, 4, 5, 6, 7, 8, 9]
print(list.reverse()) #None
print(list) #[9, 8, 7, 6, 5, 4, 3, 2]
print(list.sort()) #None
print(list) #[2, 3, 4, 5, 6, 7, 8, 9]
print("-------------List Methods Output-------------")

#Dictionary Methods
dictionary = {"name": "John", "age": 30, "city": "New York"}
print("-------------Dictionary Methods Output-------------")
print(dictionary.get("name")) #John
print(dictionary.items()) #dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
print(dictionary.keys()) #dict_keys(['name', 'age', 'city'])
print(dictionary.pop("age")) #30
print(dictionary) #{'name': 'John', 'city': 'New York'}
print(dictionary.popitem()) #('city', 'New York')
print(dictionary) #{'name': 'John'}
print(dictionary.setdefault("name", "John")) #John
print(dictionary) #{'name': 'John'}
print(dictionary.update({"age": 30})) #None
print(dictionary) #{'name': 'John', 'age': 30}
print(dictionary.values()) #dict_values(['John', 30])
print("-------------Dictionary Methods Output-------------")

#Tuple Methods
tuple = (1,2,3,4,5,6,7,8,9,10)
print("-------------Tuple Methods Output-------------")
print(tuple.count(1)) #1
print(tuple.index(1)) #0
print("-------------Tuple Methods Output-------------")

#Set Methods
set = {1,2,3,4,5,6,7,8,9,10}
print("-------------Set Methods Output-------------")
print(set.add(11)) #None
print(set) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print(set.clear()) #None
print(set) #set()
print(set.copy()) #set()
print(set) #set()
print(set.add(1)) #None
print(set) #{1}
print(set.difference({1,2,3,4,5,6,7,8,9,10,11})) #set()
print(set) #{1}
print(set.difference_update({1,2,3,4,5,6,7,8,9,10,11})) #None
print(set) #set()
print(set.add(1)) #None
print(set) #{1}
print(set.discard(1)) #None
print(set) #set()
print(set.add(1)) #None
print(set) #{1}
print(set.intersection({1,2,3,4,5,6,7,8,9,10,11})) #{1}
print(set) #{1}
print(set.intersection_update({1,2,3,4,5,6,7,8,9,10,11})) #None
print(set) #{1}
print(set.isdisjoint({1,2,3,4,5,6,7,8,9,10,11})) #False
print(set.issubset({1,2,3,4,5,6,7,8,9,10,11})) #True
print(set.issuperset({1,2,3,4,5,6,7,8,9,10,11})) #False
print(set.pop()) #1
print(set) #set()
print(set.add(1)) #None
print(set) #{1}
print(set.remove(1)) #None
print(set) #set()
print(set.symmetric_difference({1,2,3,4,5,6,7,8,9,10,11})) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print(set) #set()
print(set.symmetric_difference_update({1,2,3,4,5,6,7,8,9,10,11})) #None
print(set) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print(set.union({1,2,3,4,5,6,7,8,9,10,11})) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print(set.update({1,2,3,4,5,6,7,8,9,10,11})) #None
print(set) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}    
print("-------------Set Methods Output-------------")

# Rules of args and kwargs
# 1. args must be first
# 2. kwargs must be last
# 3. args and kwargs can be used together

#args
def args(*args):
    print(args)

args(1,2,3,4,5,6,7,8,9,10)

#kwargs
def kwargs(**kwargs):
    print(kwargs)

kwargs(name="John", age=30, city="New York")

#args and kwargs
def args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

args_kwargs(1,2,3,4,5,6,7,8,9,10, name="John", age=30, city="New York")


#Closure
def outer_func():
    message = "Hi"
    def inner_func():
        print(message)
    return inner_func

my_func = outer_func()
my_func()

#OOP PY
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("John", "Smith", 50000)
print(emp_1.email)