from  random import randrange

# add a variable to store current player
current_player = ''
# game winner
winner = ''

##
# First step : init board
# A Tic Tac Toc board is a 2 dimensions array
# eg : 3 x 3 => 3 rows and 3 columns
##
def init_board():
    # we must put the new variable current_player as global to modify it inside
    # this function - to do that we can use the 'global'  keyword
    global current_player
    # rang(3) => 3 elements , Start from 0 to 2
    # we init all square by a empty character
    board = [['' for col in range(3)] for row in range(3)]

    # now we will put number for each square
    index = 0
    for row in range(3):
        for col in range(3):
            index += 1
            board[row][col] = index
    # computer play first with X's sign in the middle of the board
    # => index_row = 1 and index_col = 1
    board[1][1] = 'X'
    # as the computer turn is done, so the next turn is you with the sign O's
    current_player = 'O'
    return board

##
# second step : print_board
# to print the board, I will use the power of the print function
##
def print_board(board):
    print('+-------' * 3, '+', sep='')
    for row in  range(3):
        print('|       ' * 3, '|', sep='')
        for col in range(3):
            print('|  ', str(board[row][col]) + '   ', end='')
        print('|')
        print('|       ' * 3, '|', sep='')
        print('+-------' * 3, '+', sep='')

# Now I will implement a new function which do a human move
# I will call enter_move
# This function will do many things :
# 1 - ask a number between 1 and 9
# 2 - valid this number(move) - if not valid then ask again
# 3 - get row and col from the entered move by using some mathematics operators
# 4 - check if the square is free and not occupied otherwise ask again ton enter
# a new move
# is it clear ? here we go !
def enter_move(board):
    print('Human turn !')

    is_ok = False
    while not is_ok:
        # ask a move
        move = input('Please enter e move (1 to 9) : ')

        # We test that snippet
        if len(move) != 1 or move < '1' or move > '9':
            print('Wrong move, please try again !')
            continue

        # get row and column index
        move = int(move) - 1
        # to get row I will use integer division operator
        row = move // 3
        # to get row I will use modulo operator
        col = move % 3

        # check if the square is free
        if board[row][col] in ['O', 'X']:
            print('Your move is incorrect. This square is occupied, please try again !')
            continue

        board[row][col] = 'O'
        # to break to while loop because we are ok here
        is_ok = not is_ok

##
# Now I will start implementing a new function for the computer moves
# To do that, we must check all free squares and return them
# and then choose randomly one square to put the computer sign 'X'
# So :
# 1 - create a function which return all free squares by using a list of tuples
# tuple in Python => tuple = (1,2)
# this function is called free_squares - it takes the board as argument
# 2 - create a second function which will draw the computer moves
##
def free_squares(board):
    free_filed = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                # every tuple contains the row index and the col index
                # of the free square in the board
                # free square => the square is not occupied neither 'X' nor 'O'
                free_filed.append((row, col))
    return free_filed

# 1 - call free_squares function
# 2 - get a random square
# 3 - get row and col index
# 4 - update the board
def draw_move(board):
    print('Computer turn !')
    free_fields = free_squares(board)
    free_fields_len = len(free_fields)

    # if we have free squares we do something
    if free_fields_len > 0:
        # we have to get a randomly field, so for that i will use
        # the randrange function from the random module
        random_field = randrange(free_fields_len)
        # get the row and col index
        row, col = free_fields[random_field]
        # put X's sign in the free square
        board[row][col] = 'X'

# In the last function I will check if we have a winner or a tie game
# for that, I will implement a new function called victory_for
# this function will check all board so as to find a winner, so for that :
# - we have to check all rows and see if we have a three sign aligner
# - check all columns
# - finally check both diagonals
# Go go go !
def victory_for(board, sign):
    # check all rows
    for row in range(3):
        if board[row][0] == sign and board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return sign
    # check all columns
    for col in range(3):
        if board[0][col] == sign and board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            return sign
    # check both diagonals
    if board[0][0] == sign and board[0][0] == board[1][1] and board[1][1] == board[2][2] or \
            board[2][0] == sign and board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return sign
    # else no winner
    return None

# Test our functions
# I will do some modification here in order to have a loop to start the game
# Here we have to make some changes
# 1 - use the free_squares function to control the while loop
# if we aldready have a free square we continue the game - otherwise it's the end
board = init_board()
free_fields = free_squares(board)

while len(free_fields) != 0:
    # print the board
    print_board(board)

    # if human turn
    if current_player == 'O':
        enter_move(board)
    else:
        draw_move(board)

    # check winner
    who_winn = victory_for(board, current_player)
    if who_winn != None:
        winner = who_winn
        break

    # which is turn ?
    # if the current player is computer so the next is you (human)
    # and vice versa
    if current_player == 'O':
        current_player = 'X'
    else:
        current_player = 'O'

    # after each move we have to recalculate the free squares
    free_fields = free_squares(board)

# print the final board
print_board(board)
# print the winner
if winner:
    if winner == 'O':
        print('Yohooo, You won the game !')
    else:
        print('You lost the game !')
else:
    print('Tie Game !')

