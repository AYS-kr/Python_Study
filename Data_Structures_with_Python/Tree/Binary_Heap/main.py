from re import I
from binary_heap import BHeap

if __name__ == '__main__':
    a = [None] * 1
    a.append([90, 'watermelon'])
    a.append([80, 'pear'])
    a.append([70, 'melon'])
    a.append([50, 'lime'])
    a.append([60, 'mango'])
    a.append([20, 'cherry'])
    a.append([30, 'grape'])
    a.append([35, 'orange'])
    a.append([10, 'apricot'])
    a.append([15, 'banana'])
    a.append([45, 'lemon'])
    a.append([40, 'kiwi'])
    b = BHeap(a)
    print("힙 만들기 전: ")
    b.print_heap()
    b.create_heap()
    print('최소힙:')
    b.print_heap()
    print('최솟값 삭제 후')
    print(b.delete_min())
    b.print_heap()
    b.insert([5,'apple'])
    print('5 삽입 후')
    b.print_heap()