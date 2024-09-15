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

# class parent():
#     def method1(self):
#         return "parent method 1"
    
#     def method2(self):
#         return "parent method 2"
    
# class child(parent):
#     def method3(self):
#         return "child method 3"
    
#     def method4(self):
#         return "child method 4"
    
# obj = child()
# print(obj.method1())
# print(obj.method2())
# print(obj.method3())
# print(obj.method4())


# # Multilevel

# class parent():
#     a = 10

# class child1(parent):
#     c = 12

# class child2(child1):
#     d = 100

# obj = child2()
# print(obj.a)
# print(obj.c)
# print(obj.d)

# # constroctor init

# class parent():
#  def __init__(self):
#     self.a = 10

# class child1(parent):
#   def __init__(self):
#     super().__init__()
#     self.c = 12

# class child2(child1):
#  def __init__(self):
#     super().__init__()
#     self.d = 100

# obj = child2()
# print(obj.a)
# print(obj.c)
# print(obj.d)


# # Multiple

# class GrandParent:
#     def __init__(self):
#         self.generation = "GrandParent"

# class Parent(GrandParent):
#     def __init__(self):
#         super().__init__()  
#         self.family = "Parent"

# class Child(Parent):
#     def __init__(self):
#         super().__init__()  
#         self.child_name = "Child"

# obj = Child()
# print(obj.generation)  
# print(obj.family)      
# print(obj.child_name) 

# class mammal():
#    def mammal_info(self):
#       print("mammals can give direct birth.")

# class wingedanimal():
#    def wingedanimal_info(self):
#       print("winged animals can flap.")   

# class bat(mammal, wingedanimal):
#    pass

# b1 = bat()
# b1.mammal_info()
# b1.wingedanimal_info()


class Mammal:
    def __init__(self, name):
        self.name = name

    def mammal_info(self):
        print(f"{self.name} is a mammal and can give direct birth.")

class WingedAnimal:
    def __init__(self, wing_span):
        self.wing_span = wing_span

    def wingedanimal_info(self):
        print(f"This animal can flap its wings with a wingspan of {self.wing_span} meters.")

class Bat(Mammal, WingedAnimal):
    def __init__(self, name, wing_span):
        Mammal.__init__(self, name) 
        WingedAnimal.__init__(self, wing_span)  


b1 = Bat("Bat", 1.5)
b1.mammal_info()           
b1.wingedanimal_info()      
