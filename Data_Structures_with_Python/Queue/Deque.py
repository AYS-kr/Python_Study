from collections import deque

#새 데크 객체를 생성
dq = deque('data')
for elem in dq:
    print(elem.upper(), end='')
print()

#맨 뒤에 항목 삽입
dq.append('r')
#맨 앞에 항목 삽입
dq.appendleft('k')

print(dq)

#맨 뒤에 항목 삭제
dq.pop()
#맨 앞에 항목 삭제
dq.popleft()
#맨뒤 항목 출력
print(dq[-1])
#데크에 x가 있는지 출력
print('x' in dq)

#맨 뒤에 여러 항목 삽입
dq.extend('structure')
#맨 앞에 여러 항목 삽입
dq.extendleft(reversed('python'))

print(dq)