# # Simple Inheritance

# # Base Class
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Derived Class
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks.")

# # create an instance of an animal
# animal = Animal("Generic Animal")
# animal.speak()

# # create ann instance of a dog
# dog = Dog("Buddy")
# dog.speak()


"""Super Key"""

# Base Class
class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class
class Dog(Animal):
    def __init__(self,breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak() # call the base class method
        print(f"{self.name} barks.It's a {self.breed}")
    
# create an instance of Dog
dog = Dog("Golden Retriever")
dog.speak()