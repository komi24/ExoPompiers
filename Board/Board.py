import random
import numpy as np


class Board:
    def __init__(self, xmax, ymax, nb_feu):
        self._xmax=xmax
        self._ymax=ymax
        self._liste_feu = [(random.randint(0,xmax-1),random.randint(0,ymax-1)) for i in range(nb_feu)]

    def is_feu(self, x, y):
        return len([i for i in self._liste_feu if i == (x,y)]) > 0
    def get_fires(self):
        return self._liste_feu
    def eteindre(self, position):
    	self._liste_feu = [feu for feu in self._liste_feu if feu != position]
    def print(self):
        disp = np.zeros((self._xmax, self._ymax))
        for feu in self._liste_feu:
            disp[feu]=1
        return disp