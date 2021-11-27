from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node = Node(value)
            new_Node.next = self.head
            self.head = new_Node

    def append(self, value):
        new_Node = Node(value)
        if self.head is None:
            self.head = new_Node
            self.tail = new_Node
        else:
            temp_Node = self.head
            while temp_Node.next:
                temp_Node = temp_Node.next
            temp_Node.next = new_Node
            self.tail = new_Node

    def insert(self, value, after):
        if self.head is None:
            print("Linked list is empty")
        new_Node = Node(value)
        if after == self.tail:
            after.next = new_Node
            self.tail = new_Node
        new_Node.next = after.next
        after.next = new_Node

    def node(self, at):
        if self.head is None:
            print("Linked list is empty")
            return None
        else:
            temp_Node = self.head
            for i in range(at):
                temp_Node=temp_Node.next
            return temp_Node

    def pop(self):
        if self.head is None:
            print("Linked list is empty")
            return None
        else:
            temp_Node = self.head
            self.head = self.head.next
            return temp_Node.value

    def remove_last(self):
        if self.head is None:
            print("Linked list is empty")
            return None
        temp_Node = self.head
        while temp_Node.next is not None:
            if temp_Node.next == self.tail:
                temp_Value = temp_Node.next.value
                temp_Node.next = None
                self.tail = temp_Node
                return temp_Value
            temp_Node = temp_Node.next

    def remove(self, after):
        if after is None:
            print("Linked list is empty")
            return None
        else:
            self.tail = after
            after.next = None

    def __str__(self):
        temp_Node = self.head
        word = ''
        while temp_Node is not None:
            word += str(temp_Node.value)
            if temp_Node != self.tail:
                word += ' -> '
            temp_Node = temp_Node.next
        return word

    def __len__(self):
        temp_Node = self.head
        total = 0
        while temp_Node is not None:
            total += 1
            temp_Node = temp_Node.next
        return total


list_ = LinkedList()
assert list_.head == None
list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

print(list_)
print(len(list_))


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def push(self, element):
        self._storage.append(element)

    def pop(self):
        return self._storage.remove_last()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        word = ''
        temp_Node = self._storage.head
        while temp_Node is not None:
            word += (str(temp_Node.value) + ' , ')
            temp_Node = temp_Node.next
        return word


stack = Stack()
assert len(stack) == 0
stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2

print(stack)
print(len(stack))
print(stack.pop())


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def peek(self):
        return self._storage.head.value

    def enqueue(self, element):
        self._storage.append(element)

    def dequeue(self):
        return self._storage.pop()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        word = ''
        temp_Node = self._storage.head
        while temp_Node is not None:
            word += str(temp_Node.value)
            if temp_Node.next is not None:
                word += ", "
            temp_Node = temp_Node.next
        return word

queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'
print(queue.peek())
client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2

print(len(queue))
print(queue.peek())