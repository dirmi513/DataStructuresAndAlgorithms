"""
Python Implementation of an LRUCache using the following data structures:
    - doubly linked list to keep track of the elements in the order that they are accessed,
    from the last at the tail of the doubly linked list, to the first at the head
    - dictionary to be able to obtain a certain linked list node based on its key value in O(1) time
"""


class DoublyLinkedListNode:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoublyLinkedListNode(-1)
        self.tail = DoublyLinkedListNode(-1)
        self.head.prev = self.tail
        self.tail.next = self.head
        self.keys = {}

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        val = self.keys[key].value
        self.delete_node(key)
        self.add_node(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            self.delete_node(key)
        self.add_node(key, value)
        if len(self.keys) > self.capacity:
            self.delete_node(self.tail.next.key)

    def delete_node(self, key):
        node = self.keys[key]
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
        del self.keys[key]

    def add_node(self, key, val):
        node = DoublyLinkedListNode(key, val)
        prev_head = self.head.prev
        prev_head.next = node
        node.prev = prev_head
        node.next = self.head
        self.head.prev = node
        self.keys[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
