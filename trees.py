class BinaryTree():
    def __init__(self,data):
      self.left = None
      self.right = None
      self.data = data

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.data
                       
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left
    
    def inOrderTraversal(self): #in order left, root, right
        if self is not None:
            if self.getLeftChild() is not None:
                self.getLeftChild().inOrderTraversal()
            print(self.getNodeValue())
            if self.getRightChild() is not None:
                self.getRightChild().inOrderTraversal()

    def insertBST(self, data):
        if data > self.data:
            if self.right:
                self.right.insertBST(data)
            else:
                newNode =  BinaryTree(data)
                self.right = newNode
        else:
            if self.left:
                self.left.insertBST(data)
            else:
                newNode =  BinaryTree(data)
                self.left =newNode
                
# test BST tree
myTree = BinaryTree("9")
myTree.insertBST("3")
myTree.insertBST("1")
myTree.insertBST("5")
myTree.inOrderTraversal()
