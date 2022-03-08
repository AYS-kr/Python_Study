from sys import stdin
_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = map(int,stdin.readline().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        i, j = 1, 1
        while m-i >= start:
            if N[m-i] != N[m]:
                break
            else: i += 1
        while m+j <= end:
            if N[m+j] != N[m]:
                break
            else: j += 1
        return i + j - 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M ))