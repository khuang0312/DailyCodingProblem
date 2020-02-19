#Given January 5, 2020

#A unival tree (which stands for "universal value") is a tree where all
#nodes under it have the same value.

#Given the root to a binary tree, count the number of unival subtrees.

#For example, the following tree has 5 unival subtrees:
#     0
#    / \
#   1   0
#      / \
#     1   0
#    / \
#   1   1


#we should use a breath first search...


def isTreeUnival(tree: Tree) -> bool:
    if not tree.left and not tree.right:
        return true
    elif tree.left.value == tree.right.value:
        return true

def countUnivalSubtrees(tree: Tree) -> int:
    if tree == None:
        return 0
    else:
        nodes = []
        nodes.append(tree)

        while len(nodes) != 0:
            nodes.append(tree.left)
            nodes.append(tree.right)
    
