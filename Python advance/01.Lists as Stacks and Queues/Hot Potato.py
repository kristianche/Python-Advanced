from collections import deque

names = deque(input().split(" "))
n = int(input())
index = 1

while True:
    if len(names) == 1:
        break

    index = n - index

    if index <= len(names):
        removed_kid = names[index]
        names.remove(removed_kid)
    else:
        index -= len(names)
        removed_kid = names[index]
        names.remove(removed_kid)
    print(f"Removed {removed_kid}")

print(f"Last is {names[0]}")