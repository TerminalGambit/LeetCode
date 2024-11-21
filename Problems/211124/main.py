def main(n, m, guards, walls):
    matrix = [[0] * n for _ in range(m)]

    for r, c in guards:
        matrix[r][c] = 1

    for r, c in walls:
        matrix[r][c] = 2

    def helper(r, c, dr, dc):
        while 0 <= r < m and 0 <= c < n and matrix[r][c] != 2 and matrix[r][c] != 1:
            if matrix[r][c] == 0:
                matrix[r][c] = 3
            r, c = r + dr, c + dc

    for r, c in guards:
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            helper(r + dr, c + dc, dr, dc)

    return sum(cell == 0 for row in matrix for cell in row)


assert (main(m=4, n=6, guards=[[0, 0], [1, 1], [2, 3]], walls=[[0, 1], [2, 2], [1, 4]]) == 7)
assert (main(m=3, n=3, guards=[[1, 1]], walls=[[0, 1], [1, 0], [2, 1], [1, 2]]))

# if __name__ == "__main__":
# main(3, 4, [], [])
