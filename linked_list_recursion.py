"""
    File: linked_list_recursion.py
    Author: Xin Li
    Purpose: In this project i will write several recursive
    function.

"""
def is_sorted_recursive(head):
    '''
        This function takes a single parameter, which is a list,
        and returns True or False, indicating whether or not the
        values in the list are sorted. Note that duplicates may
        exist in the list; these count as being in order.An empty
        list should return True.
    '''
    if head is None :
        return True
    if head.next is None:
        return True
    else:
        cur = head
        if cur.val > cur.next.val:
            return False
        return is_sorted_recursive(cur.next)

def accordion_recursive(head):
    if head == None or head.next == None:
        return None
    else:
        cur = head
    cur = cur.next
    cur.next = accordion_recursive(cur.next)
    return cur
