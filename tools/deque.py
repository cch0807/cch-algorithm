# deque
# 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너
# 양방향 큐
# 데이터의 회전도 가능
# maxlen을 설정하여 최대 항목 수를 설정

from collections import deque

a = [10, 20, 30, 40, 50]
d = deque(a)
print(d)

print(dir(d))

d.append(100)
print(d)

d.appendleft(1000)
print(d)

temp = d.pop()
print(temp)

temp = d.popleft()
print(d)

print(temp)

d.rotate(2)
print(d)

d.rotate(-1)
print(d)
