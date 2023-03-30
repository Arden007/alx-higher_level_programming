#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list of integers to find peak of
    Returns: peak of list of integers or None
    """

    if list_of_integers is None or list_of_integers == []:
        return None

    size = len(list_of_integers)
    mid = (size // 2)
    mid = int(mid)

    if size == 1:
        return list_of_integers[0]
    if size == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
