# String Related Python Feature
## String Concatenation
String concatenation refers to the process of combining multiple strings into a single string. In programming, it is a common operation used to build larger strings by joining smaller strings together.


```python
#String concatentation
print("Hello" + " " + "World")
```
## Formatted strings
Formatted strings, also known as f-strings or formatted string literals, are a feature in several programming languages that allow you to embed expressions within string literals. This feature provides a concise and convenient way to create strings that incorporate variable values or expressions.
```python
#Formatted Strings
name = "John"
age = 30
print(f"Hello, {name}. You are {age}.")
print("Hello, {}. You are {}.".format(name, age))
print("Hello, " + name + ". You are " + str(age) + ".")
print("Hello, %s. You are %d." % (name, age))
```

## String Indexing and Slicing
String indexing and slicing are operations used to access specific characters or subsequences within a string.
```python
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
```
## String Methods
1. *string.upper()*: This method returns a new string where all the characters are converted to uppercase. In your example, it would return "HELLO WORLD".

2. *string.lower()*: This method returns a new string where all the characters are converted to lowercase. In your example, it would return "hello world".

3. *string.capitalize()*: This method returns a new string where the first character is capitalized and all other characters are converted to lowercase. In your example, it would return "Hello world".

4. *string.swapcase()*: This method returns a new string where the case of each character is swapped. Uppercase characters become lowercase, and lowercase characters become uppercase. In your example, it would return "hELLO wORLD".

5. *string.replace("Hello", "Goodbye")*: This method returns a new string where all occurrences of the first argument (in this case, "Hello") are replaced with the second argument (in this case, "Goodbye"). In your example, it would return "Goodbye World".

6. *string.count("l")*: This method returns the number of non-overlapping occurrences of the specified substring (in this case, "l") within the string. In your example, it would return 3, as there are three 'l' characters in the string.

7. *string.find("World")*: This method returns the index of the first occurrence of the specified substring (in this case, "World") within the string. If the substring is not found, it returns -1. In your example, it would return 6, as "World" starts at index 6.

8. *string.split(" ")*: This method splits the string into a list of substrings based on the specified delimiter (in this case, a space " "). In your example, it would return ['Hello', 'World'], where the string is split into two substrings.

9. *string.strip()*: This method returns a new string with leading and trailing whitespace characters removed. In your example, since there are no leading or trailing spaces, it would return "Hello World" as is.

10. *string.lstrip()*: This method returns a new string with leading (left) whitespace characters removed. In your example, since there are no leading spaces, it would return "Hello World" as is.

11. *string.rstrip()*: This method returns a new string with trailing (right) whitespace characters removed. In your example, since there are no trailing spaces, it would return "Hello World" as is.

12. *string.startswith("Hello")*: This method checks if the string starts with the specified substring (in this case, "Hello"). It returns True if the string starts with the substring; otherwise, it returns False. In your example, it would return True.

13. *string.endswith("World")*: This method checks if the string ends with the specified substring (in this case, "World"). It returns True if the string ends with the substring; otherwise, it returns False. In your example, it would return True.

```python
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
```
## List and its methods
1. *list.append(element)*: This method appends the specified element to the end of the list. It modifies the original list by adding the element. The append() method always returns None. In your example, it adds 11 to the list.

2. *list.pop()*: This method removes and returns the last element from the list. If you don't provide an index, it removes the last element by default. In your example, it removes 11 from the list and returns it. After that, the modified list contains elements from 1 to 10.

3. *list.pop(element)*: This method removes and returns the element at the specified index (in this case, 0) from the list. Removing an element from the beginning of the list can be less efficient as it requires shifting all the other elements. In your example, it removes 1 from the list and returns it.

4. *list.remove(element)*: This method removes the first occurrence of the specified element (in this case, 10) from the list. If the element is not found, it raises a ValueError. The remove() method modifies the original list but doesn't return anything. In your example, it removes 10 from the list.

5. *list.reverse()*: This method reverses the order of elements in the list. It modifies the original list in-place, meaning it doesn't create a new list but changes the order of elements within the existing list. The reverse() method returns None. In your example, it reverses the elements in the list.

6. *list.sort()*: This method sorts the elements of the list in ascending order. It modifies the original list in-place. If the elements are of different types, it may raise a TypeError. The sort() method returns None. In your example, it sorts the elements in the list in ascending order.
```python
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
```