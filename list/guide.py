# 코테 적용 방법
# 배열의 다양한 활용
# 1. 반복문
# 2. Sort & Two Pointer


def two_sum(nums, target) -> bool:
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return True

    return False


if __name__ == "__main__":
    print(two_sum(nums=[4, 1, 9, 7, 5, 3, 16], target=14))
