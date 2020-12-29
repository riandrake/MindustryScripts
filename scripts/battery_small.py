"""
Name: Battery (S) Script

Description: A very small display of your:
             (1) Battery percentage icon + number
             (2) the trending charge/discharge rate of your batteries

Schematic: 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
"""

from void import (
    RES, TX, TY, SX, SY, DIGIT, THICK, PERCENT, SPACEX, SPACEY
)

"""
    BATTERY
"""

M.print('Clear! ')
M.draw.clear(0, 0, 0)

def black():
    M.draw.color(0, 0, 0, 255)


def grey():
    M.draw.color(128, 128, 128, 255)


def red():
    M.draw.color(255, 128, 128, 255)


def green():
    M.draw.color(128, 255, 128, 255)


def yellow():
    M.draw.color(255, 255, 128, 255)


def orange():
    M.draw.color(255, 128, 64, 255)


def up_arrow(x, y, l):
    M.draw.triangle(x, y, x + l/2, y + l, x + l, y)


def down_arrow(x, y, l):
    M.draw.triangle(x, y + l, x + l/2, y, x + l, y + l)


# Battery variables
POWER = battery1.sensor(M.at.powerNetStored)
CAPACITY = battery1.sensor(M.at.powerNetCapacity)
PERCENT = POWER / CAPACITY

NET_IN = battery1.sensor(M.at.powerNetIn)
NET_OUT = battery1.sensor(M.at.powerNetOut)
POWER_NET = NET_IN - NET_OUT

# Screen resolution: 80x80
RES = 80

# Battery dimensions
WIDTH = 30
HEIGHT = 50
CAP_WIDTH = 16
CAP_HEIGHT = 3

PIXELS = HEIGHT * PERCENT

# Calculate important battery co-ordinates
X0 = RES - WIDTH - 5
Y0 = RES - HEIGHT - 5

X1_2 = X0 + WIDTH / 2
CAP_X0 = X1_2 - CAP_WIDTH / 2

# Render battery background
grey()
M.draw.rect(X0, Y0, WIDTH, HEIGHT)
M.draw.rect(CAP_X0, Y0 + HEIGHT, CAP_WIDTH, CAP_HEIGHT)

# Render battery fill
if PERCENT > 0.75:
    green()
elif PERCENT > 0.50:
    yellow()
elif PERCENT > 0.25:
    orange()
else:
    red()

M.draw.rect(X0, Y0, WIDTH, PIXELS)

# Render battery foreground
black()
M.draw.rect(X0, Y0 + HEIGHT * 0.25, WIDTH, 1)
M.draw.rect(X0, Y0 + HEIGHT * 0.50, WIDTH, 1)
M.draw.rect(X0, Y0 + HEIGHT * 0.75, WIDTH, 1)
M.draw.rect(X0, Y0 + HEIGHT * 1.00, WIDTH, 1)

# Render power indicator
ARROW_SIZE = 10
ARROW_OFF = HEIGHT / 4
ARROW_X = X0 - ARROW_OFF

if POWER_NET > 0:
    ARROW_Y = Y0

    green()
    up_arrow(ARROW_X, ARROW_Y, ARROW_SIZE)

    if POWER_NET > 500:
        ARROW_Y += ARROW_OFF
        up_arrow(ARROW_X, ARROW_Y, ARROW_SIZE)
    if POWER_NET > 1000:
        ARROW_Y += ARROW_OFF
        up_arrow(ARROW_X, ARROW_Y, ARROW_SIZE)
    if POWER_NET > 2000:
        ARROW_Y += ARROW_OFF
        up_arrow(ARROW_X, ARROW_Y, ARROW_SIZE)

elif POWER_NET < 0:
    ARROW_Y = Y0 + HEIGHT - ARROW_OFF

    red()
    down_arrow(ARROW_X, ARROW_Y, ARROW_SIZE)

    if POWER_NET < -500:
        ARROW_Y -= ARROW_OFF
        down_arrow(ARROW_X, ARROW_Y, ARROW_SIZE)
    if POWER_NET < -1000:
        ARROW_Y -= ARROW_OFF
        down_arrow(ARROW_X, ARROW_Y, ARROW_SIZE)
    if POWER_NET < -2000:
        ARROW_Y -= ARROW_OFF
        down_arrow(ARROW_X, ARROW_Y, ARROW_SIZE)

else:
    yellow()


"""
    DIGITS
"""

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


VALUE = M.floor(PERCENT * 100)
NUM = 4
NUM_DIGITS = 3 if VALUE >= 100 else 2 if VALUE >= 10 else 1

RES = 80
SX = 64 / NUM
SY = SX
THICK = 2
SPACEX = (RES - SX * NUM) / (NUM + 1)
SPACEY = 4
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

"""
    PERCENT SYMBOL
"""

RES = 80
SIZ = 15
OUT = 6
CUT = 4
CUT_SPA = (OUT - CUT) / 2

# Set color to white
M.draw.color(255, 255, 255, 255)

X0 = RES - SIZ - 4
Y0 = 4

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

"""
    FINISH
"""

M.print(' Flush!')
display1.drawFlush()
message1.printFlush()
