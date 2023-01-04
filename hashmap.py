'''HashMap ADT'''

class HashMap:
    '''HashMap ADT'''
    def __init__(self):
        '''Create object'''
        self.buckets = 7
        self.map = [[] for x in range(self.buckets)]

    def get(self, key):
        '''Return the value if key is in the dictionary. If key is not in raise a KeyError.'''
        keys = self.keys()
        if key in keys:
            step = self.map[self.index(key)]
            for i in step:
                if i[0] == key:
                    return i[1]
        raise KeyError

    def set(self, key, value):
        '''add the (key,value) pair to the hashMap. if the loadfactor >= 80%, rehash the map'''
        keys = self.keys()
        if key in keys:
            self.remove(key)
        index = self.index(key)
        self.map[index].append((key, value))
        n = self.size()
        f = n/self.buckets
        if f >= .8:
            for i in range(self.buckets):
                self.map.append([])
            self.buckets = (self.buckets*2) -1

    def remove(self, key):
        '''Remove the key and its associated value from the map. If the key
        does not exist, nothing happens. Do not rehash the table after deleting keys.'''
        keys = self.keys()
        if key in keys:
            self.map[self.index(key)].pop()

    def clear(self):
        '''Clear all buckets'''
        self.buckets = 7
        self.map = self.map = [[] for x in range(self.buckets)]

    def capacity(self):
        '''Return the current capacity--number of buckets--in the map.'''
        return self.buckets

    def size(self):
        '''Return the number of key-value pairs in the map.'''
        count = len(self.keys())
        return count

    def keys(self):
        '''Return a list of keys.'''
        lyst = []
        for value in self.map:
            if value:
                for i in value:
                    lyst.append(i[0])

        return lyst

    def index(self, key):
        '''Create and index for hashmap'''
        val = 0
        for item in key:
            item = str(item)
            val += ord(item[0])

        val = val%100
        if val >= self.buckets:
            val = self.buckets - 1
        return val
