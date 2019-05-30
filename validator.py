import sys
import io
import chess.pgn

def main():
    # pgn = open(sys.argv[1])
    pgn = io.StringIO(sys.argv[1])
    user_move = chess.Move.from_uci(sys.argv[2].replace('\r', '').replace('\n', '')).uci()
    prev_game = chess.pgn.read_game(pgn)

    board = chess.Board()
    game = chess.pgn.Game()

    node = game

    for move in prev_game.mainline_moves():
        board.push(move)
        node = node.add_variation(move)

    legal_uci_moves = [m.uci() for m in list(board.legal_moves)]
    if (user_move not in legal_uci_moves): # invalid move
        print("That was not a legal move")
        sys.exit(1)

    # else valid move
    sys.exit(0)
main()
