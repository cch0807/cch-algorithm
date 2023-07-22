# brute force


# 1 ( BOJ 1816 )

# i = int(input())

# for _ in range(i):
#     password = int(input())

#     for i in range(2, 1_000_001):
#         if password % i == 0:
#             print("NO")
#             break
#         if i == 1_000_000:
#             print("YES")

# 2 ( BOJ 14568 )

# candy = int(input())
# answer = 0

# for A in range(0, candy + 1):
#     for B in range(0, candy + 1):
#         for C in range(0, candy + 1):
#             if A + B + C == candy:
#                 if A >= B + 2:
#                     if A != 0 and B != 0 and C != 0:
#                         if C % 2 == 0:
#                             answer += 1

# print(answer)

# 3 ( BOJ 19532 )

# A, B, C, D, E, F = map(int, input().split())

# for x in range(-999, 999):
#     for y in range(-999, 999):
#         if A * x + B * y == C:
#             if D * x + E * y == F:
#                 print(x, y)
#                 break

# 4 ( BOJ 2503 )

# n = int(input())

# hint = [list(map(int, input().split())) for _ in range(4)]

# answer = 0

# for a in range(1, 10):
#     for b in range(10):
#         for c in range(10):
#             if a == b or b == c or c == a:
#                 continue

#             cnt = 0

#             for arr in hint:
#                 number = hint[0]
#                 ball = hint[1]
#                 strike = hint[2]

#                 # a, b, c 라는 숫자를
#                 # number와 비교

#                 ball_count = 0
#                 strike_count = 0

#                 if ball == ball_count and strike == strike_count:
#                     cnt += 1

#             if cnt == n:
#                 answer += 1

# print(answer)


# 5 ( BOJ 1090 )

# 1번 아이디어
# x, y 를 구분해서 계산해준 뒤에 합쳐서
# 최솟값을 알려주면 된다.

# 2번 아이디어
# 우리가 한 곳에서 모일 때, 비용을 최소화 하기 위해서는
# 우리의 집 중 한 곳에서 모이면 된다.

# 3번 아이디어
# 최소 거리를 계산하고 싶다.
# 그리고, 2명이 모여야한다.
# 그 점에서, 가까운 두명의 거리만 더해주면 되지 않을까?

N = int(input())

distance = [list(map(int, input().split())) for _ in range(N)]
