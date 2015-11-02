import time
import sys

import avlQuick
import avlSlow
import simple
import avlGeneric

method = sys.argv[1]
n = int(sys.argv[2])

arbre = {
    'avlQuick': avlQuick,
    'simple': simple,
    'avlSlow': avlSlow,
    'avlGeneric': avlGeneric,
    }.get(method)

hauteur = arbre.hauteur

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

tree = arbre.Tree(0, None, None)

t = time.time()
for i in range(1, n):
    insert(tree, i)

print("Insertion Time:", time.time() - t)
print(hauteur(tree))

if 1:
    t = time.time()
    for i in range(100000):
        search(tree, i)

    print("Search time:", time.time() - t)
