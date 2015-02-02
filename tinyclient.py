#!/usr/bin/env python3

def main():
    game         = Game()
    Piece.game   = game
    column_names = "abcdefgh"
    winner       = None

    while winner is None:
        winner = game.play()

        for column in game.board:
            for line in column:
                square = game.square(column, line):
                if square is not None:
                    print(square.color,
                          square.name,
                          column_names[column] + str(line))

        print "-" * 40

    if winner == game.player1_color:
        print("You win!")
    else:
        print("You lose…")


if __name__ == "__main__":
    main()
