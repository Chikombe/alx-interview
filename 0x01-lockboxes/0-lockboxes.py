"""
This module provides a function to determine if all boxes can be opened.

Each box is numbered sequentially and may contain keys to other boxes.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of list of int): A list where each index represents
                                    a box and contains a list of
                                    keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    # Number of boxes
    n = len(boxes)
    # Set to keep track of opened boxes
    opened = set()
    # Stack for DFS
    stack = [0]

    # Start by opening the first box
    opened.add(0)

    while stack:
        # Get the last box from the stack
        current_box = stack.pop()

        # Iterate through each key in the current box
        for key in boxes[current_box]:
            if key not in opened and 0 <= key < n:
                # If the box corresponding to the key hasn't been opened,
                # open it
                opened.add(key)
                # Add it to the stack to explore further
                stack.append(key)

    # Check if all boxes have been opened
    return len(opened) == n
