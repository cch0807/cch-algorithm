# Array list 를 활용한 문제풀이
# 인터넷 브라우저에서 방문기록과 동일한 작동을 하는 BrowserHistory class를 구현.
# 구현할 브라우저는 homepage에서 시작하고, 이후에는 다른 url에 방문할 수 있다.
# 또, "뒤로가기"와 "앞으로 가기"가 작동하도록 구현.


class BrowserHistory(object):
    def __init__(self, homepage: str):
        self.li: list = [homepage]
        self.index: int = 0

    def visit(self, url: str):
        if self.index == len(self.li):
            self.li.append(url)

        self.index += 1

    def back(self, steps: int):
        if self.index - steps < 0:
            pass

    def forward(self, steps: int):
        pass
