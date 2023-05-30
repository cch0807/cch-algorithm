# ChainMap
# 여러개의 컨테이너 자료형을 연결할 수 있음

from collections import ChainMap

oneDict = {"one": 1, "two": 2, "three": 3}
twoDict = {"four": 4}

chain = ChainMap(oneDict, twoDict)
print(chain)

print(dir(chain))

print("one" in chain)
print("four" in chain)
print("five" in chain)
print(len(chain))

print(chain.values())
print(chain.keys())
print(chain.items())

# chain[0] # error
# chain['oneDict'] #error
print(chain.maps)
print(chain.maps[0])
print(chain.maps[1])

# list
one = [1, 2, 3, 4]
two = [5, 6, 7, 8]
three = ChainMap(one, two)

print(three)

print(6 in three)
print(three.maps[0])
print(three.maps[1])
