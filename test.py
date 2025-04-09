from src.Data_Structure import *

def test():
    a = QueueStack()
    for i in range(5):
        a.push(i + 1)
    print(a)
    print()
    for i in a:
        print(i)

if __name__ == '__main__':
    test()