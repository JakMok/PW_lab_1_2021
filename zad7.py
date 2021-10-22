def format_row(left_cell, right_cell):
    left_cell_text = f' {left_cell[0]:<{left_cell[1] - 1}}'
    right_cell_text = f' {right_cell[0]:>{right_cell[1] - 1}}'
    return f'{left_cell_text}|{right_cell_text}'


def table(width, height, length):
    print(format_row(("Wymiar", 20), ("Wartość", 20)))
    print(format_row(("Szerokość", 20), (str(width), 20)))
    print(format_row(("Wysokość", 20), (str(height), 20)))
    print(format_row(("Długość", 20), (str(length), 20)))


table(2434.4, 35.35, 0.202)
