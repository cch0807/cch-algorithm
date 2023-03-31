# Vaild Parentheses 
# '(){}[]'를 포함하고 있는 문자열 s가 주어졌을 때, 괄호가 유효한지 아닌지 판별하시오.
# 1. 짝수여야 함.
# 2. 여는괄호가 먼저

s = "{(([]))[]}"

def isValid(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.append("]")
        elif not stak or stack.pop() != p:
            return False
    return not stack
            