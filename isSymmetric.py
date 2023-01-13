from tree import Tree

def isSymmetric(tree: Tree)->bool:
    elems = tree.getElements()
    half = round(len(elems)/2)
    if(elems[0:half-1] == elems[half:len(elems)]):
        return True
    else:
        return False

tree = Tree(1)
tree.addNode(Tree(2),[0])
tree.addNode(Tree(2),[1])
tree.addNode(Tree(3),[0,0])
tree.addNode(Tree(3),[1,0])
tree.addNode(Tree(4),[0,1])
tree.addNode(Tree(4),[1,1])

print(isSymmetric(tree))