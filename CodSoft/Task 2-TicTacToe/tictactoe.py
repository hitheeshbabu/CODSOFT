# Tic-Tac-Toe game with Minimax AI
# Author: Hitheesh Babu M | CodSoft Internship

# Step 1: Create the board
board = [" " for _ in range(9)]  # 0-8 positions

def print_board():
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print("| " + " | ".join(row) + " |")
    print()

# Step 2: Check for winner
def is_winner(player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_positions)

# Step 3: Check if board is full
def is_draw():
    return " " not in board

# Step 4: Minimax algorithm for AI
def minimax(is_maximizing):
    if is_winner("O"):
        return 1
    elif is_winner("X"):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Step 5: AI move using Minimax
def ai_move():
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

# Step 6: Player move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")

# Step 7: Main game loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and AI is O.")
    print_board()

    while True:
        player_move()
        print_board()
        if is_winner("X"):
            print("Congratulations! You won! 🎉")
            break
        elif is_draw():
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()
        if is_winner("O"):
            print("AI wins! Better luck next time. 🤖")
            break
        elif is_draw():
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    main()
