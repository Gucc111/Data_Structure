import sys

def test():
    class ListNode:
        def __init__(self, val = None, next = None):
            self.val = val
            self.next = next
        
        def __repr__(self):
            return f'{self.val} -> {self.next}'


    class LinkedList:
        def __init__(self):
            self.head = None
            self.size = 0
        
        def __repr__(self):
            return f'{self.head}'
        
        def insert(self, a, val):
            if (a != 1 and not self.head) or (a - 1 > self.size):
                return 'insert fail'
            
            node = ListNode(val)
            self.size += 1
            
            if not self.head:
                self.head = node
            elif a == 1:
                node.next = self.head
                self.head = node
            else:
                curr = self.head
                n = 0
                while n < a - 2:
                    n += 1
                    curr = curr.next
                node.next = curr.next
                curr.next= node
            
            return 'insert OK'
        
        def delete(self, a):
            if not self.head or a > self.size:
                return 'delete fail'
            
            if a == 1:
                self.head = self.head.next
            else:
                curr = self.head
                n = 0
                while n < a - 2:
                    curr = curr.next
                    n += 1
                curr.next = curr.next.next
            
            self.size -= 1
            
            return 'delete OK'
        
        @property
        def data(self):
            curr = self.head
            data = []
            while curr:
                data.append(curr.val)
                curr = curr.next
            return data

        def show(self):
            if not self.head:
                return 'Link list is empty'
            
            s = ''
            for i, j in enumerate(self.data):
                if i != len(self.data) - 1:
                    s += f'{j} '
                else:
                    s += f'{j}'
            
            return s
        
        def get(self, a):
            if not self.head or a > self.size:
                return 'get fail'
            
            curr = self.head
            n = 0
            while n < a - 1:
                curr = curr.next
                n += 1
            return curr.val

    lines = sys.stdin.readlines()
    n = int(lines[0].strip().split()[0])
    data = lines[0].strip().split()[1:]

    l = LinkedList()
    for i in range(n):
        l.insert(i+1, data[-(i+1)])

    i = 2
    while i < len(lines):
        cmd = lines[i].strip().split()

        if len(cmd) == 1:
            print(l.show())
        elif cmd[0] == 'delete':
            print(l.delete(int(cmd[1])))
        elif cmd[0] == 'get':
            print(l.get(int(cmd[1])))
        else:
            print(l.insert(int(cmd[1]), int(cmd[2])))
        
        i += 1

if __name__ == '__main__':
    test()