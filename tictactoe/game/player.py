from .utils import erase_last_line


class Player(object):
    name = None
    mark = None

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def make_turn_decision(self, board):
        decision = int(raw_input())

        # Clean up after ourselves
        erase_last_line()

        return decision


# Todo: implement AI logic
class AiPlayer(Player):
    pass
