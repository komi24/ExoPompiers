from Board.Board import Board
from Pompier.Pompier import Pompier
from itertools import product
import numpy as np
import random
import time
import os

# self.board = Board(8,8,5)
# pompier1 = Pompier(1,(1,2), self.board)
# pompier2 = Pompier(2,(5,6), self.board)
#self.pompiers = [pompier1, pompier2]
class BoardManager():
    def __init__(self,xmax,ymax,nb_feux, nb_pompiers):
        self.board = Board(xmax,ymax,nb_feux)
        self.pompiers = [Pompier(i, (random.randint(0,xmax-1),random.randint(0,xmax-1)), self.board) for i in range(nb_pompiers)]
    
    def liste_available_pompier(self):
        return [pompier for pompier in self.pompiers if not pompier.is_busy()]

    def is_allready_taken(self, position):
        return len([pomp for pomp in self.pompiers if pomp.is_my_position(position)]) > 1

    def distance(self, pos1, pos2):
        #print(pos1[0]-pos2[0] + pos1[1]-pos2[1])
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

    def find_closest_fire(self, pompier, board):
        liste_feu = [fire for fire in board.get_fires() if not self.is_allready_taken(fire)]
        if(len(liste_feu) >0):
            result = liste_feu[0]
            for feu in liste_feu:
                if (self.distance(feu, pompier.get_position()) < self.distance(result, pompier.get_position())):
                    result = feu
            return result
        else:
            return None

    def find_next_position(self, pompier,board):
        destination = self.find_closest_fire(pompier,board)
        #print("Position pompier : %s, destination : %s"%(str(pompier.get_position()),str(destination)))
        if destination != None:
            delta = (destination[0]-pompier.get_position()[0], destination[1]-pompier.get_position()[1])
            if(delta[0]==0 and delta[1] == 0):
                #print("eteindre : delta : %s"%(str(delta)))
                pompier.eteindre()
            elif (abs(delta[0]) > abs(delta[1])):
                update_x = pompier.get_position()[0] + abs(delta[0])/delta[0]
                pompier.deplacer((int(update_x),pompier.get_position()[1]))
            else:
                update_y = pompier.get_position()[1] + abs(delta[1])/delta[1]
                pompier.deplacer((pompier.get_position()[0],int(update_y)))

    def get_state(self):
        state= self.board.print()
        for pomp in self.pompiers:
            state[pomp.get_position()]=2
        return state

    def print_line(self, arr):
        result = ""
        for i in arr:
            result+=i
        print(result)
    def display_state(self):
        #print("Position pompier : %s"%(str([pompier.get_position() for pompier in self.pompiers])))
        #print("Position feu : %s"%(str(self.board.get_fires())))
        os.system('cls')
        print("Mes petits pompiers éteignent les feux \n \n")
        state = self.get_state()
        for i in range(state.shape[0]):
            self.print_line(['     ']+[' ' if x==0 else ('x' if x ==1 else 'i') for x in state[i,:]])

    def run(self):    
        self.display_state()
        for pompier in self.liste_available_pompier():
            self.find_next_position(pompier, self.board)
        for pompier in self.pompiers:    
            pompier.run_one_step()

bm = BoardManager(20,20,6,3)
for i in range(30):
    bm.run()
    time.sleep(1)