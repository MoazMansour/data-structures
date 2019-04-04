#!/usr/bin/env python3

'''Python LinkedList'''

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None


class SLinkedList():
    def __init__(self, head=None):
        self.head = head


    def pushFront(self, value):
        '''Adds a new value to the front'''
        new_node = Node(value)
        current = self.head
        new_node.next = current
        self.head = new_node


    def popFront(self):
        '''Delete the first element and return its value'''
        if self.empty():
            return None
        current = self.head
        value = current.value
        self.head = current.next
        return value


    def size(self):
        '''Return the size of the list'''
        leng = 0
        if self.head:
            current = self.head
            leng += 1
            while current.next:
                current = current.next
                leng += 1
        return leng


    def empty(self):
        '''Return true if list is empty'''
        if not self.head:
            return True
        return False


    def valueAt(self, index):
        '''Return value at a certain index starting by 0'''
        if index < 0:
            return self.value_n_from_end(index)
        element = self.getElement(index)[0]
        if element:
            return element.value
        return None


    def pushBack(self, value):
        '''Adds a value to the end of the list'''
        new_node = Node(value)
        if self.empty():
            self.head = new_node
            return
        current = self.getLast()
        current.next = new_node
        return


    def popBack(self):
        '''Remove the very last element and return its value'''
        if self.empty():
            return None
        current = self.head
        previous = None
        while current.next:
            previous = current
            current = current.next
        value = current.value
        if previous:
            previous.next = None
        else:
            self.head = None
        return value


    def getLast(self):
        '''Get the last element helper function'''
        current = self.head
        while current.next:
            current = current.next
        return current


    def getElement(self, index):
        '''Helper function Return the elemnt at a cetain index'''
        if self.empty():
            return None, None
        i = 0
        previous = None
        current = self.head
        if index == 0:
            return current, previous
        while current.next:
            i += 1
            previous = current
            current = current.next
            if i == index:
                return current, previous
        if i == index-1:
            return None, previous
        else:
            return None, None


    def front(self):
        '''return value of the first item'''
        if self.head:
            return self.head.value
        return None


    def back(self):
        '''return the value of the last item'''
        if self.empty():
            return None
        current = self.getLast()
        return current.value


    def insert(self,
        index, value):
        ''' insert a value at the pointed index and push the rest '''
        new_element = Node(value)
        if index == 0:
            new_element.next = self.head
            self.head = new_element
            return
        previous = self.getElement(index)[1]
        if previous:
            new_element.next = previous.next
            previous.next = new_element
        return

    def erase(self, index):
        ''' erases the element at this index'''
        current, previous = self.getElement(index)
        # Checks if element exists
        if current:
            # Checks if there is a previous
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
        return


    def value_n_from_end(self, n):
        '''find value of nth element from back'''
        listLen = self.size()
        index = listLen + n
        if index < 0:
            return None
        return self.valueAt(index)


    def reverse(self):
        '''reverses the list'''
        if self.empty():
            return
        rList = SLinkedList()
        while self.head:
            rList.pushBack(self.popBack())
        self.head = rList.head

    def removeValue(self, value):
        '''remove the first instance of this value'''
        index = 0
        if self.head:
            current = self.head
            flag = (current.value != value)
            while flag and current.next:
                index += 1
                current = current.next
                flag = (current.value != value)
            if flag:
                return
            self.erase(index)


def main():
    '''Test LinkedList'''
    e1 = Node(1)
    llist = SLinkedList(e1)
    llist.pushBack(2)
    llist.pushBack(3)
    llist.pushBack(4)
    print(llist.front())
    print(llist.back())
    print('size: %s' % llist.size())
    llist.reverse()
    print(llist.front())
    print(llist.back())
    print('size: %s' % llist.size())
    llist.removeValue(2)
    print('size: %s' % llist.size())

if __name__ == '__main__':
    main()
