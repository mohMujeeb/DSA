class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


node1 = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end="->")
    currentNode = currentNode.next
print("null")