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

d = defaultdict(int)
for i in range(10):
    d[i] += 1

print(d)

# 특히 리스트의 경우 여러개의 중복값을 젖아하기 위한 용도로 많이 사용
temp_datas = [
    ("CLONE", 1123),
    ("DEFAULT", 23),
    ("MBTI", 1313),
    ("PYTHON", 312),
    ("CODING TSET", 1623),
]

d = defaultdict(list)
for title, nums in temp_datas:
    if nums < 100:
        d["ten"].append(title)
    elif nums < 1000:
        d["hundred"].append(title)
    elif nums < 10000:
        d["thousand"].append(title)

print(d)
