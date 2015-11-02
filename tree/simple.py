class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Tree(%s, %s, %s)" % (self.value, self.left, self.right)

def insert(tree, value):
    if value < tree.value:
        if tree.left == None:
            tree.left = Tree(value, None, None)
        else:
            insert(tree.left, value)
    else:
        if tree.right == None:
            tree.right = Tree(value, None, None)
        else:
            insert(tree.right, value)
    
def hauteur(tree):
    if tree == None:
        return 0
    else:
        return max(hauteur(tree.left), hauteur(tree.right)) + 1

def search(tree, value):
    if tree == None:
        return False
    if tree.value == value:
        return True

    if value < tree.value:
        return search(tree.left, value)

    return search(tree.right, value)
