from typing import Iterator, Optional, Any

class SequentialList:
    def __init__(self) -> None:
        self.capacity = 10
        self.size = 0
        self.elements = [0] * self.capacity

    def insert(self, idx: int, val: Any) -> None:
        if idx > self.size or idx < 0:
            raise IndexError(f'Index {idx} is out of range for size {self.size}')
        
        if self.size == self.capacity:
            self._resize()
        
        curr = self.size - 1
        while curr > idx:
            self.elements[curr+1] = self.elements[curr]
            curr -= 1
        self.elements[idx] = val

        self.size += 1

    def remove(self, idx: int) -> None:
        if idx < 0 or idx > self.size - 1:
            raise IndexError(f'Index {idx} is out of range for size {self.size}')
        
        while idx < self.size - 1:
            self.elements[idx] = self.elements[idx+1]
            idx += 1
        
        self.size -= 1

    def find(self, val: Any) -> int:
        for i, j in enumerate(self.elements[:self.size]):
            if j == val:
                return i
        
        return -1

    def modify(self, idx: int, val: Any) -> None:
        if idx < 0 or idx > self.size - 1:
            raise IndexError(f'Index {idx} is out of range for size {self.size}')
        
        self.elements[idx] = val

    def _resize(self) -> None:
        self.capacity = self.capacity * 2
        new_elements = [0] * self.capacity
        
        for i in range(self.size):
            new_elements[i] = self.elements[i]
        self.elements = new_elements

    def is_empty(self) -> bool:
        return self.size == 0
    
    def __repr__(self) -> str:
        return f'Sequential List: {self.elements[:self.size]}'

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator:
        return iter(self.elements[:self.size])

    def __getitem__(self, idx: int) -> Any:
        if idx < 0 or idx > self.size - 1:
            raise IndexError(f'Index {idx} is out of range for size {self.size}')
        
        return self.elements[idx]


class ListNode:
    def __init__(self, val: Any, next: Optional['ListNode'] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f'{self.val} -> {self.next}'


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.len = 0

    def insert(self, idx: int, val: Any) -> None:
        if idx < 0 or idx > self.len:
            raise IndexError(f'Index {idx} is out of range for size {self.len}')
        
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

    def remove(self, idx: int) -> None:
        if idx < 0 or idx > self.len:
            raise IndexError(f'Index {idx} is out of range for size {self.len}')
        
        self.len -= 1
        if idx == 0:
            self.head = self.head.next
        else:
            n = 0
            curr = self.head
            while n < idx - 1:
                curr = curr.next
                n += 1
            curr.next = curr.next.next

    def find(self, val: Any) -> int:
        curr = self.head
        idx = 0
        while curr:
            if curr.val == val:
                return idx
            idx += 1
            curr = curr.next

        return -1

    def modify(self, idx: int, val: Any) -> None:
        self[idx].val = val

    def is_empty(self) -> bool:
        return self.len == 0

    def __repr__(self) -> str:
        return f'{self.head}'

    def __len__(self) -> int:
        return self.len

    def __iter__(self) -> Iterator:
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __getitem__(self, idx: int) -> ListNode:
        if idx < 0 or idx > self.len:
            raise IndexError(f'Index {idx} is out of range for size {self.len}')
        
        n = 0
        curr = self.head
        while n < idx:
            curr = curr.next
            n += 1

        return curr


class ArrayStack:
    def __init__(self) -> None:
        self.data = []
    
    def push(self, val: Any) -> None:
        self.data.append(val)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('Pop from empty stack')

        return self.data.pop()

    def top(self) -> Any:
        if self.is_empty():
            raise IndexError('Peek from empty stack')

        return self.data[-1]

    def is_empty(self) -> bool:
        return len(self) == 0

    def __repr__(self) -> list:
        return f'{self.data}'

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterator:
        return iter(self.data)


class LinkStack:
    def __init__(self) -> None:
        self._data = LinkedList()

    @property
    def head(self) -> ListNode:
        return self._data.head

    def push(self, val: Any) -> None:
        self._data.insert(0, val)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        
        pop_item = self.top()
        self._data.remove(0)
        
        return pop_item

    def top(self) -> Any:
        if self.is_empty():
            raise IndexError('Peek from empty stack')

        return self.head.val

    def is_empty(self) -> bool:
        return self.head is None

    def __repr__(self) -> str:
        return f'{self.head}'

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator:
        return iter(self._data)


class ArrayQueue:
    def __init__(self) -> None:
        self.data = []

    def push(self, val: Any) -> None:
        self.data.append(val)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('Pop from empty queue')

        return self.data.pop(0)

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError('Peek from empty queue')

        return self.data[0]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __repr__(self) -> str:
        return f'{self.data}'

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterator:
        return iter(self.data)


class LinkQueue:
    def __init__(self) -> None:
        self._data = LinkedList()

    @property
    def head(self) -> ListNode:
        return self._data.head

    @property
    def tail(self) -> ListNode:
        curr = self.head
        while curr.next:
            curr = curr.next
        
        return curr

    def push(self, val: Any):
        self._data.insert(len(self), val)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError('Pop from empty queue')
        
        pop_item = self.head
        self._data.remove(0)

        return pop_item

    def front(self) -> Any:
        if self.is_empty():
            raise IndexError('Peek from empty queue')
        
        return self.head.val

    def is_empty(self) -> bool:
        return self.head is None

    def __repr__(self) -> str:
        return f'{self.head}'

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

def test():
    b = LinkQueue()
    for i in range(5):
        b.push(i + 1)
    for i in b:
        print(i.val)

if __name__ == '__main__':
    test()