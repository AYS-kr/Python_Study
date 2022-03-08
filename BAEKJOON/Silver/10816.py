import sys


def binary_search(list,start,end, num):
    if start > end:
        return None
    index = (start + end) // 2
    if list[index] == num :
        return num
    elif list[index] > num:
        return binary_search(list,start, index-1, num)
    else :
        return binary_search(list,index+1, end, num)

N = int(sys.stdin.readline())
card_li = sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
card_dic = {}

for _ in card_li:
    if _ not in card_dic:
        card_dic[_] = 1
    else:
        card_dic[_] += 1

for i in data:
    answer = binary_search(card_li,0,len(card_li)-1,i)
    try :
        print(card_dic[answer], end=' ')
    except:
        print(0,end=' ')
        
        