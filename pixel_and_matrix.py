def matrix_to_pixel(row, col):
    x_coordinate = 0; y_coordinate = 0
    if col == 0: x_coordinate = 150
    elif col == 1: x_coordinate = 300
    elif col == 2: x_coordinate = 450

    if row == 0: y_coordinate = 150
    elif row == 1: y_coordinate = 300
    elif row == 2: y_coordinate = 450

    return (x_coordinate, y_coordinate)

def pixels_to_matrix(x_coordinate,y_coordinate):
    row = -1; col = -1

    if (135 < x_coordinate < 165): col = 0
    if (285 < x_coordinate < 315): col = 1
    if (435 < x_coordinate < 465): col = 2

    if (135 < y_coordinate < 165): row = 0
    if (285 < y_coordinate < 315): row = 1
    if (435 < y_coordinate < 465): row = 2

    return (row,col)