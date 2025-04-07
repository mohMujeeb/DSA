class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def linkedListPrint(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next
node1 = LinkedList()
node1.head = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)


node1.head.next = node2
node2.next = node3
node3.next = node4

print("Linked List:")
print(node1.linkedListPrint)

