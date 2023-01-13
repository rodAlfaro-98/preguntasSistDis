class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addNextNode(self,node):
        if(self.head == None):
            self.head = node
        else:
            iterator = self.head
            while(iterator.next != None):
                iterator = iterator.next
            iterator.next = node

    def __str__(self):
        values = []
        iterator = self.head
        while(iterator != None):
            values.append(iterator.data)
            iterator = iterator.next
        string = ""
        for i in values:
            string += str(i)+"->"
        return string

    def getSize(self):
        i = 0
        iterator = self.head
        while(iterator != None):
            i+=1
            iterator = iterator.next
        return i

    def detectLoop(self):
        iterator = self.head
        nodes = []
        while(iterator.next != None):
            if(iterator in nodes):
                return True
            nodes.append(iterator)
            iterator = iterator.next
        return False