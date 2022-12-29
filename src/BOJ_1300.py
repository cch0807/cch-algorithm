# 만약, X가 어떤 배열에서 k번째로 작은 수라면,
# X 보다 작은 수가 k-1개 이하 있다.
# X 보다 큰 수가 N-k개 이하 있다.

# 입력
n = int(input())
k = int(input())


def get_num_smaller(x: int) -> int:
    # 문제에서 주어진 n x n 이차원 배열에서 x 보다 작은 수으 ㅣ개수를 구하여 반환하는 함수
    num_smaller = 0
    for i in range(1, n + 1):
        # 1번째 행에서 x보다 작은 수의 개수는 min(n, (x - 1) // i) 개
        num_smaller += min(n, (x - 1) // i)

    return num_smaller


def get_num_bigger(x: int) -> int:
    # 문제에서 주어진 n x n 이차원 배열에서 x 보다 큰 수의 개수를 구하여 반환하는 함수
    num_bigger = 0
    for i in range(1, n + 1):
        # i 번째 행에서 x보다 큰 수의 개수는 n - min(n, x // i) 개
        num_bigger += n - min(n, x // i)


# 이분 탐색을 수행하는 메인 로직
low = 1
high = min(n * n, int(1e9))
answer = -1

while low <= high:
    mid = (low + high) // 2

    num_smaller = get_num_smaller(mid)
    num_bigger = get_num_bigger(mid)
