import random
from collections import deque

WIDTH = 21  # 迷宮的寬度
HEIGHT = 21  # 迷宮的高度

# 迷宮結構初始化
def initialize_maze():
    maze = [[1] * WIDTH for _ in range(HEIGHT)]  # 1表示牆壁，0表示路徑
    return maze

# 使用深度優先搜索 (DFS) 生成迷宮
def generate_maze(maze, start_x, start_y):
    stack = [(start_x, start_y)]
    maze[start_y][start_x] = 0  # 起點設為0，代表路徑

    while stack:
        x, y = stack[-1]
        neighbors = []

        # 檢查四個方向的相鄰單元
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and maze[ny][nx] == 1:
                neighbors.append((nx, ny))

        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[(y + ny) // 2][(x + nx) // 2] = 0
            maze[ny][nx] = 0
            stack.append((nx, ny))
        else:
            stack.pop()

# 使用 BFS 解決迷宮，不使用 came_from
def solve_maze(maze, start, end):
    queue = deque([start])
    visited = [[False] * WIDTH for _ in range(HEIGHT)]  # 記錄是否走過
    visited[start[1]][start[0]] = True
    parent = [[None] * WIDTH for _ in range(HEIGHT)]  # 用來回溯路徑

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y = queue.popleft()

        # 找到終點，開始回溯路徑
        if (x, y) == end:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[y][x]
            path.append(start)  # 加入起點
            return path[::-1]  # 路徑反轉

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT and maze[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                parent[ny][nx] = (x, y)  # 記錄來源
                queue.append((nx, ny))

    return None  # 如果無法找到路徑，返回 None

# 顯示迷宮
def print_maze(maze):
    for row in maze:
        print(''.join('#' if cell == 1 else ' ' for cell in row))

# 顯示解答路徑
def visualize_solution(maze, path):
    for y, x in path:
        maze[y][x] = 2  # 標記解答路徑

    for row in maze:
        print(''.join('#' if cell == 1 else '.' if cell == 2 else ' ' for cell in row))

# 主程式
def main():
    print("生成迷宮...")
    maze = initialize_maze()
    generate_maze(maze, 1, 1)  # 設置起點為 (1, 1)

    start = (1, 1)
    end = (HEIGHT - 2, WIDTH - 2)  # 設置終點為 (HEIGHT-2, WIDTH-2)

    print("生成的迷宮:")
    print_maze(maze)

    print("\n解迷宮中...")
    path = solve_maze(maze, start, end)

    if path:
        print("\n解迷宮成功！")
        visualize_solution(maze, path)
    else:
        print("\n無法找到解決方案！")

if __name__ == "__main__":
    main()