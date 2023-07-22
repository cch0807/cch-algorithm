# OrederdDict
# 순서가 있는 dict 자료형
# LRU 알고리즘을 구현하는 용도로 자주 사용
# 3.6버전까지 딕셔너리 순서 없음
# 3.7버전부터 딕셔너리 순서 유지

from collections import OrderedDict

oneDict = {"one": 1, "two": 2, "three": 3}
d = OrderedDict(oneDict)
print(d)

d.move_to_end("one")
print(d)

d.move_to_end("two")
print(d)

d.move_to_end("two", False)
print(d)

d.move_to_end("one", False)
print(d)

d.popitem(True)
print(d)

d.popitem(False)
print(d)

oneDict = {"one": 1, "two": 2, "three": 3}
d = OrderedDict(oneDict)

d.popitem()  # default = True
print(d)
