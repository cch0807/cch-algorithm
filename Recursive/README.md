# 재귀함수 (Recursive function)
- 재귀함수(Recursive function)란 자신을 정의할 때 자기 자신을 재참조하는 함수를 뜻함.

# recurrence relation -> 점화식
- problem와 subproblem(s)의 관계식을 말함.

# base case
- 더이상 재귀호출을 하지 않아도 계산값을 반환할 수 있는 상황(조건)을 말함.
- 모든 입력이 최종적으로 base case을 이용해서 문제를 해결할 수 있어야 함.
- basecase가 무조건 있어야 재귀함수의 무한루프를 방지할 수 있다.

# 시간복잡도
- 재귀함수 전체 시간복잡도 = 재귀 함수 호출 수 x (재귀 함수 하나당) 시간 복잡도
- Execution Tree(recursion tree): 재귀 함수의 실행 흐름을 나타내는 데 사용되는 트리

- O(n) n에 비례한 호출
    - recurrence relation : f(n) = f(n - 1) + n

- O(2^n) 2^N에 비례한 호출
    - recurrence relation: f(n) = f(n - 1) + f(n - 2)
