
import random


def inputPlayer():
    """Get input from the user either to be  X or O """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()  # input from the user
    if letter == 'X':

        return ['X', 'O']  # return a list
    else:
        return ['O', 'X']  # return a list


def check_board(board, l):
    """This function will finalize the result of both teams """
    return ((board[6] == l and board[7] == l and board[8] == l) or
            (board[3] == l and board[4] == l and board[5] == l) or
            (board[0] == l and board[1] == l and board[2] == l) or
            (board[6] == l and board[3] == l and board[0] == l) or
            (board[7] == l and board[4] == l and board[1] == l) or
            (board[8] == l and board[5] == l and board[4] == l) or
            (board[6] == l and board[4] == l and board[2] == l) or
            (board[8] == l and board[4] == l and board[0] == l))


def update_board(value, board, p):
    """This function will update the board at specific position"""
    # update the board with current value and position
    board[p] = value


def input_position(board):
    """  This function will get the position from the User """
    position = 0
    while True:
        position = input(
            "Enter the position where you want to place your piece ")  # get the position from the user where he want to place the value
        if position.isnumeric() and int(position) >= 1 and int(position) <= 9:
            position = int(position) - 1
            # if position is already occupied then again get value from user
            if board[position] != "' '":
                print("This position is already filled")
                print_board(board)
            else:
                return position
        else:
            print("Position should be number in between (1-9)")


def position_empty(board, move):
    """ Check that either current position is empty or not """
    return board[move] == "' '"


def move_value(board, player):
    """  This function will move the value from 1 position to other  """
    while True:  # while user not enter the true value

        position = input(
            "Enter the position from where you want to move value ")
        if position.isnumeric():  # if position is number then proceed
            position = int(position)
            if position >= 1 and position <= 9:
                value = board[position-1]
                if value in player:
                    # get the new position where user want to move value
                    nextP = input("Enter the position where you want to move ")
                    if nextP.isnumeric():
                        nextP = int(nextP)
                        if nextP >= 1 and nextP <= 9:  # check either position is in between 1 and 9 or not
                            if position_empty(board, nextP-1):
                                board[position-1] = "' '"
                                board[nextP-1] = value
                                return board
                            else:
                                print("Position is not empty")
                        else:
                            print("position should be in between 1-9")
                    else:
                        print("Position should be number")
                elif value == "' '":
                    print("The position is empty")
                else:
                    print("You are choosing the other player position ")
            else:
                print("position should be in between 1-9")

        else:
            print("Position should be number")


def get_Copy(board):
    """Return a copy of board """
    duplicate = []
    for i in board:
        duplicate.append(i)
    return duplicate


def chooseRandomMoveFromList(board, movesList):
    """Choosing the random value for computer depends on algorithm"""
    possibleMoves = []
    for i in movesList:  # iterating over list and make a list of possible position where player should move
        if position_empty(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def print_board(board):
    """This function will print the board"""
    print('['+board[0]+','+board[1]+','+board[2]+']')
    print('['+board[3]+','+board[4]+','+board[5]+']')
    print('['+board[6]+','+board[7]+','+board[8]+']')


def random_value(board, computerLetter, playerLetter):
    """ This function will get the random position from the computer """
    # if computerLetter == 'X':
    #     playerLetter = 'O'
    # else:
    #     playerLetter = 'X'

    # algorithm for checking that in the next move either computer could win or not
    for i in range(0, 9):
        copy = get_Copy(board)
        if position_empty(copy, i):
            update_board(computerLetter, copy, i)
            # if computer could win then return computer letter
            if check_board(copy, computerLetter):
                return [i, computerLetter]

# algorithm for checking that in the next move either player could win or not
    for i in range(0, 9):
        copy = get_Copy(board)
        if position_empty(copy, i):
            update_board(playerLetter, copy,  i)
            # if computer could win then return player letter
            if check_board(copy, playerLetter):
                return [i, playerLetter]
 # if no one could win then choose random value from these
    move = chooseRandomMoveFromList(board, [0, 2, 6, 8])
    if move != None:
        return [move, computerLetter]
    if position_empty(board, 5):
        return [5, computerLetter]

    return [chooseRandomMoveFromList(board, [1, 3, 5, 7]), computerLetter]


def choose():
    """ user will choose either player vs player or player vs computer mode """
    player = 0
    while True:
        player = input("For Player vs Player press 1 and for computer press 2")
        if player.isnumeric():  # is number or not

            # eithet choice is in between 1 and 2 or not
            if int(player) >= 1 and int(player) <= 2:
                return int(player)
            else:
                print("Please choose number between (1-2)")
        else:
            print("Please enter a number ")


def chooseEitherMoveOrChooseNew(board, le):
    """In This function user will choose either move existing value or not """
    while True:
        p = input("if you want to move existing value press 1 else 2 ")
        if p.isnumeric() and (int(p) >= 1 and int(p) <= 2):  # eithet choice is in between 1 and 2 or not
            p = int(p)
            # if p is 1 then check either player contain value or not
            if p == 1 and is_board_contain_value(board, le):
                return p
            elif p == 2:
                return p
            else:
                print(
                    "You are choosing the wrong value board does not contain any letter to move")

        else:
            print("please enter a number and in between 1-2")


def is_board_contain_value(board, l):
    """Check that board contain current player value or not """
    contain = False
    for i in range(0, 9):  # iterating over the board and check either player contain that value or not
        if board[i] == l:
            contain = True

    return contain


def board_is_full(board):
    """Check that either board is full or not if full then match will  be draw"""
    for i in range(0, 9):
        if position_empty(board, i):  # check current position is empty or not
            return False
    return True


def check_result(board, lastPlayer):
    """Check the board either anyone win or not yet """
    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X' or board[3] == 'X' and board[4] == 'X' and board[5] == 'X' or board[6] == 'X' and board[7] == 'X' and board[8] == 'X' or board[0] == 'X' and board[4] == 'X' and board[8] == 'X' or board[2] == 'X' and board[4] == 'X' and board[6] == 'X' or board[0] == 'X' and board[3] == 'X' and board[6] == 'X' or board[1] == 'X' and board[4] == 'X' and board[7] == 'X' or board[2] == 'X' and board[5] == 'X' and board[8] == 'X' or board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
        print(lastPlayer+" ('X') Win's ")  # if player X wins
        exit()
    elif board[0] == 'O' and board[1] == 'O' and board[2] == 'O' or board[3] == 'O' and board[4] == 'O' and board[5] == 'O' or board[6] == 'O' and board[7] == 'O' and board[8] == 'O' or board[0] == 'O' and board[4] == 'O' and board[8] == 'O' or board[2] == 'O' and board[4] == 'O' and board[6] == 'O' or board[0] == 'O' and board[3] == 'O' and board[6] == 'O' or board[1] == 'O' and board[4] == 'O' and board[7] == 'O' or board[2] == 'O' and board[5] == 'O' and board[8] == 'O' or board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
        print(lastPlayer+" ('O') Win's ")  # if player O wins
        exit()


def main():
    """This function is the main that will hold the whole functionality"""
    playerLetter = ""
    lastPlayer = ""
    p1 = False
    p2 = False
    players = list([1, 2])
    turn = 0
    i = 1
    board = list()
    # creating the empty board
    for _ in range(10):
        board.append("' '")  # generating the board
    playerChoose = choose()  # player will choose what he want

    while True:

        print_board(board)  # print the board
        # calling the function to check the result
        check_result(board, lastPlayer)

        if board_is_full(board):  # if board is full no one could win
            print("Match Tied")
            exit()

        if i % 2 != 0:  # check that either its player turn or computer
            lastPlayer = "Player 1 "
            playerLetter = inputPlayer()
            turn = players[0]
            print("Player "+str(turn) + " turns ")
            choice = chooseEitherMoveOrChooseNew(board, playerLetter[0])
            if choice == 1 and p1:
                move_value(board, playerLetter[0])
            elif choice == 2:
                p1 = True
                # calling the input position function to get the position
                p = input_position(board)
                # calling the update_board method that will update board
                update_board(playerLetter[0], board, p)

        else:
            if playerChoose == 1:
                lastPlayer = " Player 2 "
                playerLetter = inputPlayer()
                turn = players[1]
                print("Player "+str(turn)+" turns ")
                choice = chooseEitherMoveOrChooseNew(board, playerLetter[0])
                if choice == 1 and p2:
                    #move_value(board, playerLetter[1])
                    move_value(board, playerLetter[0])
                elif choice == 2:
                    p2 = True
                    p = input_position(board)
                    #update_board(playerLetter[1], board, p)
                    update_board(playerLetter[0], board, p)

            else:
                # if the computer turn then computer will place its value
                lastPlayer = " Computer "
                print("Computer turns")
                turn = players[1]
                # calling the random function to get position
                p = random_value(board, playerLetter[1], playerLetter[0])
                update_board(p[1], board, p[0])

        i += 1


main()  # calling the main function
