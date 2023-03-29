# queue 선언
q = []
# enqueue O(1)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
# dequeue 0(n)
q.pop(0)
q.pop(0)
q.pop(0)

from collections import deque

queue = deque()
# enqueue() O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# dequeue() O(1)
queue.popleft()
queue.popleft()
queue.popleft()
