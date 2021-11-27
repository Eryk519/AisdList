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

    def display(self):
        if self.head is None:
            print("Linked list is Empty")
        else:
            temp_Node = self.head
            while temp_Node is not None:
                print(temp_Node.value, '->' , end=" ")
                temp_Node = temp_Node.next

    def len(self):
        temp_Node = self.head
        total = 0
        while temp_Node is not None:
            total += 1
            temp_Node = temp_Node.next
        return total

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
            self.head = temp_Node.next
            temp_Node.next = None

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

list_ = LinkedList()
list_.push(1)
list_.push(0)
print(list_.len())
list_.append(9)
list_.append(10)
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
first_element = list_.node(at=0)
returned_first_element = list_.pop()
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
second_node = list_.node(at=1)
list_.remove(second_node)
list_.display()
print()

class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def push(self, element):
        self._storage.append(element)

    def pop(self):
        return self._storage.remove_last()

    def len(self):
        return self._storage.len()

    def display(self):
        return self._storage.display()

stack = Stack()
stack.push(3)
stack.push(10)
top_value = stack.pop()
stack.display()
print()

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

    def len(self):
        return self._storage.len()

    def display(self):
        return self._storage.display()

queue = Queue()
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
client_first = queue.dequeue()
queue.display()