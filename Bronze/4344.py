case_num = int(input())

for i in range(0,case_num):
    a = list(map(int,input().split()))
    n = a.pop(0)
    avg = sum(a)/n
    count = 0
    for score in a:
        if score > avg:
            count += 1
    print("{0:0.3f}%".format(float((count/n*100))))