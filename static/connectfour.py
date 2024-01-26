import numpy as np
from pyweb import pydom
from js import document

class connect4_board():
        
    def __init__(self):
        self.num_rows = 6
        self.num_cols = 7
        self.board = np.zeros((self.num_rows, self.num_cols), dtype=int)
        self.user_starts = None
    
    def is_empty_board(self):
        return np.all(self.board == 0)
    
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
        
        
    def check_winner(self, game, player):
        num_rows = 6
        num_cols = 7
        board = game.get_state()
        for i in range(num_rows):
            for num in range(4):
                if (np.all(board[i,num:num+4]==player)):
                    return True
                
        for i in range(num_cols):
            for num in range(3):
                if (np.all(board[num:num+4,i]==player)):
                    return True
                
        for i in range(num_rows-3):
            for j in range(3, num_cols):
                diagonal = np.array([board[i, j], board[i+1, j-1], board[i+2, j-2], board[i+3, j-3]])
                if (np.all(diagonal==player)):
                    return True
                
        for i in range(num_rows-3):
            for j in range(3, -1, -1):
                diagonal = np.array([board[i, j], board[i+1, j+1], board[i+2, j+2], board[i+3, j+3]])
                if (np.all(diagonal==player)):
                    return True
        return False    
        
    def me_first(self, event):
        self.user_starts = True
        return
    
    def ai_first(self, event):
        self.user_starts = False
        (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), True, 1)
        row = self.play_move(1, col)
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'red'
    
    def newgame(self, event):
        self.user_starts = None
        self.board = np.zeros((self.num_rows, self.num_cols), dtype=int)
        for i in range(6):
            for j in range(7):
                location = 'cell'+str(i)+str(j)
                document.getElementById(location).style.backgroundColor = 'white'
        document.getElementById('winner').innerText = ''
        return      
        
    def insert0(self, event):
        if self.user_starts is None:
            return
        
        if self.user_starts:
            player = 1
        else:
            player = -1
        
        if self.check_winner(self, 1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        elif self.check_winner(self, 1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        
        row = self.play_move(player, 0)
        location = 'cell'+str(row)+'0'
        document.getElementById(location).style.backgroundColor = 'yellow'
        
        if self.user_starts:
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), False, -1)
            row = self.play_move(-1, col)
        else: 
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), True, 1)
            row = self.play_move(1, col)
        
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'red'
        if self.check_winner(self, player):
            document.getElementById('winner').innerText = 'Player wins!'
            return
        
    def insert1(self, event):
        if self.user_starts is None:
            return
        
        if self.user_starts:
            player = 1
        else:
            player = -1
        
        if self.check_winner(self, 1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        elif self.check_winner(self, 1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        
        row = self.play_move(player, 1)
        location = 'cell'+str(row)+'1'
        document.getElementById(location).style.backgroundColor = 'yellow'
        
        if self.user_starts:
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), False, -1)
            row = self.play_move(-1, col)
        else: 
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), True, 1)
            row = self.play_move(1, col)
        
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'red'
        if self.check_winner(self, player):
            document.getElementById('winner').innerText = 'Player wins!'
            return
        
    def insert2(self, event):
        if self.user_starts is None:
            return
        
        if self.user_starts:
            player = 1
        else:
            player = -1
        
        if self.check_winner(self, 1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        elif self.check_winner(self, 1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        
        row = self.play_move(player, 2)
        location = 'cell'+str(row)+'2'
        document.getElementById(location).style.backgroundColor = 'yellow'
        
        if self.user_starts:
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), False, -1)
            row = self.play_move(-1, col)
        else: 
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), True, 1)
            row = self.play_move(1, col)
        
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'red'
        if self.check_winner(self, player):
            document.getElementById('winner').innerText = 'Player wins!'
            return
        
    def insert3(self, event):
        if self.user_starts is None:
            return
        
        if self.user_starts:
            player = 1
        else:
            player = -1
        
        if self.check_winner(self, 1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        elif self.check_winner(self, 1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        
        row = self.play_move(player, 3)
        location = 'cell'+str(row)+'3'
        document.getElementById(location).style.backgroundColor = 'yellow'
        
        if self.user_starts:
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), False, -1)
            row = self.play_move(-1, col)
        else: 
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), True, 1)
            row = self.play_move(1, col)
        
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'red'
        if self.check_winner(self, player):
            document.getElementById('winner').innerText = 'Player wins!'
            return
        
    def insert4(self, event):
        if self.user_starts is None:
            return
        
        if self.user_starts:
            player = 1
        else:
            player = -1
        
        if self.check_winner(self, 1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        elif self.check_winner(self, 1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        
        row = self.play_move(player, 4)
        location = 'cell'+str(row)+'4'
        document.getElementById(location).style.backgroundColor = 'yellow'
        
        if self.user_starts:
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), False, -1)
            row = self.play_move(-1, col)
        else: 
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), True, 1)
            row = self.play_move(1, col)
        
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'red'
        if self.check_winner(self, player):
            document.getElementById('winner').innerText = 'Player wins!'
            return
        
    def insert5(self, event):
        if self.user_starts is None:
            return
        
        if self.user_starts:
            player = 1
        else:
            player = -1
        
        if self.check_winner(self, 1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        elif self.check_winner(self, 1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        
        row = self.play_move(player, 5)
        location = 'cell'+str(row)+'5'
        document.getElementById(location).style.backgroundColor = 'yellow'
        
        if self.user_starts:
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), False, -1)
            row = self.play_move(-1, col)
        else: 
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), True, 1)
            row = self.play_move(1, col)
        
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'red'
        if self.check_winner(self, player):
            document.getElementById('winner').innerText = 'Player wins!'
            return
        
    def insert6(self, event):
        if self.user_starts is None:
            return
        
        if self.user_starts:
            player = 1
        else:
            player = -1
        
        if self.check_winner(self, 1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'Player wins!'
            return
        elif self.check_winner(self, -1) and self.user_starts is True:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        elif self.check_winner(self, 1) and self.user_starts is False:
            document.getElementById('winner').innerText = 'AI wins!'
            return
        
        row = self.play_move(player, 6)
        location = 'cell'+str(row)+'6'
        document.getElementById(location).style.backgroundColor = 'yellow'
        
        if self.user_starts:
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), False, -1)
            row = self.play_move(-1, col)
        else: 
            (col, score) = alphabeta(self, 4, float('-inf'), float('inf'), True, 1)
            row = self.play_move(1, col)
        
        ai_location = 'cell'+str(row)+str(col)
        document.getElementById(ai_location).style.backgroundColor = 'red'
        if self.check_winner(self, player):
            document.getElementById('winner').innerText = 'Player wins!'
            return

def alphabeta(board, depth, alpha, beta, maximizingPlayer, player):    
    if depth == 0 or board.is_end():
        score = heuristic(board, player)
        return (None, score)
    
    if maximizingPlayer:
        value = float('-inf')
        column = None
        
        for action in board.get_valid_actions():
            temp = board.deep_copy()
            temp.play_move(abs(player), action)
            
            _ , new_score = alphabeta(temp, depth-1, alpha, beta, False, player)
            
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
            temp.play_move(-abs(player), action)

            _, new_score = alphabeta(temp, depth-1, alpha, beta,  True, player)
                                     
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
                  score = 10000
            elif ((board[i,num:num+4] == player).sum() == 3) and ((board[i,num:num+4] == 0).sum() == 1):
                  score += 11       
            elif ((board[i,num:num+4] == player).sum() == 2) and ((board[i,num:num+4] == 0).sum() == 2):
                  score += 1              
            elif ((board[i,num:num+4] == -player).sum() == 1):
                  score += 0
            # If opponent has 3 in a row
            if ((board[i,num:num+4] == -player).sum() == 4):
                  score -= 1000
            elif ((board[i,num:num+4] == -player).sum() == 3):
                  score -= 10
    # Vertical
    for i in range(num_cols):
        for num in range(3):
            if (np.all(board[num:num+4,i]==0)):
                continue    
            elif (np.all(board[num:num+4,i]==player)):
                  score = 10000
            elif ((board[num:num+4,i] == player).sum() == 3) and ((board[num:num+4,i] == 0).sum() == 1):
                  score += 11      
            elif ((board[num:num+4,i] == player).sum() == 2) and ((board[num:num+4,i] == 0).sum() == 2):
                  score += 1              
            elif ((board[num:num+4,i] == -player).sum() == 1):
                  score += 0
            # If opponent has 3 in a row
            if ((board[num:num+4,i] == -player).sum() == 4):
                score -= 1000
            elif ((board[num:num+4,i] == -player).sum() == 3):
                score -= 10
    # Positive diagonal
    for i in range(num_rows-3):
        for j in range(3, num_cols):
            diagonal = np.array([board[i, j], board[i+1, j-1], board[i+2, j-2], board[i+3, j-3]])
            if (np.all(diagonal==0)):
                continue 
            elif (np.all(diagonal==player)):
                  score = 10000
            elif ((diagonal == player).sum() == 3) and ((diagonal == 0).sum() == 1):
                if (board[i+1, j-1]==player) and (board[i+1, j-2]==player) and (board[i+1, j-3]==player):
                    score += 100
                else:
                    score += 11           
            elif ((diagonal == player).sum() == 2) and ((diagonal == 0).sum() == 2):
                  score += 1             
            elif ((diagonal == -player).sum() == 1):
                  score += 0
            # If opponent has 3 in a row            
            if ((diagonal == -player).sum() == 4):
                score -= 1000
            elif ((diagonal == -player).sum() == 3):
                score -= 10
                
    # Negative diagonal
    for i in range(num_rows-3):
        for j in range(3, -1, -1):
            diagonal = np.array([board[i, j], board[i+1, j+1], board[i+2, j+2], board[i+3, j+3]])
            if (np.all(diagonal==0)):
                continue
            elif (np.all(diagonal==player)):
                  score = 10000
            elif ((diagonal == player).sum() == 3) and ((diagonal == 0).sum() == 1):
                if (board[i+1, j+1]==player) and (board[i+1, j+2]==player) and (board[i+1, j+3]==player):
                    score += 100
                else:
                    score += 11
                    
            elif ((diagonal == player).sum() == 2) and ((diagonal == 0).sum() == 2):
                  score += 1             
            elif ((diagonal == -player).sum() == 1):
                  score += 0
            # If opponent has 3 in a row
            if ((diagonal == -player).sum() == 4):
                score -= 1000
            elif ((diagonal == -player).sum() == 3):
                score -= 10

    return player*score
    
GAME = connect4_board()