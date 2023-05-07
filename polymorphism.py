# It is ablity to take various forms(same object having differnt behaviors) 

# we can perform Polymorphism with method    
# 1. overloading
# 2.overriding


# method overloading (whenever class contain  more than one method with same name and different type of parameter called overloading )

# class A:
#     def show(self):
#         print("welcome")
    
#     def show(self,first_name=''):
#         print("welcome",first_name)

#     def show(self,first_name='',lst_name=''):
#         print("welcome",first_name,lst_name)

# obj= A()
# obj.show()
# obj.show("Sanjeev")
# obj.show("Sanjeev","Kaushik")


# 2. Method overriding (whenever we write method name with same signature in parent and child class called method overriding)

# class parent:
#     def show(self):
#         print("This is the parent class:")

# class Child(parent):
#     def show(self):
#         super().show()
#         print("This is the child class:")


# obj1 = Child()
# obj1.show()


# 3.mutithreading
# mutithreading is a techique which allowa a cpu to execute mutiple-threads one process at teh same time .

# why mutithreading:-
# the purpose of the muti threading is to run mutiple task and functions at the same time  

# from time import sleep
# from threading import Thread
# class A(Thread):
#     def run(self):
#         for i in range(5):
#             print("sanjeev")
#             sleep(1)

# class B(Thread):
#     def run(self):
#         for i in range(5):
#             print("kaushik")
#             sleep(1)

# t1 = A()
# t1.start()
# t2 = B()
# t2.start()

