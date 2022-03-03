def shift(input_list, shift_size, position):
    rows = len(input_list)
    columns = len(input_list[0])

    if position == 'i':
        if shift_size == rows:
            return input_list

        output_list = [[0] * rows for i in range(columns)]

        if abs(shift_size) > rows:
            shift_size = shift_size % rows

        for row in range(rows):
            for column in range(columns):
                number = row + shift_size
                if number >= rows:
                    number -= rows
                output_list[number][column] = input_list[row][column]
        return output_list

    if position == 'j':
        if shift_size == columns:
            return input_list

        output_list = [[0] * rows for i in range(columns)]

        if abs(shift_size) > columns:
            shift_size = shift_size % columns

        for column in range(columns):
            for row in range(rows):
                number = column + shift_size
                if number >= columns:
                    number -= columns
                output_list[row][number] = input_list[row][column]
        return output_list


def short_shift(input_list, shift_size):
    rows = len(input_list)
    if position == 'i':
        return rotate(input_list, shift_size)
    if position == 'j':
        for row in range(rows):
            input_list[row] = rotate(input_list[row], shift_size)
        return input_list


def rotate(input_list, shift_size):
    return input_list[-shift_size:] + input_list[:-shift_size]


def print_list(input_list):
    for row in range(len(input_list)):
        for column in range(len(input_list[0])):
            print(input_list[row][column], end=' ')
        print()


def output(input_list, shift_size, position):
    print('Input:')
    print_list(input_list)
    print('Output shift() with shift_size = {0} by {1}:'.format(shift_size, position))
    print_list(shift(input_list, shift_size, position))
    print('Output short_shift() with shift_size = {0} by {1}:'.format(shift_size, position))
    print_list(short_shift(input_list, shift_size))


def test(input_list):
    if len(input_list) == 0:
        return False
    for row in range(len(input_list)):
        if len(input_list[0]) != len(input_list[row]):
            return False
    return True


if __name__ == '__main__':
    input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    shift_size = -1
    position = 'j'

    if test(input_list):
        output(input_list, shift_size, position)
    else:
        print('Unsuitable list.')