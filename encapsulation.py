# Python Encapsulation
# By using Encapsultion, we can resrict the variable and method to access globally by making it private and protected

# _a stand for (protected)
# __a stand for (private)

class A:
    _a = 10 #protected
    __b =20 #private

    def show(self):
        print(self._a,self.__b)

obj = A()
obj.show()