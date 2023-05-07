# default contructor

# class A:
#     name = "Shyam"
#     age = 25

#     def __init__(self):
#         address ="faridabad"
#         print(self.name," ",address)
    
#     def show(self):
#         country = 'India'
#         print(country)

# obj =A()
# obj.show()




# Python Parameterized cOnstructor 

# class A:
#       subject = "English"
#       def __init__(self,name,age,address):
#           print(name,age,address,self.subject)
    
#       def show(self,group):
#            print(self.subject,group)


# obj =A("sanjeev",25,"Faridabad")
# obj.show("B+")



# Inhertiance
# 1 simple Inhertiance

# child class inhert the property of Parents Class 


# class A:
#  num1 = int(input("Enter the First Value\n"))
#  num2 = int(input("Enter the Second Value\n"))

#  def Add(self):
#   num3 = self.num1 + self.num2
#   print(num3)

#  def Sub(self):
#   num4 = self.num1 - self.num2
#   print(num4)

# class B(A):
#  def Mutiple(self):
#   num5 = self.num1 * self.num2
#   print(num5)
 
#  def Divide(self):
#   num6 = self.num1 / self.num2
#   print(num6)

# obj = B()
# obj.Add()
# obj.Sub()
# obj.Mutiple()
# obj.Divide()

# 2 . Multi-level Inheritance (single parent class and mutiple Child Class in multi level Inheritance)

# class Parent:
#     num1 = int(input("Enter the First Value\n"))
#     num2 = int(input("Enter the Second Value\n"))
 
#     def Add(self):
#         print(self.num1 + self.num2)

# class Child1(Parent):
#     def Sub(self):
#         print(self.num1 - self.num2)

# class Child2(Child1):
#     def Mutiple(self):
#         print(self.num1 * self.num2)

# obj = Child1()
# obj.Add()
# obj.Sub()

# obj2 = Child2()
# obj2.Mutiple()
# obj2.Sub()



# 3. Multiple Inheritance(We have diferent Parents Class but single child class in Mutiple Inheritance(only single class inhert the properties of all Parents Class))

# class Parent1:
#     def Add(self):
#         num1= int(input("Enter the First Value\n"))
#         num2 = int(input("Enter the Second Value\n"))
#         print(num1 + num2)
# class Parent2:
#     def Sub(self):
#         num1= int(input("Enter the First Value\n"))
#         num2 = int(input("Enter the Second Value\n"))
#         print(num1 - num2)

# class Parent3:
#     def Mutiple(self):
#         num1= int(input("Enter the First Value\n"))
#         num2 = int(input("Enter the Second Value\n"))
#         print(num1 * num2)

# class Parent4:
#     def Divide(self):
#         num1= int(input("Enter the First Value\n"))
#         num2 = int(input("Enter the Second Value\n"))
#         print(num1 / num2)


# class Child(Parent1,Parent2,Parent3,Parent4):
#     def Rem(self):
#         num1= int(input("Enter the First Value\n"))
#         num2 = int(input("Enter the Second Value\n"))
#         print(num1 % num2)


# obj = Child()
# obj.Add()
# obj.Sub()
# obj.Mutiple()
# obj.Rem()


# hierarchical Inheritace(we have single but different child which each class inhert the properties of single Parent Class)


# for study only

# class person:
#     a = 10
#     def __init__(self,name,age):
#         b = 20
#         print(name,age,self.a)
    
#     def show(self,suject,address,age):
#         print(suject,address,age)
        

# obj = person("sanjeev",25)
# obj.show("english","shahpur",26)
