import sys

alpha = [0] * 26

word = sys.stdin.readline().rstrip()
for _ in word:
    alpha[(ord(_)-97)] += 1
    
    
print(*alpha)