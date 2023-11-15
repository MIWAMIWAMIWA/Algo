import ast
from collections import deque


class ColorChanger:
    def __init__(self):
        self.arr = []
        self.visited = {}
        self.height = None
        self.width = None
        self.to_change = None
        self.new_color = None

    def fill_all(self, filepath, new, i, j):
        data = read_data(filepath)
        self.arr = data
        if i < 1 or j < 1 or i > len(data) or j > len(data[0]):
            raise Exception("u entered incorrect position")
        self.to_change = data[i - 1][j - 1]
        self.new_color = new
        self.width = len(data[0])
        self.height = len(data)
        self.fill(i - 1, j - 1)
        self.visited = {}
        write_data("output.txt", self.arr)

    def fill(self, i, j):
        self.visited[str([i, j])] = 1
        if self.arr[i][j] == self.to_change:
            self.arr[i][j] = self.new_color
            if (str([i, j + 1]) not in self.visited) and j + 1 < self.width:
                self.fill(i, j + 1)
            if (str([i + 1, j]) not in self.visited) and i + 1 < self.height:
                self.fill(i + 1, j)
            if (str([i, j - 1]) not in self.visited) and j - 1 >= 0:
                self.fill(i, j - 1)
            if (str([i - 1, j]) not in self.visited) and i - 1 >= 0:
                self.fill(i - 1, j)

    def fill_BFS(self, i, j):
        queue = deque([(i, j)])
        while queue:
            i, j = queue.popleft()
            if (i, j) not in self.visited:
                self.visited[str([i, j])] = 1
                if self.arr[i][j] == self.to_change:
                    self.arr[i][j] = self.new_color
                    if j + 1 < self.width:
                        queue.append((i, j + 1))
                    if i + 1 < self.height:
                        queue.append((i + 1, j))
                    if j - 1 >= 0:
                        queue.append((i, j - 1))
                    if i - 1 >= 0:
                        queue.append((i - 1, j))


def read_data(file_path):
    grid = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                grid.append(ast.literal_eval(line))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    return grid


def write_data(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for row in data:
                file.write(str(row) + "\n")
    except IOError:
        print(f"Error writing to {file_path}")

miwa = ColorChanger()
miwa.fill_all('your_file.txt', "A", 3, 9)
