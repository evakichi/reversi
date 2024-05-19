import sys
import random
import numpy as np
import datetime as dt

class Board:
    WHITE=1
    BLACK=-1
    EMPTY=0
    borad=None

    def __init__(self):
        self.board = [
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 1,-1, 0, 0, 0],
            [ 0, 0, 0,-1, 1, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0]]

    def copy(self):
        board = Board()
        for i in range(8):
            for j in range(8):
                board.board[i][j]=self.get(i,j)
        return board

    def get(self,i,j):
        return self.board[i][j]
    
    def reverse(color):
        return -1 * color

    def printboard(self):
        print(' ',end='')
        for y in range(8):
            print('|',end='')
            print(y,end='')
        print('|')
        for X in range(8):
            print(X,end='')
            for Y in range(8):
                if self.board[X][Y] == -1:
                    print('|B',end='')
                elif self.board[X][Y] == 1:
                    print('|W',end='')
                else:
                    print('| ',end='')
            print('|')

    def result(self):
        w = 0
        b = 0
        for x in range(8):
            w= w+ self.board[x].count(self.WHITE)
            b= b+ self.board[x].count(self.BLACK)
        # print('Black:',b,'White:',w)
        # if w == b:
        #     print('Draw')
        # elif w > b:
        #     print('White won.')
        # else:
        #     print('Black won.')

        return w,b

    def isavailable(self,x,y,color):
        if x < 0 or x > 7 or y < 0 or y > 7 or self.board[x][y] != self.EMPTY:
            return False

        enemy = Board.reverse(color)
    ### →方向の検索
        if y < 6 and self.board[x][y+1] == enemy:
            for n in range(2, 8-y):
                if self.board[x][y+n] == enemy:
                    continue
                if self.board[x][y+n] == color:
                    return True
                if self.board[x][y+n] == self.EMPTY:
                    break
    ### ←方向の検索
        if y > 1 and self.board[x][y-1] == enemy:
            for n in range(2, y+1):
                if self.board[x][y-n] == enemy:
                    continue
                if self.board[x][y-n] == color:
                    return True
                if self.board[x][y-n] == self.EMPTY:
                    break
    ### ↓方向の検索
        if x < 6 and self.board[x+1][y] == enemy:
            for n in range(2, 8-x):
                if self.board[x+n][y] == enemy:
                    continue
                if self.board[x+n][y] == color:
                    return True
                if self.board[x+n][y] == self.EMPTY:
                    break
    ### ↑方向の検索
        if x > 1 and self.board[x-1][y] == enemy:
            for n in range(2, x+1):
                if self.board[x-n][y] == enemy:
                    continue
                if self.board[x-n][y] == color:
                    return True
                if self.board[x-n][y] == self.EMPTY:
                    break
    ### ↘方向の検索
        min_value = min(8-x, 8-y)
        if min_value > 2  and self.board[x+1][y+1] == enemy:
            for n in range(2, min_value):
                if self.board[x+n][y+n] == enemy:
                    continue
                if self.board[x+n][y+n] == color:
                    return True
                if self.board[x+n][y+n] == self.EMPTY:
                    break
    ### ↙方向の検索
        min_value = min(8-x, y+1)
        if min_value > 2  and self.board[x+1][y-1] == enemy:
            for n in range(2, min_value):
                if self.board[x+n][y-n] == enemy:
                    continue
                if self.board[x+n][y-n] == color:
                    return True
                if self.board[x+n][y-n] == self.EMPTY:
                    break
    ### ↖方向の検索
        min_value = min(x+1, y+1)
        if min_value > 2  and self.board[x-1][y-1] == enemy:
            for n in range(2, min_value):
                if self.board[x-n][y-n] == enemy:
                    continue
                if self.board[x-n][y-n] == color:
                    return True
                if self.board[x-n][y-n] == self.EMPTY:
                    break
    ### ↗方向の検索
        min_value = min(x+1, 8-y)
        if min_value > 2  and self.board[x-1][y+1] == enemy:
            for n in range(2, min_value):
                if self.board[x-n][y+n] == enemy:
                    continue
                if self.board[x-n][y+n] == color:
                    return True
                if self.board[x-n][y+n] == self.EMPTY:
                    break
        return False


    def candidate(self,color):
        c = list()
        for x in range(8):
            for y in range(8):
                if self.isavailable(x,y,color):
                    c.append((x,y))
                    # print(x,y,'置ける')
        if len(c) == 0:
            return None
        return c

    def put(self,x,y,color):

        self.board[x][y] = color

        enemy = Board.reverse(color)

    ### →方向に置く
        if y < 6 and self.board[x][y+1] == enemy:
            for n in range(2, 8-y):
                if self.board[x][y+n] == enemy:
                    continue
                if self.board[x][y+n] == color:
                    for nn in range(1,n):
                        self.board[x][y+nn]=color
                    break
                if self.board[x][y+n] == self.EMPTY:
                    break
    ### ←方向に置く
        if y > 1 and self.board[x][y-1] == enemy:
            for n in range(2, y+1):
                if self.board[x][y-n] == enemy:
                    continue
                if self.board[x][y-n] == color:
                    for nn in range(1,n):
                        self.board[x][y-nn]=color
                    break
                if self.board[x][y-n] == self.EMPTY:
                    break
    ### ↓方向に置く
        if x < 6 and self.board[x+1][y] == enemy:
            for n in range(2, 8-x):
                if self.board[x+n][y] == enemy:
                    continue
                if self.board[x+n][y] == color:
                    for nn in range(1,n):
                        self.board[x+nn][y]=color
                    break
                if self.board[x+n][y] == self.EMPTY:
                    break
    ### ↑方向に置く
        if x > 1 and self.board[x-1][y] == enemy:
            for n in range(2, x+1):
                if self.board[x-n][y] == enemy:
                    continue
                if self.board[x-n][y] == color:
                    for nn in range(1,n):
                        self.board[x-nn][y]=color
                    break
                if self.board[x-n][y] == self.EMPTY:
                    break
    ### ↘方向に置く
        min_value = min(8-x, 8-y)
        if min_value > 2  and self.board[x+1][y+1] == enemy:
            for n in range(2, min_value):
                if self.board[x+n][y+n] == enemy:
                    continue
                if self.board[x+n][y+n] == color:
                    for nn in range(1,n):
                        self.board[x+nn][y+nn]=color
                    break
                if self.board[x+n][y+n] == self.EMPTY:
                    break
    ### ↙方向に置く
        min_value = min(8-x, y+1)
        if min_value > 2  and self.board[x+1][y-1] == enemy:
            for n in range(2, min_value):
                if self.board[x+n][y-n] == enemy:
                    continue
                if self.board[x+n][y-n] == color:
                    for nn in range(1,n):
                        self.board[x+nn][y-nn]=color
                    break
                if self.board[x+n][y-n] == self.EMPTY:
                    break
    ### ↖方向に置く
        min_value = min(x+1, y+1)
        if min_value > 2  and self.board[x-1][y-1] == enemy:
            for n in range(2, min_value):
                if self.board[x-n][y-n] == enemy:
                    continue
                if self.board[x-n][y-n] == color:
                    for nn in range(1,n):
                        self.board[x-nn][y-nn]=color
                    break
                if self.board[x-n][y-n] == self.EMPTY:
                    break
    ### ↗方向に置く
        min_value = min(x+1, 8-y)
        if min_value > 2  and self.board[x-1][y+1] == enemy:
            for n in range(2, min_value):
                if self.board[x-n][y+n] == enemy:
                    continue
                if self.board[x-n][y+n] == color:
                    for nn in range(1,n):
                        self.board[x-nn][y+nn]=color
                    break
                if self.board[x-n][y+n] == self.EMPTY:
                    break

class Battle:

    board = None
    whitelog = None
    blacklog = None
    whitecount = None
    blackcount = None
    drawcount  = None

    def __init__(self) -> None:
        self.whitelog = Tracelog('white')
        self.whitecount = 0
        self.blacklog = Tracelog('black')
        self.blackcount = 0
        self.drawcount = 0

    def continuous_battle(self,n):
        for count in range(n):
            self.battle()
        self.whitelog.normalize(n)
        self.whitelog.print_total()
        self.whitelog.save()
        self.blacklog.normalize(n)
        self.blacklog.print_total()
        self.blacklog.save()
        print ('black : ',self.blackcount,' white : ',self.whitecount,' draw : ',self.drawcount)

    def battle(self):
        self.board = Board()

        w = MiniMaxPlayer(self.board.WHITE)
        b = RandomChoicePlayer(self.board.BLACK)

        w.load("20240519-172302-black.npy","20240519-172302-white.npy")

        self.whitelog.reset_log()
        self.blacklog.reset_log()

        current_color = self.board.BLACK
        C = self.board.candidate(current_color)
        while True:
            # self.board.printboard()
            # if current_color == self.board.WHITE:
            #     print("White's turn")
            # else:
            #     print("Black's turn")

            flag = True
            if C is not None:
                flag = False
                if current_color == self.board.WHITE:
                    next = w.next(self.board.copy())
                else:
                    next = b.next(self.board.copy())
                if next is not None:
                    x,y = next
                    self.board.put(x,y,current_color)
                    if current_color == self.board.WHITE:
                        self.whitelog.logging(x,y)
                    else:
                        self.blacklog.logging(x,y)
            else:
                pass
                #print('Pass')
            current_color = Board.reverse(current_color)
            C = self.board.candidate(current_color)
            if flag and C is None:
                whitecount, blackcount= self.board.result()
                if whitecount < blackcount:
                    self.blackcount += 1
                    self.whitelog.result(-(blackcount/64))
                    self.blacklog.result((blackcount/64))
                elif whitecount > blackcount:
                    self.whitecount += 1
                    self.whitelog.result((whitecount/64))
                    self.blacklog.result(-(whitecount/64))
                else:
                    self.drawcount += 1
                    self.whitelog.result((blackcount/64))
                    self.blacklog.result((blackcount/64))
                break

class Player:
    own_color = None

    def __init__(self,own_color):
        self.own_color = own_color

    def next(self,currentboard):
        pass

class FirstChoicePlayer(Player):

    def __init__(self,own_color) -> None:
        super().__init__(own_color)

    def next(self,currentboard):
        c = currentboard.candidate(self.own_color)
        l = len(c)
        if l > 0:
            return c[0]
        else:
            return None

class RandomChoicePlayer(Player):

    def __init__(self,own_color) -> None:
        super().__init__(own_color)

    def next(self,currentboard):
        c = currentboard.candidate(self.own_color)
        l = len(c)
        if l > 0:
            n = random.randrange(l)
            return c[n]
        else:
            return None

class InputPlayer(Player):

    def __init__(self,own_color):
        super().__init__(own_color)

    def next(self,currentboard):
        if self.own_color == currentboard.WHITE:
            print ('input:W')
        else:
            print ('input:B')
        c = currentboard.candidate(self.own_color)
        l = len(c)
        if l != 0:
            x,y = -1,-1
            currentboard.printboard()
            flag = False
            while not currentboard.isavailable(x,y,self.own_color):
                if flag :
                    print('err')
                x_input = input('x:')
                try:
                    x = int(x_input)
                except Exception as e:
                    print (e)
                    x = -1
                y_input = input('y:')
                try:
                    y = int(y_input)
                except Exception as e:
                    print (e)
                    y = -1
                flag = True
            return x,y
        else:
            print("Pass")
            return None

class MiniMaxPlayer(Player):
    
    def __init__(self, own_color):
        super().__init__(own_color)

    def next(self,currentboard):
        return self.minimax(currentboard,self.own_color,self.own_color,1,0)

    def load(self,black_filename,white_filename):
        self.black_point_data = np.load(black_filename)
        self.white_point_data = np.load(white_filename)

    def minimax(self,currentboard,current_color,color,max_depth,depth):
        candidate = currentboard.candidate(color)
        
        if candidate is None and currentboard.candidate(-color) is None:
            white_count,black_count = currentboard.result()
            if color == Board.WHITE:
                if white_count > black_count:
                    return 1.0
                else:
                    return -1.0
            else:
                if white_count < black_count:
                    return 1.0
                else:
                    return -1.0

        if candidate is None and currentboard.candidate(-color) is not None:
            return self.minimax(currentboard,current_color,-color,max_depth,depth+1)

        
        if depth == 0:
            if candidate is None:
                return None
            max_point = -sys.float_info.max
            x,y = -1,-1
            for c in candidate:
                nextboard = currentboard.copy()
                tmp_x,tmp_y = c
                nextboard.put(tmp_x,tmp_y,color)
                point = self.minimax(nextboard,current_color,-color,max_depth,depth+1)
                if point > max_point:
                    max_point = point
                    x,y = c
            print(depth,'max',max_point,'x,y',x,y)
            return x,y

    
        if depth >= max_depth:
            if color == current_color:
                max_point = -sys.float_info.max
                for c in candidate:
                    tmp_x,tmp_y = c
                    if color == Board.BLACK:
                        point = self.black_point_data[tmp_x][tmp_y]
                    else:
                        point = self.white_point_data[tmp_x][tmp_y]
                    print(depth,'point',point,'max_point',max_point)
                    if max_point < point:
                        max_point = point
                print(depth,'max',max_point)
                return max_point
            else:
                min_point = sys.float_info.max
                for c in candidate:
                    tmp_x,tmp_y = c
                    if color == Board.BLACK:
                        point = self.black_point_data[tmp_x][tmp_y]
                    else:
                        point = self.white_point_data[tmp_x][tmp_y]
                    print(depth,'point',point,'min_point',min_point)
                    if min_point > point:
                        min_point = point
                print(depth,'min',min_point)
                return min_point

        if color == current_color:
            max_point = -sys.float_info.max
            for c in candidate:
                nextboard = currentboard.copy()
                tmp_x,tmp_y=c
                nextboard.put(tmp_x,tmp_y,color)
                point = self.minimax(nextboard,current_color,-color,max_depth,depth+1)
                if point > max_point:
                    max_point = point
            print(depth,'max',max_point)
            return max_point
        else:
            min_point = sys.float_info.max
            for c in candidate:
                nextboard = currentboard.copy()
                tmp_x,tmp_y=c
                nextboard.put(tmp_x,tmp_y,color)
                point = self.minimax(nextboard,current_color,-color,max_depth,depth+1)
                if point < min_point:
                    min_point = point
            print(depth,'min',min_point)
            return min_point



class Tracelog:

    log = None
    total = None
    color = None

    def __init__(self,color):
        self.color = color
        self.total = np.zeros((8,8))

    def reset_log(self):
        self.log = np.zeros((8,8))

    def logging(self,x,y):
        self.log[x][y]=1

    def result(self,point):
        self.total += self.log*point

    def normalize(self,total):
        self.total /= total

    def print_total(self):
        print(self.color,self.total)

    def save(self):
        np.save(dt.datetime.now().strftime('%Y%m%d-%H%M%S')+'-'+self.color,self.total)

battle = Battle()
battle.continuous_battle(100)
