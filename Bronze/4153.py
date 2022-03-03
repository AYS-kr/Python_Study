while True:
    a = list(map(int, input().split()))
    if sum(a) == 0:
        break
    b = max(a) ** 2
    a.remove(max(a))
    if b == a[0] **2 + a[1] ** 2 :
        print("right")
    else:
        print("wrong")
