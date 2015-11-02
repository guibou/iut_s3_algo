import time
import sys

import tree.avlQuick
import tree.avlSlow
import tree.simple
import tree.avlGeneric
import hash.simpleHash

method = sys.argv[1]
n = int(sys.argv[2])

arbre = {
    'avlQuick': tree.avlQuick,
    'simple': tree.simple,
    'avlSlow': tree.avlSlow,
    'avlGeneric': tree.avlGeneric,
    'simpleHash': hash.simpleHash,
    }.get(method)

empty = arbre.empty

if method != 'avlGeneric':
    insert = arbre.insert
    search = arbre.search
else:
    def key(value):
        return value
    
    def insert(tree, value):
        return arbre.insert(tree, value, key)

    def search(tree, value):
        return arbre.search(tree, value, key)

tree = empty()

t = time.time()
for i in range(1, n):
    insert(tree, i)

print("Insertion Time:", time.time() - t)

if 1:
    t = time.time()
    for i in range(100000):
        search(tree, i)

    print("Search time:", time.time() - t)
