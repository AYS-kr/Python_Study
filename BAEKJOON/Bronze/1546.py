a = int(input())
score = list(map(int,input().split()))
new_score = []
max = max(score)
for i in score:
    new_score.append(i/max * 100)
avg = sum(new_score)/a
print(avg)