# Counter
# 객체의 요소 개수를 key와 value 값으로

from collections import Counter

a = [1, 1, 1, 1, 1, 2, 2, 3, 4, 5, 1, 2, 6, 7, 2, 4]
c = Counter(a)
print(c)

for i in c:  # unpacking X
    print(i)
    print("---")

for i in c.elements():
    print(i)
    print("---")

print(c.keys())
print(c.values())
print(c.items())

for i, j in c.items():
    print(i, j)

print(c.most_common())
s = "hello, world"
sc = Counter(s)
print(sc)

sc.update("hello")
print(sc)
print(sc.total())

sc.subtract("hello")
print(sc)
