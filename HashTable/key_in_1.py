# Two sum
# 정수가 저장된 배열 nums이 주어졌을 때, nums의 원소 중 두 숫자를 더해서 target이 될 수 있으면 True 불가능하면 False를 반환.
# 같은 원소를 두번 사용 불가.

def two_sum(nums, target):
    memo = {}
    for v in nums:
        memo[v] = True
    
    for v in nums:
        needed_number = target - v
        if needed_number in memo:
            return True
    return False

print(two_sum(nums = [4,1,9,7,5,3,16], target=14))

