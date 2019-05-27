import sys
import io
import chess.pgn

def main():
    # pgn = open(sys.argv[1])
    pgn = io.StringIO(sys.argv[1])
    user_move = chess.Move.from_uci(sys.argv[2])
    prev_game = chess.pgn.read_game(pgn)

    board = chess.Board()
    game = chess.pgn.Game()

    node = game

    for move in prev_game.mainline_moves():
        board.push(move)
        node = node.add_variation(move)

    # TODO: check if game is over here, return 1 if yes (check for checkmate, etc)
    
    if (user_move not in board.legal_moves): # invalid move
        print("That was not a legal move")
        sys.exit(1)
    board.push(user_move)
    node = node.add_variation(user_move)

    # TODO: check if game is over here again, if yes return 1 (check for duplicate moves, etc)

    print(game)
    print("Move was valid")

main()
