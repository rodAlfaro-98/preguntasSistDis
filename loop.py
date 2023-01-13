from list import LinkedList
from list import Node

list = LinkedList()
list.addNextNode(Node(20))
list.addNextNode(Node(4))
list.addNextNode(Node(15))
list.addNextNode(Node(20))


if(list.detectLoop()):
    print("Loop Found")
else:
    print("No Loop ")