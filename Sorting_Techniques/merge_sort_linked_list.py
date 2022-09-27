from codes.Data_Structures.Linked_List import LinkedList


def merge_sort_linked_list(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge the sublist to produce sorted sublists until one remains
    
    Returns a sorted linked list
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split_linked(linked_list)
    
    left = merge_sort_linked_list(left_half)
    right = merge_sort_linked_list(right_half)
    
    return merge_linked(left, right)

def split_linked(linked_list):
    """
    Divide the unsorted linked list at midpoint into sublinked-lists.
    """
    if linked_list is None or linked_list.head is None:
        left_half = linked_list
        right_half = None
        
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
        
        mid_node = linked_list.node_at_index(mid-1)
        
        left_half = linked_list
        right_half = LinkedList()
        
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half
        
def merge_linked(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new, merhed list
    """
    
    # Create a new linked list that contains nodes form
    # merging left and right
    
    merged = LinkedList()
    
    # Add a face head that is discarded later
    merged.add(0)
    
    # Set current to the head of the linked list
    current = merged.head
        
        
    # obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head
    
    # Iterate over left and right until we reach the tail node 
    # of eiher
    
    while left_head or right_head:
        # if the head node of left is None, we'r past the tail
        # Add the node from right to merge linked list
        if left_head is None:
            current.next_node = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next_node
            
        # If the head node of right is None, we'r past the tail
        # Add the tail node from left to merge linked list
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next_node
        else:
            # Not at either tail node
            # Obtain node data to perform comparision operations
            left_data = left_head.data
            right_data = right_head.data
            
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                # Move left head to next node
                left_head = left_head.next_node
            # If data on left is greater than right, set current to right node
            else:
                current.next_node = right_head
                # Move right head to next node
                right_head = right_head.next_node
        # Move current to next node
        current = current.next_node
    
    # Discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    
    return merged


if __name__ == "__main__":
    unsortedLinkedList = LinkedList()
    x = [4, 2, 6, 1, 7, 8, 10, 9, 3, 5]
    for i in x:
        unsortedLinkedList.add(i)
    print(f"unsorted linked list--> {unsortedLinkedList}")
    sortedLinkedList = merge_sort_linked_list(unsortedLinkedList)
    print(f"sorted linked list--> {sortedLinkedList}")
