# print("Hello, Deepak Kumar!");
# message='Hello world, My name's Deepak Kumar'
# print(message);

# str="Hello, World!"
# str="Hello"
# print(str)
# full_name="rahul kumar"
# print(full_name)
# print(full_name.title())

# print(full_name.upper())

# first_name="rahul"
# last_name="kumar"
# last_name=last_name.upper()
# # full_name=f"{first_name} {last_name}"
# full_name=first_name.upper() + " " +last_name
# print(full_name)

# a=2
# b=3
# sum=a+b
# print("The sum of a and b is: ", sum)
# sub=a-b
# print("The difference of a and b is: ", sub)    
# mul=a*b
# print("The product of a and b is: ", mul)  
# div=a/b
# print("The division of a and b is: ", div)
# square=a**2
# print("The square of a is: ", square)

# fruits=["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])    
# print(fruits.index("banana"))
# fruits.append("Pinapple")
# print(fruits)
# print(fruits)
# fruits.insert(1, "pinapple")
# print(fruits)
# fruits.remove('apple')
# del fruits[0]

# fruits.pop()
# fruit=fruits.pop()
# print(fruit)
# print(fruits)

# fruits=["apple", "banana", "cherry"]

# for i in fruits:
#     print(i.upper())
# num=[1,2,3,4,5]
# a='Hellow world!'
# for i in range(len(num)):
#     if num[i]==3:
#         break
#     print(num[i] , end=' ')

# for i in fruits:
#     if i=="banana":
#         continue
#     print(i.upper())

# for i in range(0,6,6):
#     print(i)

# ====================================== Dictionary ============================

# student={
#     "name": "Deepak",
#     "branch": "CSE",
#     "year": 2,
#     "batch":2022,
#     "address": 'Ranchi',
#     0:"this is codezeal's titanic it can be break in blue moon.0"
# }

# student["name"]="Rahul"

# for i in student.values():
#     print(i)
# print(student[0], student["name"], student["branch"])
# print(student["year"])

# print(student.keys()) #.keys() method is used to get all the keys of the dictionary.
# print(student.values()) #.values() method is used to get all the values of the dictionary.

# print(len(student))
# student.update({"name":"Rahul Kumar", "year":6, "address":"Seraikella", "phone":1234567890})
# str=student.popitem()
# print(str)
# print(student)

# del student["batch"], student["address"]
# del student
# print(student)

# for i in student.keys():
#     print(student[i])

# =================================== Funcions ===============================.
# def myFirstfunction():
#     print("this is codezeal's titanic, it is starting now.")

# myFirstfunction()

# def sum(a,  b):
#     k=a
#     e=b
#     sum=k+e
#     return sum
# print(sum(2,3))

# ============================= functions with default parameters 12/05/2026=====================

# def add_two_no(a, b):
#     sum=a+b
#     print("sum of "+str(a)+" and "+str(b)+" is: ", sum)

# add_two_no(2,3)

# def check_odd(a):
#     if a%2==0:
#         print(f"{a} is even.")
#     else:
#         print(f"{a} is odd.")

# check_odd(2)
# check_odd(3)

# print("Hello, Deepak Kumar!");


def revers(a):
    reverStr=""
    for i in a:
        reverStr=i+reverStr;
    return reverStr
#     print(a[::-1], end=' ')

name=["Puja", "madam", "racecar", "Satyarth"]
for i in name:
    reverseStr=revers(i)
    if i==reverseStr:
        print(f"{i} is palindrome.") 
    else:
        print(f"{i} is not palindrome.")
# revers(name)   
# for i in name:
#     revers)

# def palindrome(a):
#     if a==a[::-1]:
#         print(f"{a} is palindrome.")
#     else:
#         print(f"{a} is not palindrome.")

# palindrome("dam")