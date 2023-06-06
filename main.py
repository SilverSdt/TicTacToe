from engine.TicTacToe import TicTacToe

if __name__ == "__main__":
    t: TicTacToe = TicTacToe()

    # print empty grid
    print(t)

    # while grid is not full or a player has not won
    while not t.is_full() and not t.is_player_win():

        # while move is not valid
        turn_loop: bool = True
        while turn_loop:

            # choose a case
            move: str = input("select case: ")

            # if is a digit
            if move.isdigit():
                try:
                    # turn_loop become false if the move was insert
                    turn_loop = not t.set_target(int(move))
                    # if turn_loop = if target was not empty
                    if turn_loop:
                        print("please choose a valid target")

                # if input was not between 1 and 9
                except ValueError as e:
                    print(e)

        # print grid with move insert
        print(t)

    # if the game was a draw => board is full and no player won
    if t.is_full() and not t.is_player_win(): print("Draw...")
    # the current player is the winner
    else: print(f"player {t.current_player + 1} won!")