"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    #Check each value in the list from beginning to end
    for index in range(len(lst)):
        if lst[index] == target:
            return index


    #Linear search has O(n) time complexity because in the
    #worst case it may need to check every value in the list.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # set the boundaries of the search area
    low = 0
    high = len(lst) - 1

    while low <= high:
        # Find the middle index of the current search area
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid

        #if the target is larger, eliminate the left half
        elif lst[mid] < target:
            low = mid + 1

        # if the target is smaller, eliminate the right  half
        else:
            high = mid - 1

    # Target was not found
    return -1



def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_data = [5, 10, 15, 20, 25, 30, 35, 40]

    # Test a value that exists in the dataset
    target_found = 25

    print ("Dataset:", small_data)
    print("Searching for:", target_found)
    print ("Linear search index:", linear_search(small_data, target_found))
    print("Binary search index:", binary_search(small_data, target_found))

    # Testing for a value that does not exist in the dataset.
    target_missing = 100

    print ("\nSearching for:", target_missing)
    print ("Linear search index:", linear_search(small_data, target_missing))
    print("Binary search index:", binary_search(small_data, target_missing))


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large_data = list(range(1, 10001))

    # Search for a value near the end of the dataset
    large_target = 9999

    print ("Dataset size:", len(large_data))
    print ("Searching for", large_target)
    print ("Linear search index:", linear_search(large_data, large_target))
    print ("Binary search index:", binary_search(large_data, large_target))

    # Binary search is more efficient on large sorted datasets
    # because it eliminates half of the remaining search area
    # during each comparison


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # Edge case: Empty list
    empty_data = []

    print ("Empty list:")
    print ("Linear search:", linear_search(empty_data, 20))
    print ("Binary search:", binary_search(empty_data, 20))
    #Both searches should return -1 because there aren't any values to search



    # Edge case 2: Single element list
    single_data = [20]
    print ("\nSingle element list:")
    print ("Searching for 20")
    print ("Linear search index:", linear_search(single_data, 20))
    print ("Binary search index:", binary_search(single_data, 20))

    # Both searches return index 0 because 20 is the only element and it matches the target.

    # ===============================
    # REAL-WORLD SEARCH SCENARIO
    # ===============================
    #
    # A system may need to search through a list of user IDs
    # to determine whether a specific user exists.

    print("\n=== REAL-WORLD SEARCH SCENARIO ===")

    # Sorted list of user IDs
    user_ids = [1001, 1005, 1010, 1015, 1020, 1025, 1030, 1035]
    target_user = 1025

    print("User IDs:", user_ids)
    print("Searching for user ID:", target_user)

    linear_result = linear_search(user_ids, target_user)
    binary_result = binary_search(user_ids, target_user)

    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Both algorithms find the same user, but binary search
    # becomes more efficient when the sorted list contains
    # a large number of user IDs.


if __name__ == "__main__":
    main()