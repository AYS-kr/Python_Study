word = input().upper()
alpha = list(set(word))

cnt_list = []
for _ in alpha:
    cnt = word.count(_)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1 :
    print("?")
else :
    print(alpha[cnt_list.index(max(cnt_list))])