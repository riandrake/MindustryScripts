"""
Name: Battery (L) script

Description: A very large display of your:
             (1) Battery percentage icon + number
             (2) the trending charge/discharge rate of your batteries

Schematic: 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
"""


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

cell1[0] = M.floor(PERCENT * 100)
cell1[1] = "%"

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
X0 = (RES - WIDTH) / 2
Y0 = (RES - HEIGHT) / 2

X1_2 = X0 + WIDTH / 2
CAP_X0 = X1_2 - CAP_WIDTH / 2

# Clear screen
M.draw.clear(0, 0, 0)

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
ARROW_X = X0 + WIDTH + 4

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

display1.drawFlush()
