# Author: Begaiym Fisher
# Date: 5/22/2021
# Description:

class OrthokonBoard:
    """ """

    def __init__(self):
        self._current_state = "UNFINISHED"
        self._board = [["R", "R", "R", "R"],
                       ["-", "-", "-", "-"],
                       ["-", "-", "-", "-"],
                       ["Y", "Y", "Y", "Y"]]

        self._active_player = " "

    def get_board(self):
        return self._board

    def get_current_state(self):
        """:returns current state"""
        return self._current_state

    def print_board(self):
        """Prints board"""
        for row in self._board:
            for slot in row:
                print(slot + " ", end=" ")
            print()
        print("----------")

    def make_move(self, current_x, current_y, dest_x, dest_y):
        """

        :return:
        """

        if self._current_state != "UNFINISHED":
            return False
        if self._board[dest_x][dest_y] != "-":  # if slot is taken
            return False
        if (current_x < 0 or current_x > 3) or (current_y < 0 or current_y > 3):  # make sure being moved piece in range
            return False
        if (dest_x < 0 or dest_x > 3) or (dest_y < 0 or dest_y > 3):  # make sure destination slot in range
            return False
        if current_x == dest_x and current_y == dest_y:  # have to move at least one space
            return False

        self._board[dest_x][dest_y] = self._board[current_x][current_y]
        self._active_player = self._board[dest_x][dest_y]  # now my active player is whichever current letter
        self._board[current_x][current_y] = "-"
        self.print_board()

        if 0 <= dest_x - 1 < 4:
            if self._board[dest_x - 1][dest_y] != self._active_player and self._board[dest_x - 1][dest_y] != "-":  # down
                self._board[dest_x - 1][dest_y] = self._active_player

        if 0 <= dest_x + 1 < 4:
            if self._board[dest_x + 1][dest_y] != self._active_player and self._board[dest_x + 1][dest_y] != "-":  # down
                self._board[dest_x + 1][dest_y] = self._active_player

        if 0 <= dest_y - 1 < 4:
            if self._board[dest_x][dest_y - 1] != self._active_player and self._board[dest_x][dest_y - 1] != "-":  # left
                self._board[dest_x][dest_y - 1] = self._active_player

        if 0 <= dest_y + 1 < 4:
            if self._board[dest_x][dest_y + 1] != self._active_player and self._board[dest_x][dest_y + 1] != "-":  # right
                self._board[dest_x][dest_y + 1] = self._active_player

        self.print_board()


board = OrthokonBoard()
# board.make_move(3, 2, 1, 0)  # The yellow player moves a piece diagonally, flipping one red piece to yellow
# board.make_move(0, 2, 2, 0)  # The red player moves a piece diagonally, flipping two yellow pieces to red

print(board.make_move(3, 0, 1, 0))
# board.make_move(0, 3, 2, 3)
board.make_move(3, 1, 1, 1)
board.make_move(3, 2, 1, 2)
board.make_move(3, 3, 1, 3)
print(board.get_current_state())