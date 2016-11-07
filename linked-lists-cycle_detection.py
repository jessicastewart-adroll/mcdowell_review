class Node(object):
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    visited_nodes = []
    if head.data == None:
        return False

    visited_nodes.append(head)

    current = head.next
    while current:
        if current in visited_nodes:
            return True
        else:
            visited_nodes.append(current)
            current = current.next

    return False


case_one = Node(1)
case_two = Node(1)
case_two_2 = Node(2)
case_two_3 = Node(3)

case_two_3.next = case_two_2
case_two_2.next = case_two_3
case_two.next = case_two_2

print(has_cycle(case_one))
print(has_cycle(case_two))
