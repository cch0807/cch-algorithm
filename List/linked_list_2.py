# Linked List의 다양한 활용
# 1. Linked List 자유자재로 구현 (선형 자료구조 + 중간에 데이터 추가/삭제 용이)
# 2. Tree or Graph에 활용

# 인터넷 브라우저에서 방문기록과 동일한 작동을 하는 BrowserHistory class를 구현.
# 구현할 브라우저는 homepage에서 시작하고, 이후에는 다른 url에 방문할 수 있다.
# 또, "뒤로가기"와 "앞으로 가기"가 작동하도록 구현.


class ListNode(object):
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory(object):
    def __init__(self, homepage: str):
        self.head = self.current = ListNode(val=homepage)

    def visit(self, url: str):
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = self.current.next

    def back(self, steps: int):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps: int):
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.currnet.val


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)
