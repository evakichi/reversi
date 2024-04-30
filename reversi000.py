WHITE = 1
BLACK = -1
EMPTY = 0

board = [
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 1,-1, 0, 0, 0],
        [ 0, 0, 0,-1, 1, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0, 0, 0]]


def reverse(color):
    return -1 * color

def printboard():
    print(' ',end='')
    for y in range(8):
        print('|',end='')
        print(y,end='')
    print('|')
    for X in range(8):
        print(X,end='')
        for Y in range(8):
            if board[X][Y] == -1:
                print('|B',end='')
            elif board[X][Y] == 1:
                print('|W',end='')
            else:
                print('| ',end='')
        print('|')

def isavailable(x,y,color):
    if board[x][y] != EMPTY:
        return False

### →方向の検索
    if y < 6 and board[x][y+1] == reverse(color):
        for n in range(2, 8-y):
            if board[x][y+n] == reverse(color):
                continue
            if board[x][y+n] == color:
                return True
            if board[x][y+n] == EMPTY:
                break
### ←方向の検索
    if y > 1 and board[x][y-1] == reverse(color):
        for n in range(2, y+1):
            if board[x][y-n] == reverse(color):
                continue
            if board[x][y-n] == color:
                return True
            if board[x][y-n] == EMPTY:
                break
### ↓方向の検索
    if x < 6 and board[x+1][y] == reverse(color):
        for n in range(2, 8-x):
            if board[x+n][y] == reverse(color):
                continue
            if board[x+n][y] == color:
                return True
            if board[x+n][y] == EMPTY:
                break
### ↑方向の検索
    if x > 1 and board[x-1][y] == reverse(color):
        for n in range(2, x+1):
            if board[x-n][y] == reverse(color):
                continue
            if board[x-n][y] == color:
                return True
            if board[x-n][y] == EMPTY:
                break
### ↘方向の検索
    min_value = min(8-x, 8-y)
    if min_value > 2  and board[x+1][y+1] == reverse(color):
        for n in range(2, min_value):
            if board[x+n][y+n] == reverse(color):
                continue
            if board[x+n][y+n] == color:
                return True
            if board[x+n][y+n] == EMPTY:
                break
### ↙方向の検索
    min_value = min(8-x, y+1)
    if min_value > 2  and board[x+1][y-1] == reverse(color):
        for n in range(2, min_value):
            if board[x+n][y-n] == reverse(color):
                continue
            if board[x+n][y-n] == color:
                return True
            if board[x+n][y-n] == EMPTY:
                break
### ↖方向の検索
    min_value = min(x+1, y+1)
    if min_value > 2  and board[x-1][y-1] == reverse(color):
        for n in range(2, min_value):
            if board[x-n][y-n] == reverse(color):
                continue
            if board[x-n][y-n] == color:
                return True
            if board[x-n][y-n] == EMPTY:
                break
### ↗方向の検索
    min_value = min(x+1, 8-y)
    if min_value > 2  and board[x-1][y+1] == reverse(color):
        for n in range(2, min_value):
            if board[x-n][y+n] == reverse(color):
                continue
            if board[x-n][y+n] == color:
                return True
            if board[x-n][y+n] == EMPTY:
                break
    return False



def candidate(color):
    c = list()
    for x in range(8):
        for y in range(8):
            if isavailable(x,y,color):
                c.append((x,y))
                print(x,y,'置ける')
    if len(c) == 0:
        return None
    return c

printboard()
c = candidate(BLACK)
