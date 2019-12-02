"""
this file contains implementation for some shared functions to make life easier

"""
from classes.ListNode import ListNode


def list_to_linked_list(inp):
    """
    creates a linked list representing the given list
    :param inp: a list object
    :return:  a linked list representing the list
    """

    # ensure the list has items
    if len(inp) == 0:
        return None

    the_head = ListNode(inp[0])
    the_tail = the_head

    for index in range(1, len(inp)):
        new_item = ListNode(inp[index])
        the_tail.next = new_item
        the_tail = new_item

    return the_head


def linked_list_to_list(inp: ListNode):
    """
    turns a linked list to a regular list
    :param inp: the linked list
    :return: the list object represnting the given linked list
    """
    ret = []

    while inp is not None:
        ret.append(inp.val)
        inp = inp.next

    return ret


def print_linked_list(inp: ListNode):
    """
    prints a linked list in an ordered fasion
    :param inp: the linked list
    :return: nothing
    """

    the_string = " -> ".join([str(x) for x in linked_list_to_list(inp)])

    print(the_string)
