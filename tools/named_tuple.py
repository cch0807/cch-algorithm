# 튜플처럼 immutable
# 이름을 통해 데이터로 접근 가능
# 메모리 활용 최적화(성능상에 이점이 있음) -> 활용하려는 자료형에 비해 어느정도 성능상에 이점이 있다는 것은 시간 측정 필요

# 참조하고있는 데이터의 내부 데이터는 mutable
l = [10, 20, 30]
t = (l, 10, 20)
l[2] = 100

# Basic example
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(11, y=22)  # instantiate with positional or keyword arguments
p[0] + p[1]  # indexable like the plain tuple (11, 22)

print(p)

print(p.x, p.y)

# p[x] # error
i, j = p
print(i, j)

print(Point)

d = {"x": 100, "y": 200}
p = Point(**d)
print(p.x, p.y)

print(p._asdict)
print(p._fields)
print(p._field_defaults)
re_p = p._replace(x=1000)
print(re_p)
print(p)
print(p.count("x"))

from dataclasses import dataclass  # 3.7 부터 사용 가능, 구조체 import dataclass


@dataclass
class Point:
    x: int = None
    y: int = None


print(Point())
p = Point(10, 20)
print(p)

# i, j = p # error

print(p.x, p.y)

from collections import namedtuple

skill = namedtuple("기술", "기술이름, 자격증, 연차")  # csv 파일을 가져올 때 유용
changhyeon = skill("파이썬", "정보처리기사", "3")
print(skill)
print(changhyeon)
