from django.test import TestCase

from ..board import Board, PLAYER_BOARD_MARKS
from ..player import Player, AiPlayer


class TestBoardStateOnCreation(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.board = Board()

    def setUp(self):
        self.state = {
            'board': None,
            'current_player': Player('Human', PLAYER_BOARD_MARKS[0]),
            'next_player': AiPlayer('Ai', PLAYER_BOARD_MARKS[1])
        }

    def test_initial_board_state_no_init(self):
        state = self.board.get_initial_state()

        initial_board = [
            None, None, None,
            None, None, None,
            None, None, None
        ]

        self.assertEqual(state['board'], initial_board)

    def test_initial_board_state_valid(self):
        initial_board = [
            None, None, None,
            None, 1, None,
            None, None, None
        ]

        self.state['board'] = initial_board
        state = self.board.get_initial_state(self.state)

        self.assertEqual(state['board'], initial_board)

    def test_initial_board_state_invalid_column_dimensions(self):

        initial_board = [
            None, None,
            None, None, None,
            None, None, None
        ]

        self.state['board'] = initial_board
        state_func = self.board.get_initial_state

        self.assertRaises(ValueError, state_func, self.state)

    def test_initial_board_state_invalid_row_dimensions(self):

        initial_board = [
            None, None, None,
            None, None, None
        ]

        self.state['board'] = initial_board
        state_func = self.board.get_initial_state

        self.assertRaises(ValueError, state_func, self.state)

    def test_initial_board_state_invalid_cell_value(self):

        initial_board = [
            None, None, None,
            None, None, None,
            None, 5, None
        ]

        self.state['board'] = initial_board
        state_func = self.board.get_initial_state

        self.assertRaises(ValueError, state_func, self.state)
