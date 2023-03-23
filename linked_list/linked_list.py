class Node:
    def __init__(self, value=0, next_=None):
        self.value = value
        self.next_ = next_

    def __str__(self) -> str:
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next_ = new_node
        self.tail = new_node

    def insert(self, index, value):
        new_node = Node(value)
        prev_node = self.__get_node(index - 1)
        new_node.next_ = prev_node.next_
        prev_node.next_ = new_node

    def remove(self, index):
        prev_node = self.__get_node(index - 1)
        next_node = self.__get_node(index + 1)
        prev_node.next_ = next_node

    def __get_node(self, index):
        if index < 0:
            raise IndexError
        if not self.head:
            return None
        node = self.head
        for _ in range(index):
            node = node.next_
        return node

    def get(self, index):
        return self.__get_node(index).value

    def __str__(self) -> str:
        node = self.head
        values = node.value
        while node.next_:
            node = node.next_
            values = str(values) + ", " + str(node)
        return "[" + values + "]"


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll)
ll.insert(index=2, value=9)
print(ll)
ll.append(5)
print(ll)
ll.remove(3)
print(ll)
