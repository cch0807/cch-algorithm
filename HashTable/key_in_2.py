# 해시테이블의 활용
# 메모리를 사용해서 시간복잡도를 줄일 때 사용
# key in {} 가 핵심

# Longest Consecutive Sequence
# 정렬되어 있지 않은 정수형 배열 nums가 주어졌다.
# nums 원소를 가지고 만들 수 있는 가장 긴 연속된 수의 갯수는 몇개인지 반환.


from typing import List

# 1


def longest_consecutive(nums: List[int]) -> int:
    min_num = min(nums)
    count = 1

    for _ in range(len(nums)):
        if min_num + 1 in nums:
            min_num += 1
            count += 1

    return count


if __name__ == "__main__":
    # nums = [100,4,200,1,3,2]
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longest_consecutive(nums))

# 2


def longestConsecutive(nums):
    longest = 0
    num_dict = {}
    for num in nums:
        num_dict[num] = True
    print(num_dict)
    for num in num_dict:
        if num - 1 not in num_dict:
            cnt = 1
            target = num + 1
            while target in num_dict:
                target += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest


print(longestConsecutive([6, 7, 100, 5, 4, 4]))


# 3
def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    max_val = 1
    num_set = set(nums)
    for x in num_set:
        if x - 1 not in num_set:
            target = x + 1
            val = 1
            while target in num_set:
                target += 1
                val += 1
                if max_val < val:
                    max_val = val
    return max_val
