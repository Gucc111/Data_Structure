from src.Data_Structure import *

def test():
    a = BinarySearchTree()
    a.insert(5)
    a.insert(4)
    a.insert(2)
    a.insert(1)
    a.insert(3)
    a.insert(7)
    a.insert(6)
    a.insert(9)
    a.insert(8)
    print(a.search(3))
    a.remove(3)
    print(a.search(3))
    a.inorder_traversal()

if __name__ == '__main__':
    test()