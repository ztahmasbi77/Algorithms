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
    n.key = n.key + 1
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

#Tree number 5
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)
F = Node(6)
G = Node(7)
B.addSubtree(A, C)
F.addSubtree(E, G)
D.addSubtree(B, F)
A1 = Node(11)
B1 = Node(21)
C1 = Node(31)
D1 = Node(41)
E1 = Node(51)
F1 = Node(61)
G1 = Node(71)
B1.addSubtree(A1, C1)
F1.addSubtree(E1, G1)
D1.addSubtree(B1, F1)
A2 = Node(111)
B2 = Node(121)
C2 = Node(131)
D2 = Node(141)
E2 = Node(151)
F2 = Node(161)
G2 = Node(171)
B2.addSubtree(A2, C2)
F2.addSubtree(E2, G2)
D2.addSubtree(B2, F2)
A3 = Node(211)
B3 = Node(221)
C3 = Node(231)
D3 = Node(241)
E3 = Node(251)
F3 = Node(261)
G3 = Node(271)
B3.addSubtree(A3, C3)
F3.addSubtree(E3, G3)
D3.addSubtree(B3, F3)
K = Node(10)
L = Node(200)
M = Node(100)
K.addSubtree(D, D1)
L.addSubtree(D2, D3)
M.addSubtree(K, L)

n= Node(0)

try:
    assert isBinarySearchTree(rootNode1), 'Test 1 Failed: expected answer True, your answer False'
    print('Test 1 Passed!')
    assert not isBinarySearchTree(rootNode2), 'Test 2 Failed: expected answer False, your answer True'
    print('Test 2 Passed!')
    assert isBinarySearchTree(rootNode3), 'Test 3 Failed: expected answer True, your answer False'
    print('Test 3 Passed!')
    assert not isBinarySearchTree(rootNode4), 'Test 3 Failed: expected answer False, your answer True'
    print('Test 4 Passed!')
    print(Binary_Tree_Height(rootNode1))
    print(Height_summation(rootNode1))
    print(n.key,"\n")
    n.key=0
    print(Binary_Tree_Height(rootNode2))
    print(Height_summation(rootNode2))
    print(n.key,"\n")
    n.key=0
    print(Binary_Tree_Height(rootNode3))
    print(Height_summation(rootNode3))
    print(n.key,"\n")
    n.key=0
    print(Binary_Tree_Height(rootNode4))
    print(Height_summation(rootNode4))
    print(n.key,"\n")
    n.key=0
    print(Binary_Tree_Height(D))
    print(Height_summation(D))
    print(n.key,"\n")
    n.key=0
    print(Binary_Tree_Height(K))
    print(Height_summation(K))
    print(n.key,"\n")
    n.key=0
    print(Binary_Tree_Height(M))
    print(Height_summation(M))
    print(n.key,"\n")
    n.key=0
    print(Binary_Tree_Height(B))
    print(Height_summation(B))
    print(n.key,"\n")
    n.key=0
except NotImplementedError:
    print('Nothing Implemented Yet. ')

## END-DO NOT EDIT
