# from re import I
# import sys
# import math
# N = int(sys.stdin.readline())

# sum = 0
# end = int(math.sqrt(N)+1)
# for i in range(1, end):
#     if N % i == 0:
#         sum += i + N//i
#         if i == N//i:
#             sum -= i
# if N == 1:
#     sum = 1

# print(sum)
# 블로그 여러개 본 후 이해....
import sys

n = int(sys.stdin.readline())
sum = 0
for i in range(1, n+1):
    sum += (n//i)*i
print(sum)