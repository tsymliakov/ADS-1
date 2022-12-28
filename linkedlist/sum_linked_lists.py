from linkedlist import Node
from linkedlist import LinkedList


def sum_linkedlists(first : LinkedList, second : LinkedList):
    """Return linked list in which every element is the sum of the
    elements from first and second. first and second must to be the same
    length if it not returns None. If first and second are empty,
    returns empty new linkedlist
    Values of Nodes in linked list have to support sum operation.
    Function use '+' operator"""
    if not first or not second:
        # I would prefer to raise an exception in this case, but
        # so be it
        return None
    summed_values = LinkedList()
    curr_in_first = first.head
    curr_in_second = second.head
    while curr_in_first and curr_in_second:
        # It is possible to check immediately if the lengths of the lists
        # are equal via their .len() method, but this implementation
        # speeds up execution by 10%
        summed_values.add_in_tail(Node(curr_in_first.value +
                                       curr_in_second.value))
        curr_in_first = curr_in_first.next
        curr_in_second = curr_in_second.next

    if isinstance(curr_in_second, type(curr_in_first)):
        return summed_values

    return None
