#!/usr/bin/python3
"""
This module defines the canUnlockAll function.

The function checks whether all the locked boxes can be opened,
given that each box may contain keys to other boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): Each inner list contains keys to other boxes.

    Returns:
        True if all boxes can be opened, False otherwise.
    """
    if not boxes or len(boxes) == 0:
        return False

    opened = [0]
    keys = [0]

    while keys:
        box = keys.pop()
        for key in boxes[box]:
            if key < len(boxes) and key not in opened:
                opened.append(key)
                keys.append(key)

    return len(opened) == len(boxes)
