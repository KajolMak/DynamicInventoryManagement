from hash_table import HashTable
from bbst import AVLTree
from priority_queue import PriorityQueue

# Demonstrate hash table
ht = HashTable(10)
ht.insert("item1", {"name": "Laptop", "stock": 5})
print("Hash Table Lookup:", ht.lookup("item1"))

# Demonstrate BBST
avl = AVLTree()
avl.insert(None, 50)  # Root insertion
print("AVL Tree Root:", avl.root.key)

# Demonstrate Priority Queue
pq = PriorityQueue()
pq.push(("item1", 5))  # (item_name, priority)
print("Highest Priority Item:", pq.pop())

