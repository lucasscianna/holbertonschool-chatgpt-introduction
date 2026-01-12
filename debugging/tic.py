#!/usr/bin/python3

def print_board(board):
    """Print the Tic Tac Toe board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 5)

def check_winner(board):
    """Check if there is a winner."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True, row[0]

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, board[0][2]

    return False, None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Get valid input
        while True:
            try:
                row = int(input(f"Enter row (0-2) for player {player}: "))
                col = int(input(f"Enter column (0-2) for player {player}: "))
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Coordinates out of bounds! Try again.")
                    continue
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter numbers 0, 1, or 2.")

        board[row][col] = player

        # Check for winner
        won, winner = check_winner(board)
        if won:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check for draw
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = "O" if player == "X" else "X"

tic_tac_toe()
