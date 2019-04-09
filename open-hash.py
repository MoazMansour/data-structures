#!/usr/bin/env python3

'''Hashed table class using lists and open addressing'''

class HashTable():
    def __init__(self):
        '''initate a hash table with an empty list'''
        self.size = 7
        self.table = [None] * self.size

    def hashKey(self, key):
        '''hash the key to a certain location in the list'''
        hashedKey = hash(key)
        index = hashedKey % self.size
        return index

    def addValue(self, key, value):
        '''add key, value pair to table'''
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
