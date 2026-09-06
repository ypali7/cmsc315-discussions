"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        self.value = value
        self.left = None
        self.right = None



class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Start recursive insertion at the root
        # Smaller values move left and larger ones move right
        self.root = self._insert_recursive(self.root, value)


    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Place node in empty position
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values belong in the right subtree
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Ignore duplicate values
        return node



    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # A BST is more efficient because it reduces the search space at each
        # step because values smaller than a node are on the left and
        # larger values are on the right
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Return False if value not found
        if node is None:
            return False

        # Return True when target value is found
        if value == node.value:
            return True

        # Search only the subtree where the value could exist
        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is not None:
            # Visit smaller values first
            self._inorder_recursive(node.left, values)

            # Visit the current node
            values.append(node.value)

            # Visit larger values last
            self._inorder_recursive(node.right, values)

            # Because BST values are organized with smaller values
            # on the left and the larger ones on the right,
            # this left-root-right traversal produces sorted output


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    tree = BST()

    # These values create both left and right subtrees
    values = [20, 10, 70, 90, 60, 40, 80]

    for value in values:
        tree.insert(value)

    print("Values inserted:", values)


    # BST organization allows each comparison to choose either
    # the left or the right subtree instead of scanning every value
    print("BST created with values on both left and right subtrees")


    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    traversal = tree.inorder()

    print("In-order traversal:", traversal)
    print("The values appear in sorted order because the traversal visits "
          "the left subtree, current node, and then the right subtree.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")


    # Search for values that exist
    print ("Search for 40:", tree.search(40))
    print ("Search for 80:", tree.search(80))

    # Search for values that don't exist
    print ("Search for 13:", tree.search(13))
    print ("Search for 25:", tree.search(25))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")


    # Searching and traversing an empty BST
    empty_tree = BST ()

    print ("Search empty tree for 20:", empty_tree.search(20))
    print("In-order traversal of empty tree:", empty_tree.inorder())


    # Edge Case: Duplicate insertion
    tree.insert(20)
    print("Traversal after attempting duplicate 20:", tree.inorder())
    print("Duplicate values are ignored in this implementation.")


if __name__ == "__main__":
    main()