import sys

word_list = [[]for _ in range(50)]
for i in range(int(sys.stdin.readline())):
    word = sys.stdin.readline().strip('\n')
    if word in word_list[len(word)-1]:
        continue
    else:
        word_list[len(word)-1].append(word)
    word_list[len(word)-1].sort()

for _ in word_list:
    if _ :
        for i in _:
            print(i)