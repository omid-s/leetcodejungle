"""
this file contains implementation for some shared functions to make life easier

"""
from classes.ListNode import ListNode


def list_to_linked_list(inp, as_int=True):
    """
    creates a linked list representing the given list
    :param inp: a list object
    :return:  a linked list representing the list
    """

    # ensure the list has items
    if len(inp) == 0:
        return None

    the_head = ListNode(inp[0] if not as_int else int(inp[0]))
    the_tail = the_head

    for index in range(1, len(inp)):
        new_item = ListNode(inp[index] if not as_int else int(inp[index]))
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


def add_with_carry(n1: int, n2: int, carry=0):
    """
    adds two single digit numbers and returns the result in term of a single digit and a carry
    :param n1: first number
    :param n2: second number
    :param carry: carry from previous steps
    :return: the digit, the carry
    """
    num = n1 + n2 + carry
    return num % 10, num // 10


def array_equal(a, b):
    for x in a:
        if x not in b:
            return False
    return len(a) == len(b)


def str2LinkedList(inp, as_int=True):
    """
    turns an string representation of the linked list into an actual linked list
    :param inp: the "->" separated string representation
    :return: the linked list head
    """
    if len(inp.strip()) == 0:
        return None

    items = inp.split("->")

    return list_to_linked_list(items, as_int=as_int)


def linkedlist2Str(inp):
    """
    turns a linked list into a -> separated string
    :param inp: the linkedlist head
    :return: the string representation
    """
    the_string = "->".join([str(x) for x in linked_list_to_list(inp)])
    return the_string
