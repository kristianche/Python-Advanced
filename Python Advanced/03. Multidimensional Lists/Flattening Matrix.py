matrix = [[int(el) for el in input().split(", ")] for _ in range(int(input()))]
result = [num for row in matrix for num in row]

print(result)