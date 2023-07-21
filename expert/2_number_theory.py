# 1 ( BOJ 15736 )

# n = int(input())

# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i)

n = int(input())

numbers = list(map(int, input().split()))

answer = 0
for num in numbers:
    if num < 2:
        continue

    print(num**0.5)
    print(int(num**0.5))
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            continue

    answer += 1

print(answer)
