## DO NOT EDIT THIS CLASS
class Node: 
    # A binary search tree node class in Python3
    def __init__(self, n): 
        self.key = n # Set the key to number n
        self.left = None # Currently left child is a leaf denoted by None 
        self.right = None # right child is a leaf denoted by None
        
    def addLeftSubtree(self, lNode): # Replace the left child with lNode
        self.left = lNode
        
    def addRightSubtree(self, rNode): # Replace the right child with rNode
        self.right = rNode
        
    def addSubtree(self, lNode, rNode): # Add both left and right nodes
        self.addLeftSubtree(lNode)
        self.addRightSubtree(rNode)
## END-DO NOT EDIT
        
## Your answer here (expected length: 12 lines)
def Binary_Tree_Height(rootNode):
     if rootNode == None:
        return -1
     else:
        return 1 + max(Binary_Tree_Height(rootNode.right),Binary_Tree_Height(rootNode.left))

def S(h):
    if h == 0:
        return 0
    return 2 * S(h-1) + h

def Height_summation(rootNode):
    if rootNode == None:
        return 0
    if (rootNode.left == None) & (rootNode.right == None):
        return 0
    if rootNode.right == None:
        hl = 0
    else:
        hl = Height_summation(rootNode.left)
    if rootNode.right == None:
        hr = 0
    else:
        hr = Height_summation(rootNode.right)
    return hl+hr+max(hl,hr)+1
    
def S_expansion(h):
    sum=0
    counter = 1
    while(h!=0):
        sum = 2 * sum + counter
        counter = counter + 1
        h = h - 1
    return sum
   
## IMPLEMENT YOUR CODE HERE.
## Expected Size 20 lines or less.
def isBinarySearchTree(rootNode):
    if rootNode == None:
        return True
    if not (isBinarySearchTree(rootNode.right) & isBinarySearchTree(rootNode.left)):
        return False
    Left_temp_node = rootNode.left;
    Right_temp_node = rootNode.right;
    while(Left_temp_node != None):
        if Left_temp_node.key > rootNode.key:
            return False
        Left_temp_node=Left_temp_node.right
    while(Right_temp_node != None):
        if Right_temp_node.key < rootNode.key:
            return False
        Right_temp_node=Right_temp_node.left 
    return True
    #raise NotImplementedError()
## END-YOUR CODE HERE

## THIS IS TEST CODE.
#from IPython.core.display import HTML
## TEST CODE: DO NOT EDIT

# Tree number 1

node4 = Node(1)
node5 = Node(-1)
node6 = Node(3)

node4.addSubtree(node5, node6)

node1 = Node(20)
node1.addLeftSubtree(node4)

node2 = Node(30)
node3 = Node(40)
node2.addLeftSubtree(node1)
node2.addRightSubtree(node3)

rootNode1 = node2


# Tree number 2

node1 = Node(15)
node2 = Node(54)
node3 = Node(45)
node3.addSubtree(node2, node1)
node4 = Node(115)
node5 = Node(94)
node5.addSubtree(node3, node4)
node6 = Node(18)
node7 = Node(23)
node9 = Node(20)
node9.addSubtree(node6, node7)

rootNode2 = Node(55)
rootNode2.addSubtree(node9, node5)

# Tree number 3

rootNode3 = Node(20)

# Tree number 4

node11 = Node(18)
node12 = Node(26)
node13 = Node(12)
node14 = Node(29)

node11.addSubtree(None, node12)
node12.addSubtree(node13, node14)

rootNode4 = node11



try:
    assert isBinarySearchTree(rootNode1), 'Test 1 Failed: expected answer True, your answer False'
    print('Test 1 Passed!')
    assert not isBinarySearchTree(rootNode2), 'Test 2 Failed: expected answer False, your answer True'
    print('Test 2 Passed!')
    assert isBinarySearchTree(rootNode3), 'Test 3 Failed: expected answer True, your answer False'
    print('Test 3 Passed!')
    assert not isBinarySearchTree(rootNode4), 'Test 3 Failed: expected answer False, your answer True'
    print('Test 4 Passed!')
    
except NotImplementedError:
    print('Nothing Implemented Yet. ')

## END-DO NOT EDIT
