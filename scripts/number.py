"""
Name: Number script

Description: A small 80x80 panel that can print positive integers from 0 to 999.

Schematic: bXNjaAF4nAGbBGT7AAQAAwIABG5hbWUABWRpZ2l0AAtkZXNjcmlwdGlvbgAAAwALbWVtb3J5LWNlbGwAD21pY3JvLXByb2Nlc3NvcgANbG9naWMtZGlzcGxheQAAAAMAAAAAAQAAAQAAAAIOAAAEL3icvVjbTtwwEE0rVar2A/rsT4jv9lsRRS3qRVUXqt2nKkAoVIGFXbaUX+3PUNtjx9nES0kiEBJaeybHZ+aMry+y7M3fX+uLKyRQUd0Wdyv0B50W1aqcLK7Qyflv9GOJ0XSOiG0XJyemTdDB3HZHDwoeJ8viFi3L4xt0MAO/D/u7H509R/lkVd6gt8eL9eVNuTSdbOLGxfnWgXkC1gwdUHkKVXhUlUAF+tLCTGe2Y7U+Mh0KOi1qHFu3gjY0XdS6kRfc5gdY1tVTNC4JjpgAScK2ksS0zRIz373JE3eS5FwbacLJPGGfKKK3c5AWZjpvcFC+23FoyW2M05kfNTWghgEp36o3yduVhiHpJI8cCPGGFAdjfIgDoZ5DpzraNfYgiq9ckqf0q8rV6uCsuLSOHL3bf79/gDB8wDUqr9dFBaZ2tnUcw/uTVKp8ZljHm6Zm8MIRFuhyXVXuX4ToIuCtADKiRADRAZBbARSgbAJg0qWwnYMGnBZElwROVbSDoDngOAgvIX1YQoq9hH7KCllLaExtCR8ZzxDqpCHhI6lTT90XvWKROh1ZfbRbfallHKizVPX1KmCzZtQ4A8vHgDucwSVMJaD0UUB5BeqtDkcJ1HNKoEdLwPKIM1AChgFnxAxmBHB6iMDCNOCBH69FYJ158LhFcUjw6VnQR0XGI87Q/AnA6ZM/6fMXTlZmKarzJ8cVcY8tiKnx+dMRZ2D+eA44IyYSx4DTQwJOvATS8+NRAvPzuSTgdLQEnEWcoRJwwBkjgQCcwXsBl4DSR8OwFygfoKBRw5F7Qa+FiCf3gl4SiDziPDJ8Ec5ROtzPRB2+6B6knm4rFGT0VmiUq3EGTSTBAGVw/QkOKCM2YyEAZ0wZSMD5Xxk8vabpvaGXpjriDNJU5oAyQhKJAWeEJJIAjoNoXVslhVvucVUWS3uvDX+TZVm4hxGGjsuqwv7G+33n0+Ge67bwP42TwbHTee/a9nLvgPPcq4nj6VaG660FMk0RLiEEp4q6Ay5r8PBZPLRJuYmtwt2M4I68tQuOTGzbtb4cfnY9rvFtb4pUHt8ipEZmghkXZ53OXBf8nvt3mUBI5Q4qREhE09LkoXBN1RyiummoPyMOMMwSU/gNywYgDdsJoZ2yql1YHN62XSs8Din3inexduDMxmlDjk9j3CXG2mJFmqUb6NXJUhJ8rQ1y9HVnd2/mLA0w5cDgQcl/qKGfxK/mrhtIzjwQtObeoVUxxl+DAiG5PN50dR7Te+5f9nCjck33abVwc0cTMB650WC3sr0uQQsbuKaNL5tTRNPG82Ji5dr+xqZZyBXUlO21L1AzZ0tEyjdKo3GI0LwbqYjTqBmoBFsrUDk4BvVADKqRPp2kY5IJxk0+Xp0ehOzqdlqtV2emuFZXVXGHJ1mWvcxeuVUty+7vs9fBkr28v/8H1a48pwMCAAIAAQADIu0how==
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
