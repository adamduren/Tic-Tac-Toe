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
    board_state = None
    last_player = None

    def __init__(self, board_state=None):
        if not board_state:
            board_state = [None] * NUM_CELLS

        if not self._is_valid_board(board_state):
                raise ValueError('Not a valid board state.')

        self.board_state = board_state
        self.turns = []

    def _is_valid_board(self, board):
        is_valid_cell_state = lambda col: (
            True if col in PLAYER_BOARD_MARKS or col is None else False
        )

        if len(board) != NUM_CELLS:
            return False

        if not all(map(is_valid_cell_state, board)):
            return False

        return True

    def take_turn(self, player, move):
        if player not in PLAYER_BOARD_MARKS:
            raise ValueError('Invalid player passed.')

        if player is self.last_player:
            raise ValueError('Player played out of turn.')

        if move >= NUM_CELLS:
            raise ValueError('Not a valid position.')

        if move not in self.positions_remaining():
            raise ValueError('That position is already taken.')

        self.last_player = player
        self.board_state[move] = player

    def is_terminal_state(self):
        def is_three_in_a_row(candidate):
            if candidate[0] and all([move == candidate[0] for move in candidate]):
                return True
            else:
                return False

        return (
            # Check for row win
            is_three_in_a_row(self.board_state[0:3]) or
            is_three_in_a_row(self.board_state[3:6]) or
            is_three_in_a_row(self.board_state[6:9]) or

            # Check for column win
            is_three_in_a_row(self.board_state[0::3]) or
            is_three_in_a_row(self.board_state[1::3]) or
            is_three_in_a_row(self.board_state[2::3]) or

            # Check for diagnoal win
            is_three_in_a_row(self.board_state[2:7:2]) or
            is_three_in_a_row(self.board_state[0:9:4])
        )

    def positions_remaining(self):
        return [i for i, cell in enumerate(self.board_state) if cell is None]

    def __str__(self):
        board_string = ''
        player_strings = dict(PLAYER_BOARD_REPR)

        for i, state in enumerate(self.board_state):
            board_string += '{} {}'.format(player_strings[state], ' ')

            if i % 3 == 2 and i != 8:
                board_string += '\n'

        return board_string
