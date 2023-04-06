N: int = int(input())

N_list: list = list(map(int, input().split()))
if len(N_list) != N:
    raise

v: int = int(input())

print(N_list.count(v))
