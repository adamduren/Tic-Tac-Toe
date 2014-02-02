from itertools import cycle

from .board import Board, PLAYER_BOARD_MARKS
from .player import Player, AiPlayer


class ConsoleGame(object):
    board = None

    def __init__(self, players=None):
        if players is None:
            players = [
                Player('Human', PLAYER_BOARD_MARKS[0]),
                AiPlayer('Ai', PLAYER_BOARD_MARKS[1])
            ]

        if len(players) != 2:
            raise ValueError('Tic-Tac-Toe requires two players')

        self.players = players

    def start(self, board_state=None):
        board = self.board = Board(board_state)
        turns = cycle(self.players)

        while True:
            print(board)

            game_is_over = board.is_terminal_state()

            if game_is_over:
                break

            player = turns.next()

            print('{}\'s turn'.format(player.name))

            try:
                board.take_turn(player.mark, player.make_turn_decision(board))
            except ValueError as e:
                print('{} Would you like to continue playing? '.format(e.message))

                if raw_input() not in ['y', 'yes']:
                    break

                # We need to advance the turn by one since the player
                # made a mistake
                turns.next()

        if game_is_over:
            print('{} Wins!'.format(player.name))
