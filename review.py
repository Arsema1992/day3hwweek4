from linkedlist import Node, LinkedList

def sorting_decorator(func):
    def inner(list):
        list.sort()

        func(list)
    return inner
@sorting_decorator
def convert_to_linked_list(alist):
    head_node = Node(alist[0])
    linkedList = LinkedList(head_node)
    for i in range(1,len(alist)):
        LinkedList.insert_after(alist[i])
    linkedList.print_nodes()


convert_to_linked_list([4,1,5,100,40])