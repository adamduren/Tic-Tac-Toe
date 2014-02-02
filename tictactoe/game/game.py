from itertools import cycle

from . import Board, PLAYERS, PLAYER_STRINGS


class ConsoleGame(object):
    board = None

    def start(self, board_state=None):
        board = self.board = Board(board_state)
        turns = cycle(PLAYERS)
        player_names = dict(PLAYER_STRINGS)

        while True:
            print(board)

            game_is_over, winner = board.is_terminal_state()

            if game_is_over:
                break

            player = turns.next()

            print('{}\'s turn'.format(player_names[player]))

            try:
                board.take_turn(player, int(raw_input()))
            except ValueError as e:
                print('{} Would you like to continue playing? '.format(e.message))

                if raw_input() not in ['y', 'yes']:
                    break

                # We need to advance the turn by one since the player
                # made a mistake
                turns.next()

        if winner:
            print('{} Wins!'.format(player_names[winner]))
