import random
import itertools


grid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

user_moves = []
comp_moves = []
ttt_possible = []
comb_step3 = []

ttt = {('A', 'I'):'E', ('I', 'A'):'E', ('C', 'G'):'E', ('G', 'C'):'E', ('A', 'E'): 'I', ('E', 'A'): 'I', 
         ('E', 'I'):'A', ('I', 'E'):'A', ('C', 'E'):'G', ('E', 'C'):'G', ('E', 'G'):'C',('G', 'E'):'C', 
         ('A', 'B'):'C', ('B', 'A'):'C', ('B', 'C'):'A', ('C', 'B'):'A', ('D', 'E'):'F', ('E', 'D'):'F',
         ('E', 'F'):'D', ('F', 'E'):'D', ('G', 'H'):'I', ('H', 'G'):'I', ('H', 'I'):'G', ('I','H'):'G', 
         ('A', 'D'):'G', ('D', 'A'):'G', ('D', 'G'):'A', ('G', 'D'):'A', ('B', 'E'):'H', ('E', 'B'):'H',
         ('E', 'H'):'B', ('H', 'E'):'B', ('C', 'F'):'I', ('F', 'C'):'I', ('F', 'I'):'C', ('I', 'F'):'C',
         ('A', 'G'):'D', ('G', 'A'):'D', ('B', 'H'):'E', ('H', 'B'):'E', ('C', 'I'):'F', ('I', 'C'):'F',
         ('A', 'C'):'B', ('C', 'A'):'B', ('D', 'F'):'E', ('F', 'D'):'E', ('G', 'I'):'H', ('I', 'G'):'H'}

def main():
    #user move 1   
    user_move1 = raw_input("Enter your first move ")    
    adjust_grid(user_move1)
    moves_made(user_move1, user_moves)    
    
    #comp move 1
    comp_move1 = random.choice(grid)
    print "Computer move #1 is: " + comp_move1
    adjust_grid(comp_move1)
    moves_made(comp_move1, comp_moves)
    
    update(grid, user_moves, comp_moves) 
        
    #user move 2
    user_move2 = raw_input("Enter your next move ") 
    adjust_grid(user_move2)
    moves_made(user_move2, user_moves)       
    
    #comp move 2
    user_moves_tup = tuple(user_moves)    
    if user_moves_tup in ttt:
        if ttt[user_moves_tup] in grid:
            comp_move2 = ttt[user_moves_tup]
            print "Computer move #2 is: " + comp_move2     
        
        elif ttt[user_moves_tup] not in grid:
            comp_move2 = random.choice(grid)
            print "Computer move #2 is: " + comp_move2            
    else:
        comp_move2 = random.choice(grid)
        print "Computer move #2 is: " + comp_move2      
            
    adjust_grid(comp_move2)
    moves_made(comp_move2, comp_moves)
            
    update(grid, user_moves, comp_moves)   
    
    #user move 3
    user_move3 = raw_input("Enter your next move ") 
    adjust_grid(user_move3)
    moves_made(user_move3, user_moves)
    
    #comp move 3
    #check for possible comp win
    comp_moves_tup = tuple(comp_moves) 
    if comp_moves_tup in ttt:
        if ttt[comp_moves_tup] in grid:
            comp_move3 = ttt[comp_moves_tup]
            print "Computer move #2 is: " + comp_move3
            print "COMPUTER WINS"
            raise SystemExit
                        
    #check for block of possible user win
    ttt_builder(user_moves)         
    
    if len(ttt_possible) > 0: 
        comp_move3 = ttt_possible[0]
        print "Computer move #3 is: " + comp_move3 
    
    if len(ttt_possible) == 0:
        comp_move3 = random.choice(grid)
        print "Computer move #3 is: " + comp_move3 
        
    adjust_grid(comp_move3)
    moves_made(comp_move3, comp_moves)
    del ttt_possible[:]
            
    update(grid, user_moves, comp_moves)    
        
    #user move 4
    user_move4 = raw_input("Enter your next move ")  
    moves_made(user_move4, user_moves)
        
    #check to see if user wins
    ttt_builder_userwin(user_moves, user_move4)
    
    adjust_grid(user_move4)                    
      
    #comp move 4
    #check to see if comp can win
    ttt_builder(comp_moves)    
    
    if len(ttt_possible) > 0:
        comp_move4 = ttt_possible[0]
        print "COMPUTER WINS! Computer move #4 is: " + comp_move4 
        raise SystemExit
     
    #check for mandatory block of possible user win       
    ttt_builder(user_moves)
    
    if len(ttt_possible) > 0:
        comp_move4 = ttt_possible[0]
        print "Computer move #4 is: " + comp_move4 
    
    if len(ttt_possible) == 0:
        comp_move4 = random.choice(grid)
        print "Computer move #4 is: " + comp_move4 
        
    adjust_grid(comp_move4)
    moves_made(comp_move4, comp_moves)
    del ttt_possible[:] 
    
    update(grid, user_moves, comp_moves) 
    
    #user move 5
    user_move5 = raw_input("Enter your next move ")    
    moves_made(user_move5, user_moves)
    
    #check to see if user wins
    ttt_builder_userwin(user_moves, user_move5)  
    
    adjust_grid(user_move5)
    
    update(grid, user_moves, comp_moves) 
    
    print "This game is a DRAW" 
    
def adjust_grid(move):
    grid.remove(move)
    
def moves_made(move, moves_made):
    moves_made.append(move)
    
def update(grid, user_moves, comp_moves):
    print "Available spots in the grid now are: " + str(grid)
    print "You have moved: " + str(user_moves)
    print "Computer has moved: " + str(comp_moves)    
    
def ttt_builder_userwin(moves_made, move):    
    pos_1, pos_2, pos_3 = moves_made[0], moves_made[1], moves_made[2]
    try: 
        pos_4 = moves_made[3]
    except IndexError:
        pos_4 = ""
    comb_step1 = pos_1 + pos_2 + pos_3 + pos_4
    comb_step2 = itertools.combinations(comb_step1, 2)
    comb_step3 = list(comb_step2)      
    return user_win(comb_step3, move)
    
def user_win(comb_step3, move): 
    for b in comb_step3:
        if b in ttt:
            if ttt[b] in grid:
                if move == ttt[b]:
                    print "YOU WIN"
                    raise SystemExit    
    
def ttt_builder(moves_made):    
    pos_1, pos_2, pos_3 = moves_made[0], moves_made[1], moves_made[2]
    try: 
        pos_4 = moves_made[3]
    except IndexError:
        pos_4 = ""
    comb_step1 = pos_1 + pos_2 + pos_3 + pos_4
    comb_step2 = itertools.combinations(comb_step1, 2)
    comb_step3 = list(comb_step2)      
    return check_ttt(comb_step3)
    
def check_ttt(comb_step3):    
    for b in comb_step3:
        if b in ttt:            
            if ttt[b] in grid:                
                ttt_possible.append(ttt[b])                
    return ttt_possible
    
if __name__ == '__main__':
    main()