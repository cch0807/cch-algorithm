# Dynamic Array (list)

a = [1, 2, 3] # 선언 및 초기화: O(n)

# 접근 및 수정 : O(1)
a = [0] # random access -> O(1)
a[1] = 9 # random access -> O(1)

# 데이터 추가 : O(1)
a.append(4)
a.append(5)
a.append(6)

# 마지막 데이터 삭제 : O(1)
a.pop()
a.pop()

# 중간에 데이터 추가 : O(n)
a.insert(1, 10)

# 중간에 데이터 삭제: O(n)
a.pop(2)
