class HashTable:
    def __init__(self, size):
        """Initialize the hash table with a fixed size."""
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        """
        Simple hash function to calculate the index for a given key.
        Converts the key into an integer index within the range of the table size.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert a key-value pair into the hash table.
        Handles collisions using separate chaining with linked lists.
        """
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        # Check for key existence and update if found
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # Add the new key-value pair
        self.table[index].append((key, value))

    def lookup(self, key):
        """
        Retrieve the value associated with a given key in the hash table.
        Returns None if the key does not exist.
        """
        index = self._hash_function(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        raise KeyError(f"Key '{key}' not found in hash table.")

    def delete(self, key):
        """
        Remove a key-value pair from the hash table.
        Raises an error if the key does not exist.
        """
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return
        raise KeyError(f"Key '{key}' not found in hash table.")

    def display(self):
        """Display the current state of the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket if bucket else 'Empty'}")

