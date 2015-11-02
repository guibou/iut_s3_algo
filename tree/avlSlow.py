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

    eq = equilibre(tree)
    if eq > 1:
        if equilibre(tree.left) < 0:
            rotate_left(tree.left)

        rotate_right(tree)

    elif eq < -1:
        if equilibre(tree.right) > 0:
            rotate_right(tree.right)

        rotate_left(tree)
    
def hauteur(tree):
    if tree == None:
        return 0
    else:
        return max(hauteur(tree.left), hauteur(tree.right)) + 1

def equilibre(tree):
    return hauteur(tree.left) - hauteur(tree.right)

def rotate_right(tree):
    tf = tree.left
    (tree.value, tree.left, tree.right,
            tf.value, tf.left, tf.right,
            ) = \
    (tf.value, tf.left, tf,
            tree.value, tf.right, tree.right)

    tr = tree.right

    return tree

def rotate_left(tree):
    tf = tree.right
    (tree.value, tree.right, tree.left,
            tf.value, tf.right, tf.left,
            ) = \
    (tf.value, tf.right, tf,
            tree.value, tf.left, tree.left)

    return tree

def search(tree, value):
    if tree == None:
        return False
    if tree.value == value:
        return True

    if value < tree.value:
        return search(tree.left, value)

    return search(tree.right, value)
