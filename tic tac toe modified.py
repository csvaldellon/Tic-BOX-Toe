N = 3
players = ['X', 'O']
M = len(players)
i = 1
theBoard = {}
while i <= N**2:
    theBoard[str(i)] = " "
    i += 1


def printBoard(board):
    global N
    mul = 1
    j = 1
    while mul <= N:
        printer = '|'
        printer2 = '+'
        while j <= mul*N:
            printer += board[str(j)] + '|'
            printer2 += '-+'
            j += 1
        print(printer)
        if mul < N:
            print(printer2)
        mul += 1


# printBoard(theBoard)
def game():
    turn = players[0]
    count = 0
    i = 0
    while i < N**2:
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
# Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            j = 1
            mul = 1
            while mul <= N:
                while j <= mul*N:
                    if j+2 <= mul*N and theBoard[str(j)] == theBoard[str(j+1)] == theBoard[str(j+2)] != ' ':
                        printBoard(theBoard)
                        print("\nGame Over.\n")
                        print(" **** " + turn + " won. ****")
                        i = N**2
                        count = i + 1
                    j += 1
                mul += 1

            k = 1
            mul = 1
            while mul <= N:
                while k+2*N <= mul + (N-1) * N:
                    if theBoard[str(k)] == theBoard[str(k + N)] == theBoard[str(k + 2*N)] != ' ':
                        printBoard(theBoard)
                        print("\nGame Over.\n")
                        print(" **** " + turn + " won. ****")
                        i = N**2
                        count = i + 1
                    k += N
                mul += 1
                k = mul

            p = 1
            mul = 1
            while mul <= N-2:
                while p <= mul*N:
                    if p + 2*(N+1) <= (mul+2)*N and theBoard[str(p)] == theBoard[str(p + N+1)] == theBoard[str(p + 2 * (N+1))] != ' ':
                        printBoard(theBoard)
                        print("\nGame Over.\n")
                        print(" **** " + turn + " won. ****")
                        i = N ** 2
                        count = i + 1
                    elif p + 2*(N-1) >= (mul+1)*N + 1 and theBoard[str(p)] == theBoard[str(p + N-1)] == theBoard[str(p + 2 * (N-1))] != ' ':
                        printBoard(theBoard)
                        print("\nGame Over.\n")
                        print(" **** " + turn + " won. ****")
                        i = N**2
                        count = i + 1
                    p += 1
                mul += 1

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == N**2:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        global M
        # we have to change the player after every move.
        m = 0
        while m <= M - 1:
            if turn == players[m] and m != M - 1:
                turn = players[m+1]
                m = M
            elif m == M - 1:
                turn = players[0]
                m = M
            m += 1
        i += 1


board_keys = []

for key in theBoard:
    board_keys.append(key)

restart = input("Do want to play Again?(y/n)")

if restart == "y" or restart == "Y":
    for key in board_keys:
        theBoard[key] = " "

    game()
