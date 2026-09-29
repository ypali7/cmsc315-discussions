# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

This assignment helped me better understand how Bubble Sort and Merge Sort approach the same problem in different ways. 
Bubble Sort was easier for me to understand because it compares adjacent values and swaps them when they are out of 
order. Merge Sort was more complex because it uses recursion to divide a list into smaller sections and then merges 
them back together in sorted order. Working through the merge function helped me understand the divide-and-conquer 
concept better.
The biggest challenge was understanding how the recursive calls in Merge Sort worked together with the merge function. 
Breaking the algorithm into smaller steps made it easier to understand how each half eventually becomes sorted.
The performance test showed the biggest difference between the algorithms. With 1,000 reverse-sorted values, Bubble Sort
took 0.122473 seconds, while Merge Sort took only 0.002702 seconds. Bubble Sort has O(n²) time complexity, making it 
more suitable for small datasets or simple implementations. Merge Sort runs in O(n log n), making it better for larger 
datasets, although it requires additional memory while dividing and merging the lists.