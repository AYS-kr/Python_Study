import sys
N = int(sys.stdin.readline())
card = [i for i in range(1,N+1)]

while len(card) > 1:
    card.pop(0)
    card.append(card.pop(0))

print(card[0])