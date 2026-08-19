# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.


## Implementation Documentation

For this assignment, I created a parent class called `ParentClass` that contained a class variable for species and instance variables for name and age. I then created `ChildClass`, which inherited from `ParentClass` and added a school name class variable, student ID, courses list, and a method for enrolling in additional courses. I also overrode the `display_info()` method to display the additional information associated with the child class.
I demonstrated class and instance namespaces by creating two `ChildClass` objects. I accessed the `school_name` class variable through both the class and an object. I then added an `honor_student` attribute to only one object and used `__dict__` to demonstrate how the two instance namespaces differed.
I demonstrated shallow and deep copying using an object containing nested mutable lists. After modifying a nested list in the original object, the same modification appeared in the shallow copy because the nested data was shared. The deep copy remained unchanged because `deepcopy()` created an independent copy of the nested data.
As an extension, I added the `enroll_course()` method, which allowed courses to be added to a student's course list after the object had been created.