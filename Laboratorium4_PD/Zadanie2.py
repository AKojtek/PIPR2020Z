"""
Program checks who is the winner of given tictactoe table
If it is a draw empty string is returned
"""

tictactoe = [
    ['x', 'o', 'o'],
    ['x', 'o', 'x'],
    ['x', 'x', 'o']
    ]

tictactoe2 = [
    ['x', 'o', 'x'],
    ['o', 'o', 'x'],
    ['o', 'x', 'o']
    ]

tictactoe3 = [
    ['x', 'o', 'o'],
    ['o', 'x', 'x'],
    ['o', 'x', 'x']
    ]

tictactoe4 = [
    ['o', 'o', 'o'],
    ['x', 'x', 'o'],
    ['o', 'x', 'x']
    ]


def check_line(elems):
    for row in elems:
        # Jezeli kazda komorka wiersza to ten znak
        # to dlugosc set(row) powinna byc rowna 1
        if len(set(row)) == 1:
            return row[0]
    return 0


def turn_table(elems):
    # Transponuje macierz tictactoe
    new_list = []
    for i in range(len(elems)):
        column = []
        for row in elems:
            column.append(row[i])
        new_list.append(column)
    return new_list


def check_diagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        return board[0][0]
    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        return board[0][len(board)-1]
    return ""


def look_for_winner(elems):
    horizontal = check_line(elems)
    if horizontal:
        return(horizontal)
    new_list = turn_table(elems)
    vertical = check_line(new_list)
    if vertical:
        return(vertical)
    return check_diagonals(elems)


print(look_for_winner(tictactoe))
print(look_for_winner(tictactoe2))
print(look_for_winner(tictactoe3))
print(look_for_winner(tictactoe4))