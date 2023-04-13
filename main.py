from tkinter import *

# create window
window = Tk()
window.title("Tic Tac Toe")

# create board as a matrix
board = [[0 for x in range(3)] for y in range(3)]

# set the size of the window
window.geometry("300x300")

# set the turn
turn = 1

# set the initial count of turns
count = 0

# create a result label
result_label = Label(window, text="Player 1's turn")
result_label.grid(row=3, columnspan=3)


# function to check result
def checkResult():
    # check for row
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            if board[i][0] == 1:
                result_label.config(text="Player 1 won")
            else:
                result_label.config(text="Player 2 won")
            return True

    # check for column
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            if board[0][i] == 1:
                result_label.config(text="Player 1 won")
            else:
                result_label.config(text="Player 2 won")
            return True

    # check for diagonal
    if board[0][0] == board[1][1] == board[2][2] != 0:
        if board[0][0] == 1:
            result_label.config(text="Player 1 won")
        else:
            result_label.config(text="Player 2 won")
        return True

    if board[0][2] == board[1][1] == board[2][0] != 0:
        if board[0][2] == 1:
            result_label.config(text="Player 1 won")
        else:
            result_label.config(text="Player 2 won")
        return True

    # check for tie
    if count == 9:
        result_label.config(text="It's a tie")
        return True

    return False


# function to change the turn
def changeTurn():
    global turn
    if turn == 1:
        turn = 2
        result_label.config(text="Player 2's turn")
    else:
        turn = 1
        result_label.config(text="Player 1's turn")


# function to check if the box is empty
def isEmpty(row, col):
    if board[row][col] == 0:
        return True
    return False


# function to check if the box is filled
def isFilled(row, col):
    if board[row][col] != 0:
        return True
    return False


# function to check the click
def click(row, col):
    global count
    if isEmpty(row, col):
        count += 1
        if turn == 1:
            board[row][col] = 1
            btn = Button(window, text="X", font="Arial 20 bold", bg="white")
        else:
            board[row][col] = 2
            btn = Button(window, text="O", font="Arial 20 bold", bg="white")
        btn.config(state=DISABLED)
        btn.grid(row=row, column=col)

        # check the result
        if checkResult():
            for i in range(3):
                for j in range(3):
                    if isFilled(i, j):
                        btn = Button(window, text=board[i][j], font="Arial 20 bold", bg="white")
                        btn.config(state=DISABLED)
                        btn.grid(row=i, column=j)
            return
        changeTurn()


for i in range(3):
    for j in range(3):
        btn = Button(window, text=" ", font="Arial 20 bold", command=lambda row=i, col=j: click(row, col))
        btn.grid(row=i, column=j)

window.mainloop()
