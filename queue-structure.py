#!/usr/bin/env python3

'''Python Queue Structure'''

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue():
    def __init__(self, head=None):
        '''initialize a list with empty head and tail'''
        self.head = head
        self.tail = head


    def enqueue(self, value):
        '''adds value to the end of the list'''
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode


    def dequeue(self):
        '''remove value from the head of the list and return it'''
        value = self.head.value
        self.head = self.head.next
        return value


    def empty(self):
        '''return True if list os empty'''
        if self.head:
            return False
        return True


def main():
    '''Test queue'''
    e1 = Node(1)
    q = Queue(e1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.empty())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.empty())

if __name__ == '__main__':
    main()
