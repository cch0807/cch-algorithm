"""
Number of Islands
grid는 "1"(land) 과 "0"(water)으로 이루어진 지도를 표현하는 m x n 이차원배열이다.
이 지도에 표시된 섬들의 총 갯수를 반환하시오.
섬이란 수평과 수직으로 땅이 연결되어 있고 주변은 물로 둘러쌓여있는 것을 말한다.
또한, grid의 네개의 가장자리는 모두 물로 둘러쌓있다고 가정하고 문제를 해결하라.

제약조건
m == grid.length
n == grid[i].length
1 <= m,n <= 300
grid[i][j] is '0' or '1'
"""

from collections import deque


grid: list[list[str]] = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]


def numIslands(grid: list) -> int:
    number_of_islands = 0
    row_len = len(grid)
    col_len = len(grid[0])
    visited = [[False] * col_len for _ in range(row_len)]

    def bfs(r, c):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited[r][c] = True
        queue = deque()
        queue.appendleft((r, c))
        while queue:
            cur_x, cur_y = queue.pop()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x >= 0 and next_x < col_len and next_y >= 0 and next_y < row_len:
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))

    for r, row in enumerate(grid):
        for c, letter in enumerate(row):
            if grid[r][c] == "1" and not visited[r][c]:
                bfs(r, c)
                number_of_islands += 1
                # dfs()
    return number_of_islands


print(numIslands(grid))


class BreadthFirstSearch:
    def __init__(self, grid: list[list[str]]):
        self.grid = grid
        self.row_len: int = len(grid)
        self.col_len: int = len(grid[0])
        self.dx: list[int] = [-1, 1, 0, 0]
        self.dy: list[int] = [0, 0, -1, 1]
        self.queue: deque = deque()
        self.visited: list[list[bool]] = [[False] * self.col_len for _ in range(self.row_len)]
        self.number_of_island = 0

    def bfs(self, r, c) -> None:
        self.visited[r][c] = True
        self.queue.append((r, c))
        while self.queue:
            cur_x, cur_y = self.queue.pop()
            for i in range(4):
                next_x = cur_x + self.dx[i]
                next_y = cur_y + self.dy[i]
                if next_x >= 0 and next_x < self.col_len and next_y >= 0 and next_y < self.row_len:
                    if self.grid[next_x][next_y] == "1" and not self.visited[next_x][next_y]:
                        self.visited[next_x][next_y] = True
                        self.queue.append((next_x, next_y))

    def main(self) -> int:
        for r, row in enumerate(grid):
            for c, letter in enumerate(row):
                if self.grid[r][c] == "1" and not self.visited[r][c]:
                    self.bfs(r, c)
                    self.number_of_island += 1

        return self.number_of_island


bfs = BreadthFirstSearch(grid)
print(bfs.main())
