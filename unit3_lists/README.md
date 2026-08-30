# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?




Implementation Documentation
For this assignment, I implemented list insertion, deletion, and searching operations in Python. I created an insert_at()
function that inserted values at a specified index and demonstrated how existing elements shifted when values were
inserted near the beginning or middle of the list. I also created a delete_at() function that safely validated indexes
before removing and returning values. Invalid indexes returned None instead of causing an error. 
I implemented a linear search using search_value(), which checked list elements sequentially and returned matching index
or -1 when the value was not found. I used my spotify playlist as the real world scenario and demonstrated insertions and
deletions at the beginning, middle, and end. I also tested several edge cases, including deleting with an ivalid index,
inserting into an empty list, and deleting from an empty list. These tests helped verify that the program handled the 
boundary conditions safely.
