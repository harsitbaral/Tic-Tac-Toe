# Basic Tic-Tac-Toe game
# Enter the spot on the grid you would like to go on
# Made by Harsit Baral at age 12
# Pretty bad code now that I look at it again.
# I could have cut down the lines by like 100

x_moves = []
o_moves = []

xms = []
oms = []

xms_counter = 0
oms_counter = 0

goOnX = True
draw = False

print("Tic-Tac-Toe:\nYou are either X or O. When it is your turn, you\nneed to place your letter on a square.\nTo win, you must make 3 in a row of your letter either\nvertically, horizontally, or diagonally.")
print("Board: \n- | - | -  1-1 1-2 1-3\n- | - | -  2-1 2-2 2-3\n- | - | -  3-1 3-2 3-3")

grid = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

constGrid = [
    ["1-1", "1-2", "1-3"],
    ["2-1", "2-2", "2-3"],
    ["3-1", "3-2", "3-3"]
]

constCols = [
    ["1-1", "2-1", "3-1"],
    ["1-2", "2-2", "3-2"],
    ["1-3", "2-3", "3-3"]
]

winningLines = [
    ["1-1", "1-2", "1-3"],
    ["2-1", "2-2", "2-3"],
    ["3-1", "3-2", "3-3"],
    ["1-1", "2-1", "3-1"],
    ["1-2", "2-2", "3-2"],
    ["1-3", "2-3", "3-3"],
    ["1-1", "2-2", "3-3"],
    ["1-3", "2-2", "3-1"]
]


def checkIfAvailable(slots, string):
    for slot in slots:
        if str(slot) == str(string):
            return False
        else:
            return True


def checkIfWon(player):
    hasWon = False
    hasWonD = False
    column1 = [grid[0][0],
               grid[1][0],
               grid[2][0]]  # lazily declared columns

    column2 = [grid[0][1],
               grid[1][1],
               grid[2][1]]

    column3 = [grid[0][2],
               grid[1][2],
               grid[2][2]]

    player_moves = [[], [], []]
    player_movesC = [[], [], []]

    columns = [column1, column2, column3]

    if grid[0][0] == str(player) and grid[1][1] == str(player) and grid[2][2] == str(player) or grid[0][2] == str(
            player) and grid[1][1] == str(player) and grid[2][0] == str(player):
        hasWonD = True  # check if diagonal
    else:
        pass

    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if grid[i][j] == str(player):
                player_moves[i].append(str(constGrid[i][j]))  # add the moves to the list in the order of winningLines
            if columns[i][j] == str(player):
                player_movesC[i].append(str(constCols[i][j]))

    for j in range(0, len(winningLines)):
        for move in player_moves:
            if move == winningLines[j]:
                hasWon = True  # check if player has won, stop checking if player has won if it's true
                break
        else:
            hasWon = False
            continue
        break

    for j in range(0, len(winningLines)):
        for i in range(0, len(player_movesC)):
            if player_movesC[i] == winningLines[j]:
                hasWon = True  # check if player has won, stop checking if player has won if it's true
                break
        else:
            hasWon = False
            continue
        break

    if hasWon or hasWonD:  # if the player has won
        return True
    else:
        return False


def main():
    global goOnX
    goOn = True
    if len(x_moves) >= 3:
        if checkIfWon("X"):
            goOn = False
            print("Congratulations, X! You Won!")
        else:
            pass
    elif len(o_moves) >= 3:
        if checkIfWon("O"):
            goOn = False
            print("Congratulations, O! You won!")
        else:
            pass
    else:
        goOn = True
    while goOn == True and goOnX == True:
        x_move = input("X, Where would you like to put your letter?\n")
        moves = x_moves + o_moves

        if checkIfAvailable(moves, x_move) and x_move != "" or len(moves) == 0:
            x_moves.append(str(x_move))
            moves = x_moves + o_moves
            # print("Length of X Moves: " + str(len(x_moves)))

            for i in range(0, len(grid)):
                for j in range(0, len(grid)):
                    if constGrid[i][j] == x_move:
                        grid[i][j] = "X"
                    else:
                        pass
            print(grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2] + "     1-1 | 1-2 | 1-3")
            print(grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2] + "     2-1 | 2-2 | 2-3")
            print(grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2] + "     3-1 | 3-2 | 3-3")
        else:
            while not checkIfAvailable(moves, x_move):
                x_move = input("ERROR! This square is taken! Please enter a different square: ")
                if checkIfAvailable(moves, x_move) and x_move != "":
                    x_moves.append(str(x_move))
                    moves = x_moves + o_moves

                    for i in range(0, len(grid)):
                        for j in range(0, len(grid)):
                            if constGrid[i][j] == x_move:
                                grid[i][j] = "X"
                                print(grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2] + "     1-1 | 1-2 | 1-3")
                                print(grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2] + "     2-1 | 2-2 | 2-3")
                                print(grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2] + "     3-1 | 3-2 | 3-3")
                            else:
                                pass
                else:
                    pass
        if len(x_moves) >= 3:
            if checkIfWon("X"):
                goOnX = False
                print("Congratulations, X! You Won!")
            else:
                goOnX = True
        else:
            goOn = True
        if len(moves) >= 9:
            draw = True
            print("Good game! It's a draw!")
            goOn = False
            goOnX = False
        else:
            draw = False
        if goOnX == True:
            o_move = input("O, Where would you like to put your letter?\n")
            if checkIfAvailable(moves, o_move) and x_move != "" or len(moves) == 0:

                o_moves.append(str(o_move))
                moves = x_moves + o_moves

                for i in range(0, len(grid)):
                    for j in range(0, len(grid)):
                        if constGrid[i][j] == o_move:
                            grid[i][j] = "O"
                        else:
                            pass
                print(grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2] + "     1-1 | 1-2 | 1-3")
                print(grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2] + "     2-1 | 2-2 | 2-3")
                print(grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2] + "     3-1 | 3-2 | 3-3")
            else:
                while not checkIfAvailable(moves, o_move) and x_move != "":
                    o_move = input("ERROR! This square is taken! Please enter a different square: ")
                    if checkIfAvailable(moves, o_move):
                        o_moves.append(str(o_move))
                        moves = x_moves + o_moves

                        for i in range(0, len(grid)):
                            for j in range(0, len(grid)):
                                if constGrid[i][j] == o_move:
                                    grid[i][j] = "O"
                                else:
                                    pass
                        print(grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2] + "     1-1 | 1-2 | 1-3")
                        print(grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2] + "     2-1 | 2-2 | 2-3")
                        print(grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2] + "     3-1 | 3-2 | 3-3")
                    else:
                        pass
            if len(moves) >= 9:
                draw = True
                print("Good game! It's a draw!")
                goOn = False
            else:
                draw = False
            if len(o_moves) >= 3:
                if checkIfWon("O"):
                    goOn = False
                    print("Congratulations, O! You won!")
                else:
                    pass
            elif len(x_moves) >= 3:
                if checkIfWon("O"):
                    goOn = False
                    print("Congratulations, X! You Won!")
                else:
                    pass
            else:
                goOn = True
        else:
            pass
    if goOn and goOnX:
        main()
    else:
        print("Thanks for playing! Made by Harsit Baral at age 12.\n")

main()
