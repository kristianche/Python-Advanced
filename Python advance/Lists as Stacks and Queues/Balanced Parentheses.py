from collections import deque

parentheses = deque(input())
open_parentheses = deque()

while parentheses:
    left_parentheses = parentheses.popleft()

    if left_parentheses in "{([":
        open_parentheses.append(left_parentheses)
    elif not open_parentheses:
        print("NO")
        break
    else:
        if f"{open_parentheses.pop() + left_parentheses}" not in "{}()[]":
            print("NO")
            break
else:
    print("YES")