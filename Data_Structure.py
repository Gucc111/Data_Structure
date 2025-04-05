class SequentialList:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.elements = [0] * self.capacity

    def is_empty(self):
        return self.size == 0

    def _resize(self):
        self.capacity = self.capacity * 2
        new_elements = [0] * self.capacity
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements

    def insert(self, idx, val):
        if idx > self.size or idx < 0:
            raise ValueError('Invalid Index')
        
        if self.size == self.capacity:
            self._resize()
        
        curr = self.size - 1
        while curr > idx:
            self.elements[curr+1] = self.elements[curr]
            curr -= 1
        self.elements[idx] = val

        self.size += 1

    def remove(self, idx):
        if idx < 0 or idx > self.size - 1:
            raise ValueError('Invalid Index')
        
        while idx < self.size - 1:
            self.elements[idx] = self.elements[idx+1]
            idx += 1
        
        self.size -= 1

    def find(self, val):
        for i, j in enumerate(self.elements[:self.size]):
            if j == val:
                return i
        return -1

    def modify(self, idx, val):
        if idx < 0 or idx > self.size - 1:
            raise ValueError('Invalid Index')
        self.elements[idx] = val

    def __getitem__(self, idx):
        if idx < 0 or idx > self.size - 1:
            raise ValueError('Invalid Index')
        return self.elements[idx]

    def __len__(self):
        return self.size
    
    def __repr__(self):
        return f'Sequential List: {self.elements[:self.size]}'

    def __iter__(self):
        return iter(self.elements[:self.size])

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val} -> {self.next}'

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def insert(self, idx, val):
        if idx < 0 or idx > self.len:
            raise ValueError('Invalid Index')
        
        self.len += 1
        node = ListNode(val)

        if idx == 0:
            node.next = self.head
            self.head = node
        else:
            n = 0
            curr = self.head
            while n < idx - 1:
                curr = curr.next
                n += 1
            node.next = curr.next
            curr.next = node

    def __len__(self):
        return self.len

    def __repr__(self):
        curr = self.head

def test():
    a = LinkedList()
    a.insert(0, 1)
    a.insert(0, 2)
    a.insert(2, 3)
    print(len(a))
    print(a.head)

if __name__ == '__main__':
    test()