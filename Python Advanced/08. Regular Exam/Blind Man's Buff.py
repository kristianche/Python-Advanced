rows, cols = [int(i) for i in input().split(" ")]
field = []

for row in range(rows):
    field.append(input().split())

B_coordinates = []
players_touched = 0
moves_made = 0

possible_rows = [int(i) for i in range(rows)]
possible_cols = [int(i) for i in range(cols)]

for row in range(rows):
    for col in range(cols):
        if field[row][col] == "B":
            B_coordinates.append(row)
            B_coordinates.append(col)
            break


command = input()

while True:

    if command == "Finish" or players_touched == 3:
        break

    if command == "up":
        current_row = int(B_coordinates[0]) - 1
        current_col = int(B_coordinates[1])
        if current_row in possible_rows and current_col in possible_cols:
            if not field[current_row][current_col] == "O":
                moves_made += 1
                field[int(B_coordinates[0])][int(B_coordinates[1])] = "-"
                if field[current_row][current_col] == "P":
                    players_touched += 1
                    field[current_row][current_col] = "B"
                    B_coordinates = [current_row, current_col]
                else:
                    field[current_row][current_col] = "B"
                    B_coordinates = [current_row, current_col]
    elif command == "down":
        current_row = int(B_coordinates[0]) + 1
        current_col = int(B_coordinates[1])
        if current_row in possible_rows and current_col in possible_cols:
            if not field[current_row][current_col] == "O":
                moves_made += 1
                field[int(B_coordinates[0])][int(B_coordinates[1])] = "-"
                if field[current_row][current_col] == "P":
                    players_touched += 1
                    field[current_row][current_col] = "B"
                    B_coordinates = [current_row, current_col]
                else:
                    field[current_row][current_col] = "B"
                    B_coordinates = [current_row, current_col]

    elif command == "right":
        current_row = int(B_coordinates[0])
        current_col = int(B_coordinates[1]) + 1
        if current_row in possible_rows and current_col in possible_cols:
            if not field[current_row][current_col] == "O":
                moves_made += 1
                field[int(B_coordinates[0])][int(B_coordinates[1])] = "-"
                if field[current_row][current_col] == "P":
                    players_touched += 1
                    field[current_row][current_col] = "B"
                    B_coordinates = [current_row, current_col]
                else:
                    field[current_row][current_col] = "B"
                    B_coordinates = [current_row, current_col]

    elif command == "left":
        current_row = int(B_coordinates[0])
        current_col = int(B_coordinates[1]) - 1
        if current_row in possible_rows and current_col in possible_cols:
            if not field[current_row][current_col] == "O":
                moves_made += 1
                field[int(B_coordinates[0])][int(B_coordinates[1])] = "-"
                if field[current_row][current_col] == "P":
                    players_touched += 1
                    field[current_row][current_col] = "B"
                    B_coordinates = [current_row, current_col]
                else:
                    field[current_row][current_col] = "B"
                    B_coordinates = [current_row, current_col]
    command = input()


print("Game over!")
print(f"Touched opponents: {players_touched} Moves made: {moves_made}")





