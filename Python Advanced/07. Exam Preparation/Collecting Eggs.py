from collections import deque

eggs = deque(int(x) for x in input().split(", "))
pieces_of_paper = deque(int(x) for x in input().split(", "))

filled_boxes = 0
max_size_box = 50

while True:
    if not eggs or not pieces_of_paper:
        break

    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue
    elif current_egg == 13:
        first_paper = pieces_of_paper.popleft()
        last_paper = pieces_of_paper.pop()
        pieces_of_paper.appendleft(last_paper)
        pieces_of_paper.append(first_paper)
    else:
        current_paper = pieces_of_paper.pop()
        wrapped_egg = current_egg + current_paper
        if wrapped_egg <= max_size_box:
            filled_boxes += 1
        else:
            continue


if filled_boxes >= 1:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if pieces_of_paper:
    print(f"Pieces of paper left: {', '.join([str(x) for x in pieces_of_paper])}")