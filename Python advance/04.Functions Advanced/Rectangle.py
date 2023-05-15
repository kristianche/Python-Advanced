def rectangle(lenght, width):
    def rectangle_area():
        return lenght * width

    def rectangle_perimeter():
        return 2 * (lenght + width)

    if type(lenght) != int or type(width) != int:
        return "Enter valid values!"

    return f'''Rectangle area: {rectangle_area()}
Rectangle perimeter: {rectangle_perimeter()}'''
