from src.Data_Structure import *

def test():
    a = BinaryTree(15)
    data = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', None, None, None, 'k', 'i', None, None, None]
    a.create_tree(data)
    a.preorder_traversal()
    print()
    a.inorder_traversal()
    print()
    a.postorder_traversal()

if __name__ == '__main__':
    test()