#!/usr/bin/env python3

'''Hashed table class using lists and open addressing'''

class HashTable():
    def __init__(self):
        '''initate a hash table with an empty list'''
        self.size = 1009
        self.table = [None] * self.size

    def hashKey(self, key):
        '''hash the key to a certain location in the list'''
        hashedKey = hash(key)
        index = hashedKey % self.size
        return index

    def addValue(self, key, value):
        '''add key, value pair to table'''
        index = self.hashKey(key)
        self.table[index] = value

    def exists(self, key):
        '''lookup if a certain key exists'''
        index = self.hashKey(key)
        if self.table[index]:
            return True
        return False

    def getKey(self, key):
        '''return the value of a key'''
        index = self.hashKey(key)
        return self.table[index]

    def remove(self, key):
        '''delete a key, value pair'''
        index = self.hashKey(key)
        self.table[index] = None


def main():
    t = HashTable()
    t.addValue('Moaz',100)
    t.addValue('Jubran',200)
    print(t.exists('Moaz'))
    print(t.exists('Mai'))
    print(t.getKey('Jubran'))
    t.remove('Moaz')
    print(t.exists('Moaz'))

if __name__ == '__main__':
    main()
