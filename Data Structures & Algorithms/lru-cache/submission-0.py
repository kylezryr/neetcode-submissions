class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.elements = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.elements:
            return -1
        
        node = self.elements.get(key)
        self.remove(node)
        self.insertAtTail(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.elements:
            node = self.elements.get(key)
            node.value = value
            self.remove(node)
            self.insertAtTail(node)
            return 

        if len(self.elements) == self.capacity:
            nodeToRemove = self.head.next
            self.remove(nodeToRemove)
            self.elements.pop(nodeToRemove.key)
        
        newNode = Node(key, value)
        self.insertAtTail(newNode)
        self.elements[key] = newNode

    def remove(self, node: Node) -> None:
        if node == None:
             return

        oldNext = node.next
        oldPrev = node.prev
        if node.prev != None:
            node.prev.next = oldNext
        if node.next != None:
            node.next.prev = oldPrev

    def insertAtTail(self, node: Node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
