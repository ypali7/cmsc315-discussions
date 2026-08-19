"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Species: {self.species}"




# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    school_name = "UMGC"

    def __init__(self, name, age, student_id, courses):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = courses

    def enroll_course(self, course_name):
        self.courses.append(course_name)

    def display_info(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"Student ID: {self.student_id}, "
            f"School: {self.school_name}, "
            f"Courses: {self.courses}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    student1 = ChildClass("Jason", 21, "S1234", ["CMSC 315"])
    student2 = ChildClass("Mateo", 22, "S5678", ["BIOL 103"])

    # Access class variable through the class
    print("Class variable through class:", ChildClass.school_name)

    # Access the same class variable through an object
    print("Class variable through object:", student1.school_name)

    # Add a new attribute to only one object
    student1.honor_student = True

    # Display instance namespaces
    print("Student 1 namespace:", student1.__dict__)
    print("Student 2 namespace:", student2.__dict__)

    # Display information about the class namespace
    print("ChildClass namespace:")
    print(ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")


    original = ChildClass(
        "Taylor",
        20,
        "S2001",
        [["CMSC 315", "Python"], ["BIOL 103", "Biology"]]
    )

    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # A shallow copy creates a new outer object, but nested mutable
    # objects are still shared with the original.
    #
    # A deep copy creates a new object and recursively copies nested
    # mutable objects, so changes to the original do not affect it.

    original.courses[0].append("Data Structures")

    print("Original courses:", original.courses)
    print("Shallow copy courses:", shallow_copy.courses)
    print("Deep copy courses:", deep_copy.courses)



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nParent Object")
    parent = ParentClass("Angela", 33)
    print(parent.display_info())

    print("\nChild Object")
    student = ChildClass("Iscus", 21, "S3456", ["CMSC 315"])
    print(student.display_info())

    # Student inherited the species class variable from ParentClass
    print("Inherited species:", student.species)

    # Student-created extension
    student.enroll_course("BIOL 103")
    print("After enrolling in another course:")
    print(student.display_info())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()