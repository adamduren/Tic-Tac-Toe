from .utils import erase_last_line

infinity = float('inf')


class Player(object):
    name = None
    mark = None

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def make_turn_decision(self, state, board):
        decision = int(raw_input())

        # Clean up after ourselves
        erase_last_line()

        return decision


class AiPlayer(Player):

    def make_turn_decision(self, state, board):
        player = board.to_move(state)

        def max_value(state):
            if board.is_terminal_state(state):
                return board.utility(state, player.mark)

            value = -infinity

            for a in board.get_actions(state):
                value = max(value, min_value(board.result(state, a)))

            return value

        def min_value(state):
            if board.is_terminal_state(state):
                return board.utility(state, player.mark)

            value = infinity

            for a in board.get_actions(state):
                value = min(value, max_value(board.result(state, a)))

            return value

        max_v = -infinity
        max_a = -1

        actions = board.get_actions(state)

        for a in actions:
            cur_value = min_value(board.result(state, a))

            if cur_value > max_v:
                max_v = cur_value
                max_a = a

        decision = max_a

        return decision
