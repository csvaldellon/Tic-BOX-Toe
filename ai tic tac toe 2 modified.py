from random import choice
from math import inf

XPLAYER = +1
OPLAYER = -1
EMPTY = 0

N = 4
board = []
for x in range(N):
    board += [[]]
# print(board)
for x in board:
    for y in range(N):
        x += [EMPTY]
# print(board)

def printBoard(brd):
    chars = {XPLAYER: 'X', OPLAYER: 'O', EMPTY: ' '}
    for x in brd:
        for y in x:
            ch = chars[y]
            print(f'| {ch} |', end='')
        print('\n' + '--------------------')
    print('====================')


def clearBoard(brd):
    for x, row in enumerate(brd):
        for y, col in enumerate(row):
            brd[x][y] = EMPTY


def winningPlayer(brd, player):
    i = 1
    theBoard = {}
    for a in range(N):
        for b in range(N):
            theBoard[str(i)] = brd[a][b]
            i += 1

    j = 1
    mul = 1
    while mul <= N:
        while j <= mul * N:
            if j + 2 <= mul * N and theBoard[str(j)] == theBoard[str(j + 1)] == theBoard[str(j + 2)] != 0:
                if theBoard[str(j)] == player:
                    return True
            j += 1
        mul += 1

    k = 1
    mul = 1
    while mul <= N:
        while k + 2 * N <= mul + (N - 1) * N:
            if theBoard[str(k)] == theBoard[str(k + N)] == theBoard[str(k + 2 * N)] != 0:
                if theBoard[str(k)] == player:
                    return True
            k += N
        mul += 1
        k = mul

    p = 1
    mul = 1
    while mul <= N - 2:
        while p <= mul * N:
            if p + 2 * (N + 1) <= (mul + 2) * N:
                if theBoard[str(p)] == theBoard[str(p + N + 1)] == theBoard[str(p + 2 * (N + 1))] != 0:
                    if theBoard[str(p)] == player:
                        return True
            elif p + 2 * (N - 1) >= (mul + 1) * N + 1:
                if theBoard[str(p)] == theBoard[str(p + N - 1)] == theBoard[str(p + 2 * (N - 1))] != 0:
                    if theBoard[str(p)] == player:
                        return True
            p += 1
        mul += 1

    return False


def gameWon(brd):
    return winningPlayer(brd, XPLAYER) or winningPlayer(brd, OPLAYER)


def printResult(brd):
    if winningPlayer(brd, XPLAYER):
        print('X has won! ' + '\n')

    elif winningPlayer(brd, OPLAYER):
        print('O\'s have won! ' + '\n')

    else:
        print('Draw' + '\n')


def emptyCells(brd):
    emptyC = []
    for x, row in enumerate(brd):
        for y, col in enumerate(row):
            if brd[x][y] == EMPTY:
                emptyC.append([x, y])

    return emptyC


def boardFull(brd):
    if len(emptyCells(brd)) == 0:
        return True
    return False


def setMove(brd, x, y, player):
    brd[x][y] = player


def playerMove(brd):
    e = True
    moves = {}
    i = 1
    for a in range(N):
        for b in range(N):
            moves[i] = [a, b]
            i += 1

    while e:
        try:
            move = int(input('Pick a position(1-N^2)'))
            if move < 1 or move > N**2:
                print('Invalid location! ')
            elif not (moves[move] in emptyCells(brd)):
                print('Location filled')
            else:
                setMove(brd, moves[move][0], moves[move][1], XPLAYER)
                printBoard(brd)
                e = False
        except(KeyError, ValueError):
            print('Please pick a number!')


def getScore(brd):
    if winningPlayer(brd, XPLAYER):
        return 10

    elif winningPlayer(brd, OPLAYER):
        return -10

    else:
        return 0


def MiniMaxAB(brd, depth, alpha, beta, player):
    row = -1
    col = -1
    if depth == 0 or gameWon(brd):
        return [row, col, getScore(brd)]

    else:
        for cell in emptyCells(brd):
            setMove(brd, cell[0], cell[1], player)
            score = MiniMaxAB(brd, depth - 1, alpha, beta, -player)
            if player == XPLAYER:
                # X is always the max player
                if score[2] > alpha:
                    alpha = score[2]
                    row = cell[0]
                    col = cell[1]

            else:
                if score[2] < beta:
                    beta = score[2]
                    row = cell[0]
                    col = cell[1]

            setMove(brd, cell[0], cell[1], EMPTY)

            if alpha >= beta:
                break

        if player == XPLAYER:
            return [row, col, alpha]

        else:
            return [row, col, beta]


def AIMove(brd):
    if len(emptyCells(brd)) == N**2:
        x = choice([n for n in range(1, N-1)])
        y = choice([n for n in range(1, N-1)])
        setMove(brd, x, y, OPLAYER)
        printBoard(brd)

    else:
        result = MiniMaxAB(brd, len(emptyCells(brd)), -inf, inf, OPLAYER)
        setMove(brd, result[0], result[1], OPLAYER)
        printBoard(brd)


def AI2Move(brd):
    if len(emptyCells(brd)) == N**2:
        x = choice([n for n in range(N)])
        y = choice([n for n in range(N)])
        setMove(brd, x, y, XPLAYER)
        printBoard(brd)

    else:
        result = MiniMaxAB(brd, len(emptyCells(brd)), -inf, inf, XPLAYER)
        setMove(brd, result[0], result[1], XPLAYER)
        printBoard(brd)


def AIvsAI():
    currentPlayer = XPLAYER
    count = 0
    for x in range(1000):
        clearBoard(board)

        while not (boardFull(board) or gameWon(board)):
            makeMove(board, currentPlayer, 2)
            currentPlayer *= -1

        printResult(board)
        if gameWon(board):
            count += 1

    print('Number of AI vs AI wins =', count)


def makeMove(brd, player, mode):
    if mode == 1:
        if player == XPLAYER:
            playerMove(brd)

        else:
            AIMove(brd)
    else:
        if player == XPLAYER:
            AIMove(brd)
        else:
            AI2Move(brd)


def playerVSai():
    while True:
        try:
            order = int(input('Would you like to go first or second? (1/2)? '))
            if not (order == 1 or order == 2):
                print('Please pick 1 or 2')
            else:
                break
        except(KeyError, ValueError):
            print('Enter a number')

    clearBoard(board)
    if order == 2:
        currentPlayer = OPLAYER
    else:
        currentPlayer = XPLAYER

    while not (boardFull(board) or gameWon(board)):
        makeMove(board, currentPlayer, 1)
        currentPlayer *= -1

    printResult(board)


def main():
    while True:
        user = input('Play?(Y/N) ')
        if user.lower() == 'y':
            t = input('AI vs AI or Player vs AI(1/2)')
            if int(t) == 1:
                AIvsAI()
            else:
                playerVSai()
        else:
            print('Bye!')
            exit()


if __name__ == '__main__':
    main()