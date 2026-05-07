#!/usr/bin/python3

def print_board(board):
    """Print the tic tac toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """Return True if a player has won."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False


def board_full(board):
    """Return True if there are no empty spaces left."""
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """Run the tic tac toe game."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
            continue

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position. Row and column must be between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"


tic_tac_toe()