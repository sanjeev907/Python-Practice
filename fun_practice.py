# def sum(*args):
#     print(args)
# obj = sum(8+2+3+0+7)


# def max(x,y,z):
#     if x>y:
#         print("x is big than Y")
#     elif y>z:
#         print("y is big than z")
#     elif z>x:
#         print("z is big than x")
#     else:
#         print("error")

# obj = max(5,10,2)


# def mutiple(*args):
#     print(args)
# m = mutiple(8 * 2 * 3 * -1 * 7)


# def r():
#     s = "1234abcd"
#     a = s[::-1]
#     b = f'{a}'
#     print(b)

# obj = r()

# import math

# def fact():
#   x = 4**3*2*1
#   f = math.factorial(x)
#   print(f)

# d= fact()

# def up():
#     s = 'The quick Brow Fox'
#     upper = 0
#     lower = 0
#     for i in s:
#         if i.isupper():
#             upper += 1
#         elif i.islower():
#             lower += 1
#     print(upper)
#     print(lower)
# obj= up()

# def unique():
#     a1 = [1,2,3,3,3,3,4,5]
#     x= []
#     for a in a1:
#         if a not in x:
#             x.append(a)
#             print(x)

# obj = unique()


# def prime():
#     a = int(input("enter the number\n"))
#     if (a%2)==0:
#         print("composite number is this")
#     else:
#         print("This is prime number")

# a = prime()


# def even():
#     l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     enum = []
#     for i in l:
#         if i % 2==0:
#             enum.append(i)
#             print(enum)
   
# d = even()

# def pad():
#     a = input("Enter the value\n")
#     if a == a[::-1]:
#         print("yes")
#     else:
#         print("NO")
    
# d = pad()



# def demo(fname):
#     # a = 10
#     # b = 20
#     # c = a + b
#     # print(a+b)
#     print(fname)
# o = demo(5)

# def demo2():
#     global a
#     a = 10
#     print(a)

# def demo3(self):
#     b = 10
#     print(b,self.a)
    
# obj = demo2()
# obj1 = demo3()


# a =10
# def add():
#     print(a)

# a =add()

# a =10

# class p:
#     def __init__(self,name):
#         print(name)

# obj = p("name")

# def rev():
#     s = "green-red-yellow-black-white"
#     a = list(s)
#     a.sort(reverse=True)
#     b = ''.join(map(str,a))
#     print(b)
# r = rev()

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# a = []
# def square():
#     for i in l:
#         a.append(i **2)
#         print(a)

# square()

# def add():
#     a =10
#     b =20
#     c= a+b
#     print(c)
#     def sub():
#         x = 2
#         y = 3
#         z = y-x
#         print(z)
#     sub()

# add()      


# a =15555
# class sa:
#     b=20
#     def add(self,name,age):
#        print(a,name,age,self.b)

# obj =sa() 
# obj.add("sanju",25)


# x = 14
# class f:
#     a = 15
#     def fun(self,b):
#         print(x,self.a,b)


#     def sum(self):
#         print(x)


# o= f()
# o.fun(5)
# # o.sum()

# a = 20
# def fun():
    
    
#     print(a)
#     def fun2():
#         print(a)
#     fun2()

# fun()

# b = 20
# class A:
#     s = 25
#     def fun(self):
#         print(b,self.s)
#     def fun2(self):
#         print(b)
    
        

# C = A()
# C.fun()
# C.fun2()

# def fun():
#     l = [5,25,15]
#     m = max(l)
#     print(m)

# fun()


# def fun():
#     t = (8, 2, 3, 0, 7)
#     s = sum(t)
#     print(s)

# fun()


# def fun():
#     t = (8, 2, 3, -1, 7)
#     l = list(t)
#     a = 1
#     for i in l:
#         a = a * i
    
#     print(a)

# fun()

# def fun():
#     s = "1234abcd"
#     l = list(s)
#     l.reverse()
#     a = ''.join(map(str,l))
#     print(a)

# fun()


# def fun(n):
#     if n ==0:
#         print(1)
#     else:
#         a = n * (n-1)
#         print(a)

# fun(4)

# def fun():
#     l = [1,2,3,3,3,3,4,5]
#     a = set(l)
#     b = list(a)
#     print(b)


# fun()

# def fun(*args,**kwargs):
#     print(args,)

# fun("sanjeev","kaushik","sdjddds","saisasa")


# def fun():
#     s = "The quick Brow Fox"
#     upper = 0
#     lower = 0
#     for i in s:
#         if i.isupper():
#             upper = upper + 1
#         elif i.islower():
#             lower = lower + 1
#         else:
#             pass
    
#     print(upper,lower)

# fun()


# def fun():
#     l = [1,2,3,3,3,3,4,5]
#     a = set(l)
#     b = list(a)
#     print(b)


# fun()

# def fun():
#     l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     new = [i for i in l if i %2==0]
#     print(new)

# fun()