from list import LinkedList
from list import Node

def invertirLista(lista: LinkedList())->LinkedList:
    iterator = lista.head
    values = []
    while(iterator != None):
        values.append(iterator.data)
        iterator = iterator.next
    
    lista_rev = LinkedList()
    for i in reversed(range(0,lista.getSize())):
        lista_rev.addNextNode(Node(values[i]))
    return lista_rev

lista = LinkedList()
values = [1,3,6,2,1,4]
for i in values:
    lista.addNextNode(Node(i))

print(lista)
print("Invirtiendo lista")
print(invertirLista(lista))
