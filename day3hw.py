class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(lst):
    if not lst:
        return None

    head = Node(lst[0])
    current = head

    for i in range(1, len(lst)):
        current.next = Node(lst[i])
        current = current.next

    return head
def sort_input_list(func):
    def wrapper(lst):
        sorted_lst = sorted(lst)
        return func(sorted_lst)
    return wrapper
@sort_input_list
def create_linked_list(lst):
    if not lst:
        return None

    head = Node(lst[0])
    current = head

    for i in range(1, len(lst)):
        current.next = Node(lst[i])
        current = current.next

    return head

