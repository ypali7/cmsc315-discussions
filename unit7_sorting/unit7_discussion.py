import time
"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Create copy of the list so that the original isn't changed
    sorted_list = lst.copy()

    # Make repeated passes through the list.
    for i in range(len(sorted_list)):

        # Compare each pair of adjacent values.
        for j in range(0, len(sorted_list) - i - 1):

            # Swap the values if they are in the wrong order.
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    return sorted_list


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # A list with 0 or 1 elements is already sorted.
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle of the list and divide it into two halves.
    middle = len(lst) // 2
    left_half = lst[:middle]
    right_half = lst[middle:]

    # Recursively sort both halves.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the two sorted halves together.
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    # Create an empty list to store the sorted values.
    result = []

    # Track our current position in each half.
    i = 0
    j = 0

    # Compare values from both halves.
    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining values from either half.
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")

    # Create an unsorted list of values.
    dataset1 = [38, 12, 8, 43, 9, 31, 18, 25]

    # Display the original list.
    print("Original list:", dataset1)

    # Sort the same dataset using both algorithms.
    bubble_result1 = bubble_sort(dataset1)
    merge_result1 = merge_sort(dataset1)

    # Display the results from both sorting algorithms.
    print("Bubble Sort:", bubble_result1)
    print("Merge Sort:", merge_result1)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    #Create a second dataset with different values and a duplicate.
    dataset2 = [100, 15, 48, 99, 26, 48, 5, 61, 34]

    # Display the original list.
    print("Original list:", dataset2)

    # Sort the same dataset using both algorithms.
    bubble_result2 = bubble_sort(dataset2)
    merge_result2 = merge_sort(dataset2)

    # Display and compare the results.
    print("Bubble Sort:", bubble_result2)
    print("Merge Sort:", merge_result2)

    # Check whether both algorithms produced the same result.
    print("Results match:", bubble_result2 == merge_result2)



    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    # Both algorithms should return an empty list because
    # there are no values that need to be sorted.
    empty_list = []

    print("\nEmpty list:")
    print("Original:", empty_list)
    print("Bubble Sort:", bubble_sort(empty_list))
    print("Merge Sort:", merge_sort(empty_list))


    # Edge Case 2: Already sorted list
    # Both algorithms should keep the values in the same order
    # because the list is already sorted.
    sorted_list = [10, 20, 30, 40, 50, 60, 70]

    print("\nAlready sorted list:")
    print("Original:", sorted_list)
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))


    # ===============================
    # PERFORMANCE COMPARISON
    # ===============================

    print("\n=== PERFORMANCE COMPARISON ===")

    # Create a larger reverse-sorted dataset.
    large_dataset = list(range(1000, 0, -1))

    # Measure Bubble Sort execution time.
    start_time = time.perf_counter()
    bubble_sort(large_dataset)
    bubble_time = time.perf_counter() - start_time

    # Measure Merge Sort execution time.
    start_time = time.perf_counter()
    merge_sort(large_dataset)
    merge_time = time.perf_counter() - start_time

    print(f"Dataset size: {len(large_dataset)} values")
    print(f"Bubble Sort time: {bubble_time:.6f} seconds")
    print(f"Merge Sort time: {merge_time:.6f} seconds")


    # ===============================
    # REAL-WORLD SORTING EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD EXAMPLE: EXAM SCORES ===")

    # A professor may need to sort student exam scores
    # from lowest to highest for reviewing class performance.
    exam_scores = [84, 72, 95, 28, 91, 64, 88, 100]

    print("Original exam scores:", exam_scores)

    # Sort the scores using both algorithms.
    bubble_scores = bubble_sort(exam_scores)
    merge_scores = merge_sort(exam_scores)

    print("Bubble Sort:", bubble_scores)
    print("Merge Sort:", merge_scores)

    # Verify that both algorithms produced the same result.
    print("Results match:", bubble_scores == merge_scores)



if __name__ == "__main__":
    main()