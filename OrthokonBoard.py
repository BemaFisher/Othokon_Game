# Author: Begaiym Fisher
# Date: 5/22/2021
# Description:
#     The board for a two-player game that is played on a 4x4 grid. A player moving one of their pieces
#     orthogonally or diagonally as far as it can go until it hits another piece or the edge of the board.
#     After the piece stops, any opponent pieces on orthogonally adjacent squares are flipped over
#     to its color. A player wins upon making a move that either flips over the remaining opponent pieces or
#     leaves the opponent without a move.

class OrthokonBoard:
    """This class represents the board for a two-player game that is played on a 4x4 grid. The board starts with four
    red pieces on row 0 and four yellow pieces on row 3. A valid move consists of a player moving one of their pieces
    orthogonally or diagonally as far as it can go until it hits another piece or the edge of the board (it must move
    at least one space). After the piece stops, any opponent pieces on orthogonally adjacent squares are flipped over
    to its color. """

    def __init__(self):
        self._current_state = "UNFINISHED"
        self._board = [["R", "R", "R", "R"],
                       ["-", "-", "-", "-"],
                       ["-", "-", "-", "-"],
                       ["Y", "Y", "Y", "Y"]]

        self._active_player = ""
        self._opponent_player = ""

    def get_board(self):
        """ Returns board"""
        return self._board

    def get_current_state(self):
        """Returns current state"""
        return self._current_state

    def print_board(self):
        """Prints board"""
        for row in self._board:
            for slot in row:
                print(slot + " ", end=" ")
            print()
        print("----------")

    def check_win(self):
        """Checks if the game has been won"""
        new_set = set()
        for row in self._board:  # add all items in board to a set
            for slot in row:
                new_set.add(slot)

        # if opponent player not in set, it means active player flipped all the colors
        if self._opponent_player not in new_set:
            if self._active_player == "Y":
                self._current_state = "YELLOW WON"
            else:
                self._current_state = "RED WON"
            return True

    def opponent_player(self):
        """ Determines opponent player"""
        if self._active_player == "Y":
            self._opponent_player = "R"
        else:
            self._opponent_player = "Y"
        print(self._opponent_player)

        
    def make_move(self, current_x, current_y, dest_x, dest_y):
        """ Takes four parameters (current coord and destination coord, checks if the move is legal,
        records the moves, if the game has been won, and returns true"""

        if self._current_state != "UNFINISHED":
            return False
        if self._board[dest_x][dest_y] != "-":  # if slot is taken
            return False
        if self._board[current_x][current_y] == "-":  # only R or Y can make move
            return False
        if (current_x < 0 or current_x > 3) or (current_y < 0 or current_y > 3):  # make sure being moved piece in range
            return False
        if (dest_x < 0 or dest_x > 3) or (dest_y < 0 or dest_y > 3):  # make sure destination slot in range
            return False
        if current_x == dest_x and current_y == dest_y:  # have to move at least one space
            return False

        # if player is moving, make sure the path is clear, also make sure slot above is not empty aka make sure
        # it moves until it hits another player or the wall
        # when player moves up
        if dest_x < current_x and current_y == dest_y:
            if 0 <= current_x - 1 < 4 and 0 <= current_x - 2 < 4:
                if self._board[current_x - 1][current_y] != "-" or self._board[current_x - 2][current_y] != "-":
                    return False
            if 0 <= dest_x - 1 < 4:
                if self._board[dest_x - 1][dest_y] == "-":
                    return False

        # when player is moving down
        if dest_x > current_x and current_y == dest_y:
            if 0 <= current_x + 1 < 4 and 0 <= current_x + 2 < 4:
                if self._board[current_x + 1][current_y] != "-" or self._board[current_x + 2][current_y] != "-":
                    return False
            if 0 <= dest_x + 1 < 4:
                if self._board[dest_x + 1][dest_y] == "-":
                    return False

        # when player is moving right
        if dest_y < current_y and current_x == dest_x:
            if 0 <= current_y - 1 < 4 and 0 <= current_y - 2 < 4:
                if self._board[current_x][current_y - 1] != "-" or self._board[current_x][current_y - 2] != "-":
                    return False
            if 0 <= dest_y - 1 < 4:
                if self._board[dest_x][dest_y - 1] == "-":
                    return False

        # when player is moving left
        if dest_y > current_y and current_x == dest_x:
            if 0 <= current_y + 1 < 4 and 0 <= current_y + 2 < 4:
                if self._board[current_x][current_y + 1] != "-" or self._board[current_x][current_y + 2] != "-":
                    return False
            if 0 <= dest_y + 1 < 4:
                if self._board[dest_x][dest_y + 1] == "-":
                    return False

        # check moves diagonally
        # player moves NE
        if (current_x > dest_x) and (current_y < dest_y):
            if 0 <= current_x - 1 < 4 and 0 <= current_y + 1 < 4:
                if self._board[current_x - 1][current_y + 1] != "-":
                    return False
            if (dest_y - current_y) > 1:
                if 0 <= current_x - 2 < 4 and 0 <= current_y + 2 < 4:
                    if self._board[current_x - 2][current_y + 2] != "-":
                        return False
            if 0 <= dest_x - 1 < 4 and 0 <= dest_y + 1 < 4:
                if self._board[dest_x - 1][dest_y + 1] == "-":
                    return False

        # player moves SW
        if (current_x < dest_x) and (current_y > dest_y):
            if 0 <= current_x + 1 < 4 and 0 <= current_y - 1 < 4:
                if self._board[current_x + 1][current_y - 1] != "-":
                    return False
            if (dest_x - current_x) > 1:
                if 0 <= current_x + 2 < 4 and 0 <= current_y - 2 < 4:
                    if self._board[current_x + 2][current_y - 2] != "-":
                        return False
            if 0 <= dest_x + 1 < 4 and 0 <= dest_y - 1 < 4:
                if self._board[dest_x + 1][dest_y - 1] == "-":
                    return False

        # player moves NW
        if (current_x > dest_x) and (current_y > dest_y):
            if 0 <= current_x - 1 < 4 and 0 <= current_y - 1 < 4:
                if self._board[current_x - 1][current_y - 1] != "-":
                    return False
            if (current_x - current_y) > 1:  # if player moves more than one slot, check the second one too
                if 0 <= current_x - 2 < 4 and 0 <= current_y - 2 < 4:
                    if self._board[current_x - 2][current_y - 2] != "-":
                        return False
            if 0 <= dest_x - 1 < 4 and 0 <= dest_y - 1 < 4:
                if self._board[dest_x - 1][dest_y - 1] == "-":
                    return False

        # player moves SE
        if (current_x < dest_x) and (current_y < dest_y):
            if 0 <= current_x + 1 < 4 and 0 <= current_y + 1 < 4:
                if self._board[current_x + 1][current_y + 1] != "-":
                    return False
            if (dest_x - current_x) > 1:
                if 0 <= current_x + 2 < 4 and 0 <= current_y + 2 < 4:
                    if self._board[current_x + 2][current_y + 2] != "-":
                        return False
            if 0 <= dest_x + 1 < 4 and 0 <= dest_y + 1 < 4:
                if self._board[dest_x + 1][dest_y + 1] == "-":
                    return False
        
        # update active player
        self._active_player = self._board[current_x][current_y]  
        self._board[current_x][current_y] = "-"
        self.print_board()

        # convert orthogonally adjacent opponent's pieces to active player's color
        if 0 <= dest_x - 1 < 4:
            if self._board[dest_x - 1][dest_y] != self._active_player and self._board[dest_x - 1][dest_y] != "-":  # up
                self._board[dest_x - 1][dest_y] = self._active_player

        if 0 <= dest_x + 1 < 4:
            if self._board[dest_x + 1][dest_y] != self._active_player and self._board[dest_x + 1][
                dest_y] != "-":  # down
                self._board[dest_x + 1][dest_y] = self._active_player

        if 0 <= dest_y - 1 < 4:
            if self._board[dest_x][dest_y - 1] != self._active_player and self._board[dest_x][
                dest_y - 1] != "-":  # left
                self._board[dest_x][dest_y - 1] = self._active_player

        if 0 <= dest_y + 1 < 4:
            if self._board[dest_x][dest_y + 1] != self._active_player and self._board[dest_x][
                dest_y + 1] != "-":  # right
                self._board[dest_x][dest_y + 1] = self._active_player

        self.print_board()
        self.opponent_player()
        self.check_win()

        return True


