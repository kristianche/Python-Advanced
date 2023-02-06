n = int(input())
matrix = [[int(el) for el in input().split(" ")] for _ in range(n)]
primary = [int(matrix[r][r]) for r in range(n)]
secondary = [int(matrix[r][n - r - 1]) for r in range(n - 1, -1, -1)]

primary_sum = sum(primary)
secondary_sum = sum(secondary)
difference = abs(primary_sum - secondary_sum)

print(difference)