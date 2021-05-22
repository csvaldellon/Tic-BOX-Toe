# MODULES
import pygame, sys
import numpy as np

# initializes pygame
pygame.init()

# ---------
# CONSTANTS
# ---------
N = 5
WIDTH = 100*N
HEIGHT = WIDTH + 200
LINE_WIDTH = 7
WIN_LINE_WIDTH = LINE_WIDTH
BOARD_ROWS = N
BOARD_COLS = BOARD_ROWS
SQUARE_SIZE = 100
CIRCLE_RADIUS = 30
CIRCLE_WIDTH = 8
CROSS_WIDTH = 13
BOX_WIDTH = 13
SPACE = 28
# rgb: red green blue
# RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
BOX_COLOR = (233, 150, 122)

# ------
# SCREEN
# ------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC BOX TOE')
screen.fill(BG_COLOR)

# -------------
# CONSOLE BOARD
# -------------
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
# scores = [0, 0]
X_score = 0
O_score = 0
Y_score = 0
jex = []
kex = []
pex = []
qex = []

# ---------
# FUNCTIONS
# ---------


def draw_lines():
    i = 0
    while i <= N:
        pygame.draw.line(screen, LINE_COLOR, (0, i*SQUARE_SIZE), (WIDTH, i*SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i*SQUARE_SIZE, 0), (i*SQUARE_SIZE, WIDTH), LINE_WIDTH)
        i += 1


def check_win():
    global O_score, X_score, Y_score, jex, kex, pex, qex
    hor_win, ver_win, diag_win_1, diag_win_2 = False, False, False, False
    i = 1
    theBoard = {}
    for a in range(N):
        for b in range(N):
            theBoard[str(i)] = board[a][b]
            i += 1

    j = 1
    mul = 1
    while mul <= N:
        while j <= mul * N:
            if j + 2 <= mul * N and theBoard[str(j)] == theBoard[str(j + 1)] == theBoard[str(j + 2)] != 0. and j not in jex:
                draw_horizontal_winning_line(mul-1, player, j-(mul-1)*N-1)
                jex += [j]
                if player == 1:
                    O_score += 1
                elif player == 2:
                    X_score += 1
                elif player == 3:
                    Y_score += 1
                hor_win = True
            j += 1
        mul += 1

    k = 1
    mul = 1
    while mul <= N:
        while k + 2 * N <= mul + (N - 1) * N:
            if theBoard[str(k)] == theBoard[str(k + N)] == theBoard[str(k + 2 * N)] != 0. and k not in kex:
                draw_vertical_winning_line(mul-1, player, (k-1)//N)
                kex += [k]
                if player == 1:
                    O_score += 1
                elif player == 2:
                    X_score += 1
                elif player == 3:
                    Y_score += 1
                ver_win = True
            k += N
        mul += 1
        k = mul

    q = 1
    p = 1
    mul = 1
    while mul <= N - 2:
        while q <= mul * N:
            if q + 2 * (N - 1) >= (mul + 1) * N + 1:
                if theBoard[str(q)] == theBoard[str(q + N - 1)] == theBoard[str(q + 2 * (N - 1))] != 0. and q not in qex:
                    draw_asc_diagonal(mul-1, player, q-(mul-1)*N-1)
                    qex += [q]
                    if player == 1:
                        O_score += 1
                    elif player == 2:
                        X_score += 1
                    elif player == 3:
                        Y_score += 1
                    diag_win_1 = True
            q += 1
        while p <= mul * N:
            if p + 2 * (N + 1) <= (mul + 2) * N:
                if theBoard[str(p)] == theBoard[str(p + N + 1)] == theBoard[str(p + 2 * (N + 1))] != 0. and p not in pex:
                    draw_des_diagonal(mul-1, player, p-(mul-1)*N-1)
                    pex += [p]
                    if player == 1:
                        O_score += 1
                    elif player == 2:
                        X_score += 1
                    elif player == 3:
                        Y_score += 1
                    diag_win_2 = True
            p += 1
        mul += 1

    return hor_win or ver_win or diag_win_1 or diag_win_2


def draw_figures():
    ADD = 6
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col] == 2:
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )
                pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )
            elif board[row][col] == 3:
                pygame.draw.line( screen, BOX_COLOR, (col * SQUARE_SIZE + SPACE-ADD, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE+ADD, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), BOX_WIDTH )
                pygame.draw.line( screen, BOX_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), BOX_WIDTH )
                pygame.draw.line(screen, BOX_COLOR, (col * SQUARE_SIZE + SPACE-ADD, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE+ADD, row * SQUARE_SIZE + SPACE), BOX_WIDTH)
                pygame.draw.line(screen, BOX_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), BOX_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True


def draw_vertical_winning_line(col, player, k):
    posX = col * SQUARE_SIZE + SQUARE_SIZE//2
    start = (k) * SQUARE_SIZE + SQUARE_SIZE // 2
    end = (k+2) * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    elif player == 3:
        color = BOX_COLOR

    pygame.draw.line(screen, color, (posX, start), (posX, end), LINE_WIDTH)


def draw_horizontal_winning_line(row, player, j):
    posY = row * SQUARE_SIZE + SQUARE_SIZE//2
    start = (j) * SQUARE_SIZE + SQUARE_SIZE // 2
    end = (j+2) * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    elif player == 3:
        color = BOX_COLOR

    pygame.draw.line(screen, color, (start, posY), (end, posY), LINE_WIDTH)


def draw_des_diagonal(row, player, col):
    x_start = col * SQUARE_SIZE + SQUARE_SIZE//2
    x_end = (col+2) * SQUARE_SIZE + SQUARE_SIZE // 2
    y_start = row * SQUARE_SIZE + SQUARE_SIZE // 2
    y_end = (row+2) * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    elif player == 3:
        color = BOX_COLOR

    pygame.draw.line( screen, color, (x_start, y_start), (x_end, y_end), WIN_LINE_WIDTH )


def draw_asc_diagonal(row, player, col):
    x_start = col * SQUARE_SIZE + SQUARE_SIZE//2
    x_end = (col-2) * SQUARE_SIZE + SQUARE_SIZE // 2
    y_start = row * SQUARE_SIZE + SQUARE_SIZE // 2
    y_end = (row+2) * SQUARE_SIZE + SQUARE_SIZE // 2
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    elif player == 3:
        color = BOX_COLOR

    pygame.draw.line( screen, color, (x_start, y_start), (x_end, y_end), WIN_LINE_WIDTH )


draw_lines()

# ---------
# VARIABLES
# ---------
player = 1
game_over = False

# --------
# MAINLOOP
# --------
FONT_SIZE = 35
ALLOWANCE = 15
Turn = 'O'
TURN_COLOR = CIRCLE_COLOR
players = {1: ['O', CIRCLE_COLOR], 2: ['X', CROSS_COLOR], 3: ['Box', BOX_COLOR]}
while True:
    font_turn1 = pygame.font.SysFont('freesansbold', FONT_SIZE)
    text_turn1 = font_turn1.render('Turn to Move: ', True, LINE_COLOR, BG_COLOR)
    screen.blit(text_turn1, (WIDTH//2 + 2*ALLOWANCE + 7, WIDTH + ALLOWANCE))
    font_turn2 = pygame.font.SysFont('freesansbold', 2*FONT_SIZE)
    text_turn2 = font_turn2.render(str(Turn), True, TURN_COLOR, BG_COLOR)
    textRect = text_turn2.get_rect()
    textRect.center = (WIDTH // 2 + 2*ALLOWANCE + WIDTH // 6, WIDTH + ALLOWANCE + 2*FONT_SIZE)
    screen.blit(text_turn2, textRect)

    font = pygame.font.SysFont('freesansbold', FONT_SIZE)
    text_O = font.render('O Score: ' + str(O_score), True, CIRCLE_COLOR, BG_COLOR)
    text_X = font.render('X Score: ' + str(X_score), True, CROSS_COLOR, BG_COLOR)
    text_BOX = font.render('Box Score: ' + str(Y_score), True, BOX_COLOR, BG_COLOR)
    screen.blit(text_O, (ALLOWANCE, WIDTH+ALLOWANCE))
    screen.blit(text_X, (ALLOWANCE, WIDTH+FONT_SIZE+ALLOWANCE))
    screen.blit(text_BOX, (ALLOWANCE, WIDTH + 2*FONT_SIZE + ALLOWANCE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if available_square( clicked_row, clicked_col ):

                mark_square( clicked_row, clicked_col, player )
                if check_win():
                    screen.blit(text_O, (ALLOWANCE, WIDTH + ALLOWANCE))
                    screen.blit(text_X, (ALLOWANCE, WIDTH + FONT_SIZE + ALLOWANCE))
                    screen.blit(text_BOX, (ALLOWANCE, WIDTH + 2 * FONT_SIZE + ALLOWANCE))
                if not is_board_full():
                    player = player % 3 + 1
                    screen.fill(BG_COLOR, (WIDTH // 2 + 2*ALLOWANCE + WIDTH // 6 - 3*FONT_SIZE, WIDTH + ALLOWANCE + FONT_SIZE, WIDTH // 2 + 2*ALLOWANCE + WIDTH // 6 + FONT_SIZE, WIDTH + ALLOWANCE + 3*FONT_SIZE))
                    Turn = players[player][0]
                    TURN_COLOR = players[player][1]
                elif is_board_full():
                    screen.fill(BG_COLOR, (WIDTH // 2 + 2 * ALLOWANCE + WIDTH // 6 - 3 * FONT_SIZE, WIDTH + ALLOWANCE + FONT_SIZE, WIDTH // 2 + 2 * ALLOWANCE + WIDTH // 6 + FONT_SIZE, WIDTH + ALLOWANCE + 3 * FONT_SIZE))
                    Turn = "End"
                    TURN_COLOR = LINE_COLOR
                draw_figures()

        if is_board_full():
            font2 = pygame.font.SysFont('freesansbold', 2*FONT_SIZE)
            if X_score > O_score and X_score > Y_score:
                message = "X wins!"
                MESSAGE_COLOR = CROSS_COLOR
            elif O_score > X_score and O_score > Y_score:
                message = "O wins!"
                MESSAGE_COLOR = CIRCLE_COLOR
            elif Y_score > X_score and Y_score > O_score:
                message = "Box wins!"
                MESSAGE_COLOR = BOX_COLOR
            elif X_score == Y_score > O_score:
                message = "X and Box win!"
                MESSAGE_COLOR = LINE_COLOR
            elif X_score == O_score > Y_score:
                message = "X and O win!"
                MESSAGE_COLOR = LINE_COLOR
            elif Y_score == O_score > X_score:
                message = "Box and O win!"
                MESSAGE_COLOR = LINE_COLOR
            else:
                message = "It's a draw!"
                MESSAGE_COLOR = LINE_COLOR
            text_win = font2.render(message, True, MESSAGE_COLOR, BG_COLOR)
            screen.blit(text_win, (ALLOWANCE, 3*FONT_SIZE+ALLOWANCE+WIDTH))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player = 1
                game_over = False

    pygame.display.update()
