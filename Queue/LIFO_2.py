# Daily Temperatures
# 매일의 온도를 나타내는 int형 배열 temperatures가 주어진다.
# answer배열의 원소 answer[i]는 i번 째 날의 온도보다 더 따듯해지기까지 며칠을 기다려야하는지 나타낸다.
# 만약 더 따듯해지는 날이 없다면 answer[i] == 0이다.
# answer 배열을 반환하는 함수를 구현하시오.


def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    stack = []
    for cur_day, cur_temp in enumerate(temperatures):
        while stack and stack[-1][1] < cur_temp:
            prev_day, _ = stack.pop()
            ans[prev_day] = cur_day - prev_day
        stack.append((cur_day, cur_temp))
    print(ans)
    return ans


dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
