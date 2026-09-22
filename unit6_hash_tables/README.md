# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

This assignment helped me understand how Python dictionaries work as hash tables by storing information as key-value 
pairs. I practiced inserting, retrieving, updating, and deleting data using course codes as keys and enrollment numbers 
as values. I also learned how .get() can safely search for a missing key without causing a KeyError. Testing missing 
courses showed me why handling edge cases is important. One challenge was understanding what happens when a key already 
exists. Updating CMSC315 from 28 to 35 showed me that dictionaries replace the value associated with the existing key 
instead of creating a duplicate entry.

Hash tables use a hash function to determine where keys and their values are stored. Sometimes different keys can map 
to the same location, which is called a collision, so the underlying implementation must handle those collisions. Hash 
tables are efficient because lookups, insertions, and deletions are typically O(1) on average. My support-ticket example 
showed how this could be useful in a real system because a ticket ID can quickly retrieve or update its current status.
This assignment helped me understand how Python dictionaries work as hash tables by storing information as key-value 
pairs. I practiced inserting, retrieving, updating, and deleting data using course codes as keys and enrollment numbers 
as values. I also learned how .get() can safely search for a missing key without causing a KeyError. Testing missing 
courses showed me why handling edge cases is important. One challenge was understanding what happens when a key already 
exists. Updating CMSC315 from 28 to 35 showed me that dictionaries replace the value associated with the existing key 
instead of creating a duplicate entry.

Hash tables use a hash function to determine where keys and their values are stored. Sometimes different keys can map to
the same location, which is called a collision, so the underlying implementation must handle those collisions. Hash 
tables are efficient because lookups, insertions, and deletions are typically O(1) on average. My support-ticket 
example showed how this could be useful in a real system because a ticket ID can quickly retrieve or update its 
current status.
