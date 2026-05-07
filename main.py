# TIC-TAC-TOE GAME
def print_board(board):
    print("\n╔═══╦═══╦═══╗")
    for i in range(3):
        print("║", end=" ")
        for j in range(3):
            print(f"{board[i * 3 + j]:^2}║", end=" ")
        print("\n╠═══╬═══╬═══╣")
    print("╚═══╩═══╩═══╝")


def is_valid_move(board, pos):
    return 0 <= pos < 9 and board[pos] == " "


def check_winner(board):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def is_full(board):
    return " " not in board


def play():
    board = [" "] * 9
    player = "X"

    print("🎮 TIC-TAC-TOE 🎮")
    print("Positions: 1|2|3  4|5|6  7|8|9")

    while True:
        print_board(board)

        try:
            move = int(input(f"\nPlayer {player}: Enter position (1-9): ")) - 1
            if not is_valid_move(board, move):
                print("❌ Invalid move! Try again.")
                continue
        except:
            print("❌ Enter number 1-9!")
            continue

        board[move] = player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🏆 {winner} WINS! 🏆")
            break

        if is_full(board):
            print_board(board)
            print("🤝 DRAW! 🤝")
            break

        player = "O" if player == "X" else "X"

while True:
    play()
    if input("\nPlay again? (y/n): ").lower() != 'y':
        print("👋 Thanks for playing!")
        break