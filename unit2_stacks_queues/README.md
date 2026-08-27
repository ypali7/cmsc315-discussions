# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.



Implementation Documentation

For this assignment, I implemented both a stack and a queue in Python. The stack used a Python list to store values and
supported push, pop, peek, and empty-check operations. I demonstrated LIFO behavior by adding several actions and removing 
them in reverse order. I also tested edge cases by popping and peeking from an empty stack and by removing the only item 
from a single-item stack.
The queue used collections.deque and supported enqueue, dequeue, front, and empty-check operations. I demonstrated FIFO 
behavior by adding several support tickets and removing them in the same order they were added. I also tested empty-queue
behavior and verified that a single-item queue became empty after its item was removed. The real-world examples used an 
action history for the stack and a support-ticket line for the queue.