X_MARK = 1
O_MARK = -1
PLAYERS = (X_MARK, O_MARK)
PLAYER_STRINGS = (
    (None, '-'),
    (X_MARK, 'X'),
    (O_MARK, 'O'),
)


class Board(object):
    board_state = None
    last_player = None

    def __init__(self, board_state=None):
        if not board_state:
            board_state = [None] * 9

        if not self._is_valid_board(board_state):
                raise ValueError('Not a valid board state.')

        self.board_state = board_state
        self.turns = []

    def _is_valid_board(self, board):
        is_valid_cell_state = lambda col: (
            True if col is X_MARK or col is O_MARK or col is None
            else False
        )

        if len(board) != 9:
            return False

        if not all(map(is_valid_cell_state, board)):
            return False

        return True

    def take_turn(self, player, move):
        if player not in PLAYERS:
            raise ValueError('Invalid player passed')

        if player is self.last_player:
            raise ValueError('Player played out of turn')

        if move not in self.valid_moves():
            raise ValueError('Invalid move')

        self.last_player = player
        self.board_state[move] = player

    def is_terminal_state(self):
        def get_winner_or_none(candidate):
            if all([move == candidate[0] for move in candidate]):
                return candidate[0]
            else:
                return None

        winner = (
            # Check for row win
            get_winner_or_none(self.board_state[0:3]) or
            get_winner_or_none(self.board_state[3:6]) or
            get_winner_or_none(self.board_state[6:9]) or

            # Check for column win
            get_winner_or_none(self.board_state[0::3]) or
            get_winner_or_none(self.board_state[1::3]) or
            get_winner_or_none(self.board_state[2::3]) or

            # Check for diagnoal win
            get_winner_or_none(self.board_state[2:7:2]) or
            get_winner_or_none(self.board_state[0:9:4])
        )

        is_terminal_state = True if winner else False

        return is_terminal_state, winner

    def valid_moves(self):
        return [i for i, cell in enumerate(self.board_state) if cell is None]

    def __str__(self):
        board_string = ''
        player_strings = dict(PLAYER_STRINGS)

        for i, state in enumerate(self.board_state):
            board_string += '{} {}'.format(player_strings[state], ' ')

            if i % 3 == 2 and i != 8:
                board_string += '\n'

        return board_string
