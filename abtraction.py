# Abstarction is process of hiding the  implementations details from the user and provide only highlighted services to the user


# topic Abstract Class 

# Abstract class is the that contain one or more abstract method is called abstarct class  

# note 1. An object of an abstarct class is cannot created.
    #  2. python provide the abc module to work on abstract class 
    #  3. we use @abstactmethod decorator to define the abstact method.

# from abc import ABC,abstractmethod
# class car(ABC):
#     def show(self):
#         print("Every car have 4 whell")
#         @abstractmethod
#         def speed(self):
#             pass

# class Maruti(car):
#     def speed(self):
#         print("the speed of maruti is 100/km/hr.")

# class Tata(car):
#     def speed(self):
#         print("the speed of maruti is 180/km/hr.")


# obj = Maruti()
# obj.show()
# obj.speed()
# obj1 = Tata()
# obj1.show()
# obj1.speed()



# from abc import ABC,abstractmethod
# class A(ABC):
#     def show(self):
#         print("hello world")
#         @abstractmethod
#         def fun1():
#          pass
        
# class B(A):
#     def fun1(self):
#         print("hello")

# obj = B()
# obj.show()
# obj.fun1()