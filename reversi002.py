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
    if x < 0 or x > 7 or y < 0 or y > 7 or board[x][y] != EMPTY:
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

def put(x,y,color):

    board[x][y] = color

### →方向に置く
    if y < 6 and board[x][y+1] == reverse(color):
        for n in range(2, 8-y):
            if board[x][y+n] == reverse(color):
                continue
            if board[x][y+n] == color:
                for nn in range(1,n):
                    board[x][y+nn]=color
                break
            if board[x][y+n] == EMPTY:
                break
### ←方向に置く
    if y > 1 and board[x][y-1] == reverse(color):
        for n in range(2, y+1):
            if board[x][y-n] == reverse(color):
                continue
            if board[x][y-n] == color:
                for nn in range(1,n):
                    board[x][y-nn]=color
                break
            if board[x][y-n] == EMPTY:
                break
### ↓方向に置く
    if x < 6 and board[x+1][y] == reverse(color):
        for n in range(2, 8-x):
            if board[x+n][y] == reverse(color):
                continue
            if board[x+n][y] == color:
                for nn in range(1,n):
                    board[x+nn][y]=color
                break
            if board[x+n][y] == EMPTY:
                break
### ↑方向に置く
    if x > 1 and board[x-1][y] == reverse(color):
        for n in range(2, x+1):
            if board[x-n][y] == reverse(color):
                continue
            if board[x-n][y] == color:
                for nn in range(1,n):
                    board[x-nn][y]=color
                break
            if board[x-n][y] == EMPTY:
                break
### ↘方向に置く
    min_value = min(8-x, 8-y)
    if min_value > 2  and board[x+1][y+1] == reverse(color):
        for n in range(2, min_value):
            if board[x+n][y+n] == reverse(color):
                continue
            if board[x+n][y+n] == color:
                for nn in range(1,n):
                    board[x+nn][y+nn]=color
                break
            if board[x+n][y+n] == EMPTY:
                break
### ↙方向に置く
    min_value = min(8-x, y+1)
    if min_value > 2  and board[x+1][y-1] == reverse(color):
        for n in range(2, min_value):
            if board[x+n][y-n] == reverse(color):
                continue
            if board[x+n][y-n] == color:
                for nn in range(1,n):
                    board[x+nn][y-nn]=color
                break
            if board[x+n][y-n] == EMPTY:
                break
### ↖方向に置く
    min_value = min(x+1, y+1)
    if min_value > 2  and board[x-1][y-1] == reverse(color):
        for n in range(2, min_value):
            if board[x-n][y-n] == reverse(color):
                continue
            if board[x-n][y-n] == color:
                for nn in range(1,n):
                    board[x-nn][y-nn]=color
                break
            if board[x-n][y-n] == EMPTY:
                break
### ↗方向に置く
    min_value = min(x+1, 8-y)
    if min_value > 2  and board[x-1][y+1] == reverse(color):
        for n in range(2, min_value):
            if board[x-n][y+n] == reverse(color):
                continue
            if board[x-n][y+n] == color:
                for nn in range(1,n):
                    board[x-nn][y+nn]=color
                break
            if board[x-n][y+n] == EMPTY:
                break

current_color = BLACK
C = candidate(current_color)
while True:
    printboard()
    if current_color == WHITE:
        print("White's turn")
    else:
        print("Black's turn")

    flag = True
    if C is not None:
        flag = False
        x,y = C[0]
        put(x,y,current_color)
        print('Put:',x,y)
    else:
        print('Pass')
    current_color = reverse(current_color)
    C = candidate(current_color)
    if flag and C is None:
        break

W = 0
B = 0
for x in range(8):
    W = W + board[x].count(WHITE)
    B = B + board[x].count(BLACK)
print('White:',W,'Black:',B)
if W == B:
    print('Draw')
elif W > B:
    print('White won.')
else:
    print('Black won.')

