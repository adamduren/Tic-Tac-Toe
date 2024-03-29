from .board import Board


class ConsoleGame(object):
    def start(self, state=None):
        board = Board()
        state = board.get_initial_state(state)

        while True:
            print(board.display(state))

            if board.is_terminal_state(state):
                break

            player = board.to_move(state)

            print('{}\'s turn'.format(player.name))

            try:
                state = board.result(state, player.make_turn_decision(state, board))
            except ValueError as e:
                print('{} Would you like to continue playing? '.format(e.message))

                if raw_input() not in ['y', 'yes']:
                    break

        if board.determine_winner(state):
            print('{} Wins!'.format(player.name))
        else:
            print('It\'s a draw')
