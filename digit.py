""" Digit display
"""

from void import (
    RES, TX, TY, SX, SY, DIGIT, THICK, PERCENT, SPACEX, SPACEY
)


def L1():
    M.draw.rect(TX, TY + SY / 2, THICK, SY / 2)


def L2():
    M.draw.rect(TX, TY, THICK, SY / 2)


def R1():
    M.draw.rect(TX + SX - THICK, TY + SY / 2, THICK, SY / 2)


def R2():
    M.draw.rect(TX + SX - THICK, TY, THICK, SY / 2)


def T1():
    M.draw.rect(TX, TY + SY - THICK, SX, THICK)


def T2():
    M.draw.rect(TX, TY + SY/2 - THICK, SX, THICK)


def T3():
    M.draw.rect(TX, TY, SX, THICK)


def draw_percent():
    RES = 80
    SIZ = 20
    SPA = (RES - SIZ) / 2
    OUT = SIZ * 0.4
    CUT = OUT * 0.5
    CUT_SPA = (OUT - CUT) / 2

    # Set color to white
    M.draw.color(255, 255, 255, 255)

    X0 = RES - SIZ - 4
    Y0 = X0 / 2

    # Draw divisor
    AX = X0
    AY = Y0 + CUT_SPA / 2
    BX = X0 + CUT_SPA / 2
    BY = Y0
    CX = X0 + SIZ - CUT_SPA / 2
    CY = Y0 + SIZ
    DX = X0 + SIZ
    DY = Y0 + SIZ - CUT_SPA / 2

    M.draw.triangle(AX, AY, CX, CY, DX, DY)
    M.draw.triangle(AX, AY, DX, DY, BX, BY)

    # Draw circle rectangles in white
    A = 0
    B = SIZ - OUT
    M.draw.rect(X0 + A, Y0 + B, OUT, OUT)
    M.draw.rect(X0 + B, Y0 + A, OUT, OUT)

    # Set draw color to black for cutouts
    M.draw.color(0, 0, 0, 255)

    # Render cutouts for circles
    M.draw.rect(X0 + A + CUT_SPA, Y0 + B + CUT_SPA, CUT, CUT)
    M.draw.rect(X0 + B + CUT_SPA, Y0 + A + CUT_SPA, CUT, CUT)


def draw_digit():
    M.draw.color(255, 255, 255, 255)
    M.print(DIGIT)
    if DIGIT < 1:
        T1() | T3() | L1() | L2() | R1() | R2()
    elif DIGIT < 2:
        R1() | R2()
    elif DIGIT < 3:
        T1() | T2() | T3() | R1() | L2()
    elif DIGIT < 4:
        T1() | T2() | T3() | R1() | R2()
    elif DIGIT < 5:
        L1() | R1() | T2() | R2()
    elif DIGIT < 6:
        T1() | L1() | T2() | R2() | T3()
    elif DIGIT < 7:
        T1() | L1() | T2() | R2() | T3() | L2()
    elif DIGIT < 8:
        T1() | R1() | R2()
    elif DIGIT < 9:
        T1() | T2() | T3() | L1() | L2() | R1() | R2()
    else:
        T1() | T2() | T3() | L1() | R1() | R2()


M.print('Clear! ')
M.draw.clear(0, 0, 0)

PERCENT = cell1[1] == "%"

VALUE = cell1[0]
NUM = 3 if VALUE >= 100 else 2
NUM_DIGITS = NUM

if PERCENT:
    NUM += 1

RES = 80
SX = 64 / NUM
SY = SX
THICK = 2 if NUM == 3 else 8 if NUM == 1 else 4
SPACEX = (RES - SX * NUM) / (NUM + 1)
SPACEY = (RES - SY) / 2
TX = SPACEX
TY = SPACEY


if NUM_DIGITS > 2:
    DIGIT = M.floor(VALUE // 100)
    VALUE = VALUE % 100
    draw_digit()
    TX += SPACEX + SX

if NUM_DIGITS > 1:
    DIGIT = M.floor(VALUE // 10)
    draw_digit()
    TX += SPACEX + SX

DIGIT = M.floor(VALUE % 10)
draw_digit()

if PERCENT:
    draw_percent()

M.print(' Flush!')
display1.drawFlush()
message1.printFlush()
