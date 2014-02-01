from django.test import TestCase

from .. import Board


class TestBoardCreation(TestCase):

    def test_initial_board_state_no_init(self):
        board = Board()

        initial_board = [
            None, None, None,
            None, None, None,
            None, None, None
        ]

        self.assertEqual(board.board_state, initial_board)

    def test_initial_board_state_valid(self):
        initial_board = [
            None, None, None,
            None, 1, None,
            None, None, None
        ]

        board = Board(initial_board)

        self.assertEqual(board.board_state, initial_board)

    def test_initial_board_state_invalid_column_dimensions(self):

        initial_board = [
            None, None,
            None, None, None,
            None, None, None
        ]

        self.assertRaises(ValueError, Board, initial_board)

    def test_initial_board_state_invalid_row_dimensions(self):

        initial_board = [
            None, None, None,
            None, None, None
        ]

        self.assertRaises(ValueError, Board, initial_board)

    def test_initial_board_state_invalid_cell_value(self):

        initial_board = [
            None, None, None,
            None, None, None,
            None, 5, None
        ]

        self.assertRaises(ValueError, Board, initial_board)
