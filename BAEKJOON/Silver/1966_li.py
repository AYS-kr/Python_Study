import sys

for i in range(int(sys.stdin.readline())):
    N ,M = map(int, sys.stdin.readline().split())
    li_importance = list(map(int,sys.stdin.readline().split()))
    doc = list(range(len(li_importance)))
    doc[M] = "answer"
    i = 1
    while li_importance:
        if li_importance[0] == max(li_importance):
            li_importance.pop(0)
            if doc.pop(0) == "answer":
                print(i)
                break
            i += 1
        else:
            li_importance.append(li_importance.pop(0))
            doc.append(doc.pop(0))
