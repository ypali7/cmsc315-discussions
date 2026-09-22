"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # A Python dictionary behaves like a hash table by storing
    # information as key-value pairs. Each unique course code
    # is used as a key to access its associated enrollment value.
    course_enrollment = {}

    # Add five course enrollment records.
    course_enrollment["CMSC315"] = 28
    course_enrollment["BIOL103"] = 32
    course_enrollment["MATH140"] = 25
    course_enrollment["ENGL102"] = 30
    course_enrollment["HIST125"] = 22

    print("Course enrollment:", course_enrollment)

    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    #Dictionary values can be retrieved directly by using their keys
    # Python hashes the key to efficiently locate the associated value.
    print("CMSC315 enrollment:", course_enrollment["CMSC315"])
    print("BIOL103 enrollment:", course_enrollment["BIOL103"])



    print("\n=== UPDATE OPERATIONS ===")

    #Display the dictionary before updating the value
    print("Before update:", course_enrollment)

    #Assigning a new value to existing key will replace the current value.
    course_enrollment["CMSC315"] = 35

    # Display the dictionary after the update
    print("After update:", course_enrollment)
    print ("Updated CMSC315 enrollment:", course_enrollment["CMSC315"])


    print("\n=== DELETE OPERATIONS ===")

    #Display the dictionary before deleting a value.
    print("Before deletion:", course_enrollment)

    # del removes the key and its associated value
    del course_enrollment["HIST125"]

    #Display the dictionary after deleting key-value pair.
    print("After deletion:", course_enrollment)


    print("\n=== EDGE CASES ===")

    # Edge case 1: Look up a key that does not exist.
    # get() safely returns None instead of causing a KeyError.
    missing_course = course_enrollment.get("CHEM101")
    print("Lookup for missing CHEM101:", missing_course)

    # Edge case 2: Attempt to delete a key that does not exist.
    # Check for the key first so the program does not cause a KeyError.
    if "PHYS101" in course_enrollment:
        del course_enrollment["PHYS101"]
    else:
        print("PHYS101 was not found, so nothing was deleted.")

    print("Dictionary after edge cases:", course_enrollment)

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SCENARIO: SUPPORT TICKET LOOKUP ===")

    # A help desk can use a dictionary to associate each unique
    # ticket number with its current support status.
    support_tickets = {
        "T1001": "Open",
        "T1002": "In Progress",
        "T1003": "Waiting for Customer",
        "T1004": "Resolved"
    }

    print("Support tickets:", support_tickets)

    # Quickly look up the status of a specific support ticket.
    ticket_id = "T1002"
    print(ticket_id, "status:", support_tickets.get(ticket_id))

    # Update the ticket when its status changes.
    support_tickets["T1002"] = "Resolved"
    print(ticket_id, "updated status:", support_tickets.get(ticket_id))

    # Add a new support ticket.
    support_tickets["T1005"] = "Open"
    print("New ticket added:", support_tickets)

    # Remove a ticket that no longer needs to be stored.
    del support_tickets["T1004"]
    print("After removing T1004:", support_tickets)



if __name__ == "__main__":
    main()