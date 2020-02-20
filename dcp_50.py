#Given February 16, 2020

#Suppose an arithmetic expression is given as a binary tree.
#Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

#Given the root to such a tree, write a function to evaluate it.
#For example, given the following tree:

#    *
#   / \
#  +    +
# / \  / \
#3  2  4  5

#You should return 45, as it is (3 + 2) * (4 + 5).


#ArithmeticExpression is a tree containing an arithmetic expression
class ArithmeticExpression:
    def __init__(self, value : str, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        def parse(node):
            if node.isLeaf():
                return node.value
            
            else:
                return '(' + parse(node.left) + ' ' + node.value + ' ' + parse(node.right) + ')'

        #this string slice allows us to get rid of the outermost set of parentheses
        return parse(self)[1:-1]
                
    #this makes the base case less verbose
    def isLeaf(self):
        #leaf nodes are defined as numbers...
        return self.left == None and self.right == None

    #these two helpers helps us make trees without creating really long expressions
    def attachLeftChild(self, node):
        self.left = node

    def attachRightChild(self, node):
        self.right = node
    
    
if __name__ == '__main__':
    #this allows us to use AE as another name for ArithmeticExpression since otherwise, it would be too long to use...
    AE = ArithmeticExpression
    a = AE('+', AE('2'), AE('3'))
    print(a, '| 2 + 3')

    b = AE('+')
    b.attachLeftChild(AE('+', AE('2'), AE('7')))
    b.attachRightChild(AE('5'))
    print(b, '| (2 + 7) + 5')

    c = AE('*', AE('7'))
    c.attachRightChild(AE('/', AE('-', AE('*', AE('5'), AE('9')), AE('3')), AE('*', AE('8'), AE('7'))))
    
    print(c, '| 7 * (((5 * 9) - 3) / (8 * 7))')
    
    


    
