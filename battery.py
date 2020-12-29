""" Battery script
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
