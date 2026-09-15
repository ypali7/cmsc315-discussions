# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

This assignment helped me better understand how linear search and binary search work and how their efficiency changes 
depending on the size of the dataset. Linear search checks each element one at a time, giving it O(n) time complexity, 
while binary search repeatedly cuts the search area in half. Testing both algorithms on a small dataset and then on a 
dataset with 10,000 values helped me see why binary search becomes more useful as the amount of data increases. I also 
tested edge cases using an empty list and a single-element list to make sure both algorithms handled them correctly. 
The biggest challenge for me was understanding how low, high, and mid work together during binary search. Walking 
through how the search area changes after each comparison helped me understand it better. Linear search is useful for 
small or unsorted datasets because it does not require the data to be sorted. Binary search is much faster for large, 
sorted datasets, but requiring sorted data is a tradeoff. For example, searching through a large sorted list of user 
IDs would be a good use for binary search.
