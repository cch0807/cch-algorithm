# 코테 적용 방법
# 배열의 다양한 활용
# 1. 반복문
# 2. Sort & Two Pointer

# 접근방법 (가장 어려워 하는 부분)

# 직관적으로 생각하기
#   보통 완전탐색으로 시작
#   문제 상황을 단순화 하여 생각하기
#   문제 상황을 극한화 하여 생각하기

# 자료구조와 알고리즘 활용
#   파악한 내용을 토대로 어떤 자료구조를 사용하는게 가장 적합한지 결정
#   대놓고 특정 자료구조와 알고리즘을 묻는 문제도 많음
#   자료구조에 따라 선택할 수 있는 알고리즘을 문제에 적용

# 메모리 사용
#   시간복잡도를 줄이기 위해 메모리를 사용하는 방법
#   대표적으로 해시테이블

def two_sum(nums, target) -> bool:
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
    
    return False

if __name__ == "__main__":
    print(two_sum(nums=[4,1,9,7,5,3,16], target=14))

