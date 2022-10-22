# adding text colors
def colored(r, g, b, text):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"


# letter I
letter_i = [[" " for columns_in_name in range(5)]for rows_in_name in range(7)]
for row in range(7):
    for column in range(5):
        if column == 2 or ((row == 0 or row == 6) and column != 2):
            letter_i[row][column] = "*"

# letter S
letter_s = [[" " for columns_in_name in range(5)] for rows_in_name in range(7)]
for row in range(7):
    for column in range(5):
        if ((row == 0 or row == 3 or row == 6) or (column == 0 and (row >= 0 and row < 3)) or (column == 4 and row > 3)):
            letter_s[row][column] = "*"

# letter H
letter_h = [[" " for columns_in_name in range(5)] for rows_in_name in range(7)]
for row in range(7):
    for column in range(5):
        if column == 0 or column == 4 or (row == 3 and (column > 0 and column < 4)):
            letter_h[row][column] = "*"

# printing name in asterisk format
for columns_in_name in range(7):
    for rows_in_name in range(5):
        printed_letter_i = letter_i[columns_in_name][rows_in_name]
        print(colored(209, 107, 165, printed_letter_i), end="")
    print(end=" ")
    for rows_in_name in range(5):
        printed_letter_s = letter_s[columns_in_name][rows_in_name]
        print(colored(134, 168, 231, printed_letter_s), end="")
    print(end=" ")
    for rows_in_name in range(5):
        printed_letter_h = letter_h[columns_in_name][rows_in_name]
        print(colored(95, 251, 241, printed_letter_h), end="")
    print()
