import random
import itertools
import sys

board = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

ttt = {('A', 'I'):'E',('C', 'G'):'E',('A', 'E'):'I',
       ('E', 'I'):'A',('C', 'E'):'G',('E', 'G'):'C',
       ('A', 'B'):'C',('B', 'C'):'A',('D', 'E'):'F',
       ('E', 'F'):'D',('G', 'H'):'I',('H', 'I'):'G',
       ('A', 'D'):'G',('D', 'G'):'A',('B', 'E'):'H',
       ('E', 'H'):'B',('C', 'F'):'I',('F', 'I'):'C',
       ('A', 'G'):'D',('B', 'H'):'E',('C', 'I'):'F',
       ('A', 'C'):'B',('D', 'F'):'E',('G', 'I'):'H',
       }

class Player(object):
    def __init__(self, name):
        self.name = name
        self.moves = []

    def add_moves(self, moves):
        self.moves.append(move)

def check_for_winners(player):
    combinations = list(itertools.combinations(player.moves, 2))
    for combo in combinations:
        sorted_combo = tuple(sorted(combo))
        if sorted_combo in ttt:
            winner = ttt[sorted_combo]
            if winner in board:
                return winner
    return None

def take_a_turn(player, opponent):    
    move = check_for_winners(opponent)
    if move:
        play(move, opponent)        
    else:    
        move = check_for_winners(player)
        if move:
            play(move, opponent)            
        else:            
            play_randomly(opponent)

def play(move, player):
    check_if_won(player)    
    make_move(player, move)    

def make_move(player, move):    
    player.moves.append(move)  
    board.remove(move)              
 
def check_if_won(player):
    win_move = check_for_winners(player)
    if win_move:
        print "{} moves {} and wins!".format(player.name, win_move)
        sys.exit(0)    
    
def play_randomly(player):
    move = random.choice(board)
    make_move(player, move)    

if __name__ == '__main__':

    player = Player("Human")
    opponent = Player("Computer")
    while True:
        print "board is {}".format(board)
        print "player moves {}".format(player.moves)
        print "opponenent moves {}".format(opponent.moves)
        player_move = raw_input("please make a move ")
        play(player_move, player)       
        take_a_turn(player, opponent)
       
        

    
