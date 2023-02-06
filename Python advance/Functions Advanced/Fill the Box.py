def fill_the_box(height, lenght, width, *args):
    space = height * lenght * width
    fill_space = 0

    for cube in args:
        if cube == "Finish":
            break
        else:
            fill_space += int(cube)

    if fill_space < space:
        return f"There is free space in the box. You could put {space - fill_space} more cubes."
    else:
        return f"No more free space! You have {fill_space - space} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))