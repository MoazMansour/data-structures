#!/usr/bin/env python3

'''Hashed table class using lists and open addressing'''

class HashTable():
    def __init__(self, size=3, n=0):
        '''initate a hash table with an empty list'''
        self.items = n
        self.size = size
        self.table = [None] * self.size

    def hashKey(self, key):
        '''hash the key to a certain location in the list'''
        hashedKey = hash(key)
        index = hashedKey % self.size
        return index

    def addValue(self, key, value):
        '''add key, value pair to table'''
        self.items += 1
        loadfactor = float(self.items)/float(self.size)
        if loadfactor >= 0.5:
            self.table, self.size = self.doubleTable()
        keyPair = self.findKeyPair(key)
        index = self.hashKey(keyPair)
        self.table[index] = (key, value)


    def exists(self, key):
        '''lookup if a certain key exists'''
        keyPair = self.findKeyPair(key)
        index = self.hashKey(keyPair)
        if self.table[index]:
            return True
        return False

    def getKey(self, keyPair):
        '''return the value of a key'''
        index = self.hashKey(keyPair)
        return self.table[index]

    def remove(self, key):
        '''delete a key, value pair'''
        keyPair = self.findKeyPair(key)
        index = self.hashKey(keyPair)
        self.table[index] = None

    def findKeyPair(self, key):
        '''returns the keyPair available for the given key'''
        i = 1
        keyPair = (key, i)
        pos = self.getKey(keyPair)
        while pos:
            if pos[0] == key:
                break
            else:
                i += 1
                keyPair = (key, i)
                pos = self.getKey(keyPair)
        return keyPair

    def doubleTable(self):
        '''doubles the table it reachs 0.5 load factor'''
        new_table = HashTable(self.size*2)
        for element in self.table:
            if element:
                new_table.addValue(element[0], element[1])
        return new_table.table, new_table.size

    def get(self, key):
        keyPair = self.findKeyPair(key)
        index = self.hashKey(keyPair)
        return self.table[index][1]


def main():
    t = HashTable()
    t.addValue('Moaz',100)
    t.addValue('Jubran',200)
    print(t.size)
    print(t.exists('Moaz'))
    print(t.exists('Mai'))
    print(t.exists('Jubran'))
    t.remove('Moaz')
    print(t.exists('Moaz'))
    print(t.get('Jubran'))

if __name__ == '__main__':
    main()
