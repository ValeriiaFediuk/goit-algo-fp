class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def sorted_merge(self, list1, list2):
        dummy_node = Node()
        tail = dummy_node

        while True:
            if not list1:
                tail.next = list2
                break
            if not list2:
                tail.next = list1
                break

            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        return dummy_node.next

llist1 = LinkedList()
llist1.append(1)
llist1.append(3)
llist1.append(5)

llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(6)

print("Перший список:")
llist1.print_list()

print("Другий список:")
llist2.print_list()

merged_list = LinkedList()
merged_list.head = merged_list.sorted_merge(llist1.head, llist2.head)
print("Об'єднаний відсортований список:")
merged_list.print_list()

print("Реверсований список:")
merged_list.reverse()
merged_list.print_list()
