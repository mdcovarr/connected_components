import numpy as np

matrix = np.array([
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
])


def check_valid(visited, row, col):
    if (row < 0) or (row >= len(visited)) or (col < 0) or (col >= len(visited[0])):
        return False

    if visited[row][col] == 1 or matrix[row][col] == 0:
        return False

    return True

def count_components():
    visited = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    count = 0

    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if matrix[m][n] == 1 and visited[m][n] == 0:
                dfs(visited, m, n)
                count += 1

    return count

def dfs(visited, row, col):
    visited[row][col] = 1
    row_neighbors = [-1, 0, 1, -1, 1, -1, 0, 1]
    col_neighbors = [-1, -1, -1, 0, 0, 1, 1, 1]

    for i in range(len(row_neighbors)):
        if check_valid(visited, row + row_neighbors[i], col + col_neighbors[i]):
            dfs(visited, row + row_neighbors[i], col + col_neighbors[i])

def main():
    """
    """
    count = count_components()
    print('# of Islands: {0}'.format(count))

if __name__ == '__main__':
    main()
