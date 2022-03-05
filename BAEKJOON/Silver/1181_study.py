# 다른 사람 코드를 보니 훨씬 짧고 코드 발견
# set()를 통해 중복 값 제거
# sort() 에서 key를 사용
import sys

word = []
for i in range(int(sys.stdin.readline())):
    word.append(sys.stdin.readline().strip())
    
set_word = set(word)
word = list(set_word)

# 알파벳 순서로 정렬
word.sort()
# 문자열 길이 순으로 정렬
word.sort(key=len)

for _ in word:
    print(_)