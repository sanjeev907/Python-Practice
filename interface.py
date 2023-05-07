# interface is nothing but abstract class which contains only abstract methods but only normal method   

# important points
# 1. we cannot create object of interface
# 2. we use interface, when an action is common but impentations
# 3. All child class should be inherit abstract method.

from abc import ABC,abstractmethod

class interface(ABC):
    @abstractmethod
    def fun(self):
        pass
    
class inter(interface):
    def fun(self):
        print("hello")

class intersection(interface):
    def fun(self):
        print("hello world to everyone")

obj = inter()
obj.fun()
obj1 = intersection()
obj1.fun()