import sys
max = int(sys.argv[1])

import tree.avlGeneric as t

# This is the key of the dictionary value
def key(value):
    k, v = value
    return k

def keyAnagram(value):
    return ''.join(sorted(value))

groups = t.Tree(("", []), None, None)

with open('/usr/share/dict/french') as f:
    count = 0
    for line in f:
        line = line.strip()

        sWord = keyAnagram(line)

        group = t.search(groups, sWord, key)

        if group == None:
            t.insert(groups, (sWord, [line]), key)
        else:
            group[1].append(line)
        
        count += 1

        if count > max:
            break

def lenDict(tree):
    if tree == None:
        return 0
    else:
        return lenDict(tree.left) + lenDict(tree.right) + 1


print(lenDict(groups), "groupes")
print(t.search(groups, keyAnagram("tortue"), key))
