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

    def addNode(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

# Create LinkedList and Nodes
node1 = LinkedList()
node1.head = Node(5)
node2 = Node(10)
node3 = Node(15)
node4 = Node(20)

# Connect the nodes
node1.head.next = node2
node2.next = node3
node3.next = node4

# Print original Linked List
print("Original Linked List:")
node1.linkedListPrint()

# Add new node to the front
node1.addNode(25)

# Print updated Linked List
print("\nUpdated Linked List after adding 25 at the beginning:")
node1.linkedListPrint()
