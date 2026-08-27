"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # New values are added to the end, making the newest item the first removed.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if self.is_empty():
            return "Stack is empty."
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek allows the top item to be viewed without changing the stack.
        if self.is_empty():
            return "Stack is empty."
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values are added to the back so older values leave first.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            return "Queue is empty."
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front allows the oldest queued item to be viewed without removing it.
        if self.is_empty():
            return "Queue is empty."
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")

    stack = Stack()

    print("Adding four actions to the stack:")
    stack.push("Open document")
    stack.push("Type paragraph")
    stack.push("Insert image")
    stack.push("Save document")

    print("Top item:", stack.peek())

    print("\nRemoving items demonstrates LIFO behavior:")
    while not stack.is_empty():
        print("Popped:", stack.pop())

    print("\nAttempting to pop from an empty stack:")
    print(stack.pop())

    print("Attempting to peek at an empty stack:")
    print(stack.peek())

    single_stack = Stack()
    single_stack.push("Only item")

    print("\nSingle-item stack test:")
    print("Removed:", single_stack.pop())
    print("Stack empty afterward:", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")

    queue = Queue()

    print("Adding four support tickets to the queue:")
    queue.enqueue("Reset password")
    queue.enqueue("Install printer")
    queue.enqueue("Update software")
    queue.enqueue("Unlock account")

    print("Front item:", queue.front())

    print("\nRemoving items demonstrates FIFO behavior:")
    while not queue.is_empty():
        print("Dequeued:", queue.dequeue())

    print("\nAttempting to dequeue from an empty queue:")
    print(queue.dequeue())

    print("Attempting to view the front of an empty queue:")
    print(queue.front())

    single_queue = Queue()
    single_queue.enqueue("Only ticket")

    print("\nSingle-item queue test:")
    print("Removed:", single_queue.dequeue())
    print("Queue empty afterward:", single_queue.is_empty())


if __name__ == "__main__":
    main()