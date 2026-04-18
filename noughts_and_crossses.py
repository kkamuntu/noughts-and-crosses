VALID_POSITIONS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def get_blank_board():

    board = {}

    for position in VALID_POSITIONS:
        board[position] = ' '

    return board


def get_board_map():

    board_map = {}

    for position in VALID_POSITIONS:
        update_board(board_map, position, position)

    return board_map


def get_board_string(board: dict):

    board_string = ''

    for i in range(1, 10):
        board_string += board[str(i)]

        if i in [3, 6]:
            board_string += '\n-+-+-\n'

        elif i != 9:
            board_string += '|'

    return board_string


def get_players():

    player_1 = {"name": input("Player 1 name: "), "marker": "X"}
    player_2 = {"name": input("Player 2 name: "), "marker": "0"}

    return [player_1, player_2]


def is_valid_move(board, move):
    return move in VALID_POSITIONS and board[move] == ' '


def get_player_move(player, board):

    move = input(f"{player['name']}, what is your move? (1-9) ")

    while not is_valid_move(board, move):
        print("That's not a valid move")
        move = input(f"{player['name']}, what is your move? (1-9) ")

    return move


def update_board(board, move, marker):
    board[move] = marker


def is_winner(board, player):

    return ((board['1'] == board['2'] == board['3'] == player['marker']) or
            (board['4'] == board['5'] == board['6'] == player['marker']) or
            (board['7'] == board['8'] == board['9'] == player['marker']) or
            (board['1'] == board['4'] == board['7'] == player['marker']) or
            (board['2'] == board['5'] == board['8'] == player['marker']) or
            (board['3'] == board['6'] == board['9'] == player['marker']) or
            (board['1'] == board['5'] == board['9'] == player['marker']) or
            (board['3'] == board['5'] == board['7'] == player['marker']))


def is_board_full(board):

    for position in VALID_POSITIONS:

        if board[position] == ' ':
            return False

    return True


def play_game():

    welcome_message = "Noughts and Crosses!"
    print("\n" + "~"*len(welcome_message))
    print(welcome_message)
    print("~"*len(welcome_message) + "\n")

    print("Who will be playing today?\n")

    [player1, player2] = get_players()

    print("\nMap of possible moves:\n\n" +
          get_board_string(get_board_map()) + "\n")

    print(
        f"{player1['name']}({player1['marker']}) vs {player2['name']}({player2['marker']})\n")

    game_board = get_blank_board()
    [current_player, next_player] = [player1, player2]

    while True:

        print(get_board_string(game_board) + "\n")

        next_move = get_player_move(current_player, game_board)

        update_board(game_board, next_move, current_player['marker'])

        if is_winner(game_board, current_player):

            print("\n" + get_board_string(game_board) + "\n")
            print(f"{current_player['name']} wins!")
            break

        elif is_board_full(game_board):
            print("\n" + get_board_string(game_board))
            print("\nIt's a tie!")
            break

        [current_player, next_player] = [next_player, current_player]

    print("\nThanks for playing!")


if __name__ == "__main__":
    play_game()
