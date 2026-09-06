# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.



## Implementation Documentation

For this assignment, I implemented a Binary Search Tree in Python using recursive insertion, searching, and in-order 
traversal. I created a Node class that stored a value and references to left and right child nodes. The BST class 
stored the root of the tree and used recursive helper methods to manage its operations.
I inserted seven values into the BST so that values were placed in both the left and right subtrees. Smaller values 
were placed to the left of the current node, while larger values were placed to the right. Duplicate values were ignored.
I implemented a recursive search that returned True when a value was found and False when it was not found. Because 
the BST uses ordering to determine which subtree should be searched, it can reduce the amount of data that must be 
examined compared with a linear search.
I also implemented an in-order traversal that visited the left subtree, the current node, and then the right subtree. 
This produced the BST values in sorted order.
Edge cases included searching and traversing an empty tree and attempting to insert a duplicate value.