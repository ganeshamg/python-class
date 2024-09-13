# class parent():
#     a = 10
#     b = 11

# class child(parent):
#     c = 12

# obj = child()
# print(obj.a)


# Parent class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

#     def parent_method(self):
#         print("This is a method in the Parent class.")

# # Child class inheriting from Parent
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Calling the constructor of the Parent class
#         self.age = age

#     def child_method(self):
#         print(f"I am {self.age} years old.")

#     def greet(self):  # Overriding the greet method from Parent class
#         print(f"Hi, I'm {self.name}, and I'm {self.age} years old.")

# # Creating an object of the Child class
# child_obj = Child("Saharsh", 11)

# # Accessing methods from both Parent and Child classes
# child_obj.greet()           # Calls the overridden greet method from Child class
# child_obj.parent_method()    # Calls the method from Parent class
# child_obj.child_method()     # Calls the method from Child class

class parent():
    def method1(self):
        return "parent method 1"
    
    def method2(self):
        return "parent method 2"
    
class child(parent):
    def method3(self):
        return "child method 3"
    
    def method4(self):
        return "child method 4"
    
obj = child()
print(obj.method1())
print(obj.method2())
print(obj.method3())
print(obj.method4())


