#While loop 
#syntax 
# i = 1
# while i<=10:
#     print("hello world")
#     i=i+1


# string indexing and slicing
# indexing
# w = "Welcome to wscubetech"
# # print(w[5])
# # print(w[-5])

# # slicing
# print(w[0:7])
# print(w[0::2])



#string iterations

# w = "Welcome to wscubetech"
# t = len(w)
# print (t)
# for a in range(t):
#  print(w[a])

# python string function

# w = "welcome to home"
# # n = w.lower()
# # n = w.upper()
# # n = w.title()
# n = w.capitalize()
# print(n)

# Another python string function

# w = "welcome"
# print(w.find('e',2))
# print(w.isalpha())

# w = "welcome123"
# # print(w.isdigit())
# print(w.isalnum())

# chr() and ord()
# a = chr(70)
# print(a)
# a = ord('a')
# print(type(a),a)

# python string Format() method

# w ="welcome {} my {}".format("to","channel")
# w ="welcome {1} my {0}".format("to","channel")
# w ="welcome {b} my {a}".format(a=30,b=4)
# print(w)


# how to create list in python

# print(l[0:2])
# print(l)
# print(l[3][2])

# l= [2,3,"hello",[4,5,6,7,8]]
# print(type(l[2:4]))

# l= [2,3,"hello",[4,5,6,7,8]]
# # print(l[0:2])
# print(l[1:])


# list comprehension
# n = [m for m in range (1,101)]
# print(n)

# l=[1,2,3,4,5,6,7,8]
# # del l[2]
# l.pop(2)
# print(l)


# zip Function

# l=[10,20,30,40]
# l2=[4,5,6,7]
# for a,b in zip(l,l2):
#  print(a,b)

#split function

# a=input("enter the value\n")
# l=a.split()
# print(l)

# for multiple strings
# l=[]
# for a in range(1,4):
#     n=input("enter the value")
#     l.append(n)

# print(l)


# dictionary

# d={
#     'name':'python',
#     'Fess':8000,
#     'duration':'2 Months'
# }
# print(type(d))
# print(d['Fess'])
# for n in d:
#     print(n)
#     print(d[n])


# dictionary Functions


# d={
#     'name':'python',
#     'Fess':8000,
#     'duration':'2 Months'
# }

# # get()
# n=d.get('name')
# print(n)

# # key()
# for a in d.keys():
#     print(a)

#values

# for a in d.values():
#     print(a)

# items()

# for a,b in d.items():
#     print(a,b)

#delete

# del d['duration']
# print(d)

# pop()

# a = d.pop('duration')
# print(a)


# Nested Dictionary

# course={
#     'PHP':{'duration':'2Months','fess':8000},
#     'JAVA':{'duration':'2Months','fess':18000},
#     'PYTHON':{'duration':'2Months','fess':28000},
# }

# print(course)
# print(course['PHP']['fess'])
# course['JAVA']['fess']=20000
# print(course)

# del course['JAVA']['fess']
# print(course)


# for k,v in  course.items():
    # print(k,v)
    # print(k,v['duration'])

# Sets in Python

# s=[10,20,30]
# se=set(s)
# print(se)
# # for a in s:
#     print(a)

# s.add(49)
# print(s)

# s={10,20,30,40}
# # s.pop()
# # s.remove(20)
# # s.discard(20)
# # s.clear()
# l=[30,50,60]
# s.update(l)
# print(s)


# Functions in Python

# def simplefunction():
#     print("Welcome to everone")

# simplefunction()


# function with argument

# def sumdata(a,b=10):
#     print(a+b)

# n=int(input("please enter the value of n\n"))
# n1=int(input("please enter the value of n1\n"))
# sumdata(10,20)
# sumdata(n,n1)

# default arugument
# return function

# def sumdata(a,b=10):
#     c=(a+b)
#     return c

# a=sumdata(10,20)
# print(a)



# Module in Python

# from module import *
# print(sumdata(10,20))
 
# fuction of module

# math.ceil()
 
# import math
# x=10.5
# print(math.ceil(x))


# x1=-50
# print(math.fabs(x1))

# y=5
# print(math.factorial(y))

# z=10.5
# print(math.floor(z))

# l=[10,20,13,50]
# print(math.fsum(l))

# print(math.sqrt(5))

# Random module 

# import random

# n=random.randint(2,8)
# print(n)

# n1=random.randrange(2,8)
# print(n1)

# l=[10,20,30,40]
# # print(random.choice(l))

# # print(random.random())

# random.shuffle(l)
# print(l)


# print(random.uniform(3,9))

# date time Module

# import datetime

# x=datetime.datetime.now()
# print(x)
# x=datetime.datetime(2012,1,18)
# print(x)

# srtftime function

# a=datetime.datetime.now()
# year=a.strftime("%I")
# print(year)

# Number Guessing Game 

# Object oriented programming in python

# class car:
#     a= "alto"
#     b="Cycle"
#     c="fortuner"
#     d="swift"
#     def sumvalue (self):
#         print(30+20)
# object1=car()
# object2=car()
# # print(object2.b)
# object1.sumvalue()

# method in OOB

# class DemoClass:
#     a=10

#     def __init__(self):
#         print("Welcome to Here")


#     def Showvalue(self):
#         self.c= self.a * self.a
#         print(self.c)

#     def showvalue1(self,a,b):
#         print(a+b)

# obj=DemoClass()
# obj.Showvalue()
# obj.showvalue1(10,20)


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a = max(l)
# # b = set(a)
# # print(b)
# print(a)


# s = {10,20,30,40,50}
# s1 = {50,40,30,20}
# z= s.intersection(s1)
# print(z)

s = "sanjeev kaushik"
code = s[:-8]
a = f'{code}'
print(a)