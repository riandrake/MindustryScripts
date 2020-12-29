""" Digit display
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
