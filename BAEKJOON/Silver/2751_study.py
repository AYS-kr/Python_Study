import sys

input = sys.stdin.readline

n = int(input())
s = [int(input()) for _ in range(n)]
print("\n".join(map(str,sorted(s))))