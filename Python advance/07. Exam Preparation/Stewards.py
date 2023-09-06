from collections import deque

seats = input().split(", ")
first_sequence = deque(int(x) for x in input().split(", "))
second_sequence = deque(int(x) for x in input().split(", "))
rotations = -0
seat_matches = []


while True:
    if len(seat_matches) >= 3 or rotations >= 10:
        break

    num_1 = int(first_sequence.popleft())
    num_2 = int(second_sequence.pop())
    sum = num_1 + num_2
    letter = chr(sum)
    str_num_1 = str(num_1)
    str_num_2 = str(num_2)

    first_seat = str_num_1 + letter
    second_seat = str_num_2 + letter

    if first_seat in seats or second_seat in seats:
        if first_seat in seats:
            seat_matches.append(first_seat)
            seats.remove(first_seat)
        elif second_seat in seats:
            seat_matches.append(second_seat)
            seats.remove(second_seat)
    elif first_seat not in seats and second_seat not in seats:
        first_sequence.append(num_1)
        second_sequence.appendleft(num_2)
    elif first_seat in seat_matches or second_seat in seat_matches:
        pass

    rotations += 1


print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")

