"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert places the new value at the requested index
    # Elements at and after that index shift one position to the right.
    # Inserting near the beginning generally requires more shifting than
    # inserting near the end of the list.
    list.insert(lst, index, value)



def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    #Validate index before attempting deletion
    # This prevents an indexError when the requested position doesn't exist.
    if index < 0 or index >= len(lst):
        return None

    #pop() removes and returns the value stored at the specified index.
    # Elements after the removed value shift one position to the left.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search because each element is scanned sequentially
    # from the beginning of the list until the value is found.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

        # Return -1 when the value isn't present
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # Real world application: My spotify playlist.
    playlist = ["Petal", "Tomorrow", "Like I Do"]

    # Displaying original list
    print("Original playlist:" , playlist)

    # Testing insertion at the beginning
    insert_at(playlist,0, "Commando")
    print("After inserting at the beginning:", playlist)

    # Testing insertion at the middle
    insert_at(playlist, 2, "Kiss Me")
    print("After inserting at the middle:", playlist)


    # Testing insertion at the end
    insert_at(playlist, len(playlist), "Bad Habits")
    print("After inserting at the end:", playlist)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")


    # Removing the first item
    removed = delete_at(playlist, 0)

    # Display the removed item and updated list
    print("Removed from beginning:", removed)
    print("Updated playlist:", playlist)


    # Removing an item from the middle
    middle_index = len(playlist) // 2
    removed = delete_at(playlist, middle_index)

    #Display the removed item and updated list
    print("Removed from middle:", removed)
    print("Updated playlist:", playlist)


    # Removing from the end
    removed = delete_at(playlist, len(playlist) - 1)

    # Display the removed item and updated list
    print("Removed from end:", removed)
    print("Updated playlist:", playlist)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")


    # Searching for a song that exists
    found_index = search_value(playlist, "Kiss Me")
    print("Searching for Kiss Me. Index found:", found_index)

    # Searching for a song that does not exist
    missing_index = search_value(playlist, "Tomorrow")
    print("Searching for Tomorrow. Result:", missing_index)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")


    # Case 1: Deleting using an invalid index. Should display "None"
    invalid_delete = delete_at(playlist, 100)
    print("Deleting at invalid index 100:", invalid_delete)

    # Case 2: Inserting into an empty list
    empty_list = []
    insert_at(empty_list, 0, "Deuces")
    print("Insert into empty list:", empty_list)

    # Case 3: Attempting to delete from an empty list
    random_lst = []
    empty_delete = delete_at(random_lst, 0)
    print("Deleting from an empty list:", empty_delete)



if __name__ == "__main__":
    main()