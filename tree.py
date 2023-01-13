class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key
    
    def addNode(self,tree,order):
        if(order[0] == 0 and self.left != None):
            self.left.addNode(tree,order[1:])
        elif(order[0] == 1 and self.right != None):
            self.right.addNode(tree,order[1:])
        elif(order[0] == 0):
            self.left = tree
        else:
            self.right = tree

    def getElements(self):
        toReturn = []
        if(self.left == None):
            return [self.data]
        else:
            toReturn += self.left.getElements()
        toReturn += [self.data]
        if(self.right == None):
            return [self.data]
        else:
            toReturn += self.right.getElements()
        return toReturn
