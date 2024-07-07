import tkinter as tk
from tkinter import messagebox

X = "X"
O = "O"
EMPTY = " "

WIN = 1
DRAW = 0
LOSS = -1

board = [EMPTY for _ in range(9)]

root = tk.Tk()
root.title('Tic Tac Toe')

def is_win(symbol):
    if board[0] == board[1] == board[2] == symbol:
        return True
    if board[3] == board[4] == board[5] == symbol:
        return True
    if board[6] == board[7] == board[8] == symbol:
        return True
    if board[0] == board[3] == board[6] == symbol:
        return True
    if board[1] == board[4] == board[7] == symbol:
        return True
    if board[2] == board[5] == board[8] == symbol:
        return True
    if board[0] == board[4] == board[8] == symbol:
        return True
    if board[2] == board[4] == board[6] == symbol:
        return True
    return False

def is_full():
    return EMPTY not in board

def evaluate():
    if is_win(X):
        return WIN
    if is_win(O):
        return LOSS
    if is_full():
        return DRAW

def minimax(is_maximizing):
    if is_win(X) or is_win(O) or is_full():
        return evaluate()
    if is_maximizing:
        best_value = -float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = X
                value = minimax(False)
                board[i] = EMPTY
                best_value = max(best_value, value)
        return best_value
    else:
        best_value = float("inf")
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = O
                value = minimax(True)
                board[i] = EMPTY
                best_value = min(best_value, value)
        return best_value

def find_best_move():
    best_value = -float("inf")
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = X
            value = minimax(False)
            board[i] = EMPTY
            if value > best_value:
                best_value = value
                best_move = i
    return best_move

def make_user_move(i):
    if board[i] == EMPTY:
        board[i] = O
        buttons[i].config(text=O)
        if is_win(O):
            messagebox.showinfo("Game over", "You win!")
            root.destroy()
        elif is_full() and not is_win(X):
            messagebox.showinfo("Game over", "It's a draw!")
            root.destroy()
        else:
            make_computer_move()

def make_computer_move():
    if not is_full():
        move = find_best_move()
        board[move] = X
        buttons[move].config(text=X)
        if is_win(X):
            messagebox.showinfo("Game over", "Computer wins!")
            root.destroy()
        elif is_full() and not is_win(O):
            messagebox.showinfo("Game over", "It's a draw!")
            root.destroy()


buttons = []
for i in range(9):
    button = tk.Button(root, text=EMPTY, command=lambda i=i: make_user_move(i), width=10, height=5,
                       font=('Helvetica', '20'))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)


root.mainloop()

