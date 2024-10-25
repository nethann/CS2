# Parent class (Base class)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Child class (Derived class)
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call the constructor of the parent class
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

    # Overriding the introduce method
    def introduce(self):
        print(f"Hi, I'm {self.name}, a student with ID {self.student_id}.")

# Creating an instance of the parent class
person1 = Person("Alice", 30)
person1.introduce()  # Calls the Person class introduce method

# Creating an instance of the child class
student1 = Student("Bob", 20, "S12345")
student1.introduce()  # Calls the overridden introduce method in Student
student1.study()  # Calls the study method of the Student class
