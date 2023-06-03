# Default Dict
# 키로 어떤 값이 들어올지 모를 경우 사용

from collections import defaultdict

oneDict = {"one": 1, "two": 2, "three": 3}
# d = defaultdict(oneDict)
# print(d)
d = defaultdict(str)

d["one"] = "1"
d["two"] = "2"
d["three"]

print(d)

d = defaultdict(list)

d["one"] = "1"
d["two"] = "2"
d["three"]

print(d)
