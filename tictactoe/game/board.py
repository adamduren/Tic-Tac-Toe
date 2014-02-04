from copy import deepcopy

from .player import Player, AiPlayer

X_MARK = 1
O_MARK = -1
PLAYER_BOARD_MARKS = (X_MARK, O_MARK)
PLAYER_BOARD_REPR = (
    (None, '-'),
    (X_MARK, 'X'),
    (O_MARK, 'O'),
)

NUM_CELLS = 9


class Board(object):
    def get_initial_state(self, state=None):
        if state is None:
            state = {
                'board': [None] * NUM_CELLS,
                'current_player': Player('Human', PLAYER_BOARD_MARKS[0]),
                'next_player': AiPlayer('Ai', PLAYER_BOARD_MARKS[1])
            }

        if not self._is_valid_state(state):
                raise ValueError('Not in a valid state.')

        return state

    def _is_valid_state(self, state):
        is_valid_cell_state = lambda col: (
            True if col in PLAYER_BOARD_MARKS or col is None else False
        )

        if len(state['board']) != NUM_CELLS:
            return False

        if not all(map(is_valid_cell_state, state['board'])):
            return False

        return True

    def get_actions(self, state):
        return [i for i, cell in enumerate(state['board']) if cell is None]

    def to_move(self, state):
        return state['current_player']

    def utility(self, state, player):
        winner = self.determine_winner(state)

        if winner is None:
            return 0

        if winner == player:
            return 1

        return -1

    def result(self, state, action):
        if action >= NUM_CELLS:
            raise ValueError('Not a valid position.')

        if action not in self.get_actions(state):
            raise ValueError('That position is already taken.')

        state = deepcopy(state)

        state['board'][action] = state['current_player'].mark
        state['current_player'], state['next_player'] = state['next_player'], state['current_player']

        return state

    def determine_winner(self, state):
        def winner_or_none(cells):
            if cells[0] and all([move == cells[0] for move in cells]):
                return cells[0]
            else:
                return None

        board = state['board']

        winner = (
            # Check for row win
            winner_or_none(board[0:3]) or
            winner_or_none(board[3:6]) or
            winner_or_none(board[6:9]) or

            # Check for column win
            winner_or_none(board[0::3]) or
            winner_or_none(board[1::3]) or
            winner_or_none(board[2::3]) or

            # Check for diagnoal win
            winner_or_none(board[2:7:2]) or
            winner_or_none(board[0:9:4])
        )

        return winner

    def is_terminal_state(self, state):
        return self.determine_winner(state) or not self.get_actions(state)

    def display(self, state):
        board_string = ''
        player_strings = dict(PLAYER_BOARD_REPR)

        for i, mark in enumerate(state['board']):
            board_string += '{} {}'.format(player_strings[mark], ' ')

            if i % 3 == 2 and i != 8:
                board_string += '\n'

        return board_string
