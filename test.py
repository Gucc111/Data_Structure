from src.Data_Structure import *

def test():
    a = Tree(9)
    for i in range(9):
        a.assign_data(i, i + 1)
    print(a)
    a.set_root(0)
    a.add_child(0, [1, 2])
    a.add_child(1, 3)
    a.add_child(2, [4, 5])
    a.add_child(3, [6, 7, 8])
    a.dfs()
    print()
    print(a.degree)

if __name__ == '__main__':
    test()