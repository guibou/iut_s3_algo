def initGrid(size):
    grid = []
    for i in range(size):
        grid.append([])

    return grid

class Hash:
    def __init__(self):
        self.data = initGrid(100)

def insert(self, key):
    h = hash(key) % len(self.data)

    if key not in self.data[h]:
        self.data[h].append(key)

        if len(self.data[h]) > 5:
            rehash(self)

def search(self, key):
    h = hash(key) % len(self.data)

    return key in self.data[h]

def rehash(self):
    newSize = len(self.data) * 2

    newData = initGrid(newSize)

    for conflicts in self.data:
        for key in conflicts:
            h = hash(key) % newSize
            newData[h].append(key)

    self.data = newData

def length(self):
    l = 0
    for c in self.data:
        l += len(c)

    return l

def empty():
    return Hash()
    
if __name__ == '__main__':
    hashSet = Hash()
    insert(hashSet, 0)

    print(search(hashSet, 0))
    print(search(hashSet, 1))
