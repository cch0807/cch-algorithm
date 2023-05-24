"""
Shortest Path in Binary Matrix
n x n binary matrix인 grid가 주어졌을 때, 출발지에서 목적지 까지 도착하는 가장 빠른 경로의 길이를 반환
만약 경로가 없다면 -1 반환

출발지: top-left cell
목적지: bottom - right cell

- 값이 0인 cell만 지나갈 수 있다.
- cell끼리는 8가지 방향으로 연결되어 있다. (edge와 corner 방향으로 총 8가지)
- 연결된 cell을 통해서만 지나갈 수 있다.

제약조건
n == grid.length
n == grid[i].length
1 <- n <= 100
grid[i][j] is 0 or 1
"""

from collections import deque
from pprint import pprint

grid = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
]


def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1
    row = len(grid)
    col = len(grid[0])
    visited = [[False] * col for _ in range(row)]
    delta = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
    ]

    visited[0][0] = True
    queue = deque()
    queue.append((0, 0))

    while queue:
        cur_r, cur_c = queue.pop()
        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc

    return shortest_path_len


print(shortestPathBinaryMatrix(grid))
