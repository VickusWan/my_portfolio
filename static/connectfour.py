import numpy as np
from pyweb import pydom
from js import document

class connect4_board():
        
    def __init__(self):
        self.num_rows = 6
        self.num_cols = 7
        self.board = np.zeros((self.num_rows, self.num_cols), dtype=int)
        self.board[5, 3] = -1
        
    def get_state(self):
        return self.board
        
    def is_end(self):
        return 0 not in self.board

    def play_move(self, player, col):
        for i in range(self.num_rows-1, -1, -1):
            if self.board[i, col] == 0:
                self.board[i, col] = player
                return i
        return 'CELL ALREADY FULL'

    def get_valid_actions(self):
        actions = []
        for col in range(self.num_cols):
            if self.board[0, col] == 0:
                actions.append(col)
        return actions
    
    def deep_copy(self):
        new_instance = connect4_board()
        new_instance.board = np.copy(self.board)
        return new_instance
    
    def reset(self):
        self.board = np.zeros((self.num_rows, self.num_cols), dtype=int)     
        
    def insert0(self, event):
        row = self.play_move(-1, 0)
        location = 'cell'+str(row)+'0'
        document.getElementById(location).style.backgroundColor = 'red'
        
        (col, _) = alphabeta(self, 4, float('-inf'), float('inf'), True)
        row = self.play_move(1, col)
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'yellow'
        print(location, col, 'AI=', ai_location)
        
    def insert1(self, event):
        row = self.play_move(-1, 1)
        location = 'cell'+str(row)+'1'
        document.getElementById(location).style.backgroundColor = 'red'
        
        (col, _) = alphabeta(self, 4, float('-inf'), float('inf'), True)
        row = self.play_move(1, col)
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'yellow'
        print(location, col, 'AI=', ai_location)
        
    def insert2(self, event):
        row = self.play_move(-1, 2)
        location = 'cell'+str(row)+'2'
        document.getElementById(location).style.backgroundColor = 'red'
        
        (col, _) = alphabeta(self, 4, float('-inf'), float('inf'), True)
        row = self.play_move(1, col)
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'yellow'
        print(location, col, 'AI=', ai_location)
        
    def insert3(self, event):
        row = self.play_move(-1, 3)
        location = 'cell'+str(row)+'3'
        document.getElementById(location).style.backgroundColor = 'red'
        
        (col, _) = alphabeta(self, 4, float('-inf'), float('inf'), True)
        row = self.play_move(1, col)
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'yellow'
        print(location, col, 'AI=', ai_location)
        
    def insert4(self, event):
        row = self.play_move(-1, 4)
        location = 'cell'+str(row)+'4'
        document.getElementById(location).style.backgroundColor = 'red'
        
        (col, _) = alphabeta(self, 4, float('-inf'), float('inf'), True)
        row = self.play_move(1, col)
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'yellow'
        print(location, col, 'AI=', ai_location)
        
    def insert5(self, event):
        row = self.play_move(-1, 5)
        location = 'cell'+str(row)+'5'
        document.getElementById(location).style.backgroundColor = 'red'
        
        (col, _) = alphabeta(self, 4, float('-inf'), float('inf'), True)
        row = self.play_move(1, col)
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'yellow'
        print(location, col, 'AI=', ai_location)
        
    def insert6(self, event):
        row = self.play_move(-1, 6)
        location = 'cell'+str(row)+'6'
        document.getElementById(location).style.backgroundColor = 'red'
        
        (col, _) = alphabeta(self, 4, float('-inf'), float('inf'), True)
        row = self.play_move(1, col)
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'yellow'
        print(location, col, 'AI=', ai_location)

def alphabeta(board, depth, alpha, beta, maximizingPlayer):
    if maximizingPlayer:
        player = 1
    else:
        player = -1
        
    if depth == 0 or board.is_end():
        score = heuristic(board, player) + heuristic(board, -player)
        return (None, score)
    
    if maximizingPlayer:
        value = float('-inf')
        column = None
        
        for action in board.get_valid_actions():
            temp = board.deep_copy()
            temp.play_move(player, action)
            
            _ , new_score = alphabeta(temp, depth-1, alpha, beta, False)
             
#           maximzing score
            if new_score > value:
                value = new_score
                column = action
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return (column, value)
    
    else:
        value = float('inf')
        column = None

        for action in board.get_valid_actions():
            temp = board.deep_copy()
            temp.play_move(player, action)

            _, new_score = alphabeta(temp, depth-1, alpha, beta,  True)
                         
            # minimizing score
            if new_score < value:
                value = new_score
                column = action
            beta = min(value, beta)
            if beta <= alpha:
                break
        return (column, value)
   
def heuristic(game, player):
    num_rows = 6
    num_cols = 7
    score = 0
    board = game.get_state()
    
    if board[5, 3] == player:
        score += 1
    else:
        score -= 1
    # Horizontal
    for i in range(num_rows):
        for num in range(4):
            if (np.all(board[i,num:num+4]==0)):
                continue
            elif (np.all(board[i,num:num+4]==player)):
                  score = float('inf')
            elif ((board[i,num:num+4] == player).sum() == 3) and ((board[i,num:num+4] == 0).sum() == 1):
                  score += 10       
            elif ((board[i,num:num+4] == player).sum() == 2) and ((board[i,num:num+4] == 0).sum() == 2):
                  score += 1              
            elif ((board[i,num:num+4] == -player).sum() == 1):
                  score += 0
    # Vertical
    for i in range(num_cols):
        for num in range(3):
            if (np.all(board[num:num+4,i]==0)):
                continue    
            elif (np.all(board[num:num+4,i]==player)):
                  score = float('inf')
            elif ((board[num:num+4,i] == player).sum() == 3) and ((board[num:num+4,i] == 0).sum() == 1):
                  score += 10        
            elif ((board[num:num+4,i] == player).sum() == 2) and ((board[num:num+4,i] == 0).sum() == 2):
                  score += 1              
            elif ((board[num:num+4,i] == -player).sum() == 1):
                  score += 0
    # Positive diagonal
    for i in range(num_rows-3):
        for j in range(3, num_cols):
            diagonal = np.array([board[i, j], board[i+1, j-1], board[i+2, j-2], board[i+3, j-3]])
            if (np.all(diagonal==0)):
                continue 
            elif (np.all(diagonal==player)):
                  score = float('inf')
            elif ((diagonal == player).sum() == 3) and ((diagonal == 0).sum() == 1):
                if (board[i+1, j-1]==player) and (board[i+1, j-2]==player) and (board[i+1, j-3]==player):
                    score += 100
                else:
                    score += 10             
            elif ((diagonal == player).sum() == 2) and ((diagonal == 0).sum() == 2):
                  score += 1             
            elif ((diagonal == -player).sum() == 1):
                  score += 0        
    
    # Negative diagonal
    for i in range(num_rows-3):
        for j in range(3, -1, -1):
            diagonal = np.array([board[i, j], board[i+1, j+1], board[i+2, j+2], board[i+3, j+3]])
            if (np.all(diagonal==0)):
                continue
            elif (np.all(diagonal==player)):
                  score = float('inf')
            elif ((diagonal == player).sum() == 3) and ((diagonal == 0).sum() == 1):
                if (board[i+1, j+1]==player) and (board[i+1, j+2]==player) and (board[i+1, j+3]==player):
                    score += 100
                else:
                    score += 10
                    
            elif ((diagonal == player).sum() == 2) and ((diagonal == 0).sum() == 2):
                  score += 1             
            elif ((diagonal == -player).sum() == 1):
                  score += 0
    return player*score
    
GAME = connect4_board()