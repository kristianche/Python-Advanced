from collections import deque
quantity_of_water = int(input())
names_deque = deque()
while True:
    name = input()
    if name == "Start":
        break
    else:
        names_deque.append(name)
while True:
    command = input().split(" ")
    if command[0] == "End":
        break
    elif command[0] == "refill":
        liters = int(command[1])
        quantity_of_water += liters
    else:
        liters = int(command[0])
        person = names_deque.popleft()
        if liters <= quantity_of_water:
            quantity_of_water -= liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
print(f"{quantity_of_water} liters left")
