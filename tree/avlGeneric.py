class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
        self.hauteurG = 0
        self.hauteurD = 0

    def __str__(self):
        return "Tree(%s (%d, %d), %s, %s)" % (self.value, self.hauteurG, self.hauteurD, self.left, self.right)


def insert(tree, value, key):
    if key(value) < key(tree.value):
        if tree.left == None:
            tree.left = Tree(value, None, None)
            tree.hauteurG = 1
        else:
            insert(tree.left, value, key)
            tree.hauteurG = 1 + max(tree.left.hauteurG,
                                    tree.left.hauteurD)
    else:
        if tree.right == None:
            tree.right = Tree(value, None, None)
            tree.hauteurD = 1
        else:
            insert(tree.right, value, key)
            tree.hauteurD = 1 + max(tree.right.hauteurG,
                                    tree.right.hauteurD)

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
    return tree.hauteurG - tree.hauteurD

def rotate_right(tree):
    tf = tree.left
    (tree.value, tree.left, tree.right,
            tf.value, tf.left, tf.right,
            ) = \
    (tf.value, tf.left, tf,
            tree.value, tf.right, tree.right)

    tr = tree.right
    tr.hauteurD = hauteur_subtree(tr.right)
    tr.hauteurG = hauteur_subtree(tr.left)
    
    tree.hauteurD = hauteur_subtree(tree.right)
    tree.hauteurG = hauteur_subtree(tree.left)

    return tree

def hauteur_subtree(t):
    if t == None:
        return 0
    return max(t.hauteurG, t.hauteurD) + 1

def rotate_left(tree):
    tf = tree.right
    (tree.value, tree.right, tree.left,
            tf.value, tf.right, tf.left,
            ) = \
    (tf.value, tf.right, tf,
            tree.value, tf.left, tree.left)

    tr = tree.left
    tr.hauteurG = hauteur_subtree(tr.left)
    tr.hauteurD = hauteur_subtree(tr.right)
    
    tree.hauteurG = hauteur_subtree(tree.left)
    tree.hauteurD = hauteur_subtree(tree.right)

    return tree

def search(tree, value, key):
    if tree == None:
        return None

    if key(tree.value) == key(value):
        return tree.value

    if key(value) < key(tree.value):
        return search(tree.left, value, key)

    return search(tree.right, value, key)
