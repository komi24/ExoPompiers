class Pompier:
    def __init__(self, id, position, board):
        self._id= id
        self._position= position
        self._next_position= position
        self._busy= 0
        self._board= board
    def deplacer(self, position):
        self._next_position= position
    def eteindre(self):
        self._busy = 5
    def run_one_step(self):
        """
            Execute les directives du tour courant
        """
        #print("busy %d"%self._busy)
        if (self._busy > 1):
            self._busy -= 1
        elif(self._busy == 1):
            self._busy = 0
            self._board.eteindre(self._position)
        else:
            self._position= self._next_position
    def is_busy(self):
        return self._busy != 0
    def get_position(self):
        return self._position
    def is_my_position(self, position):
        return self._position == position
    