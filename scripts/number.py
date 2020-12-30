"""
Name: Number script

Description: A small 80x80 panel that can print positive integers from 0 to 999.

Schematic: bXNjaAF4nAGbBGT7AAQAAwIABG5hbWUABWRpZ2l0AAtkZXNjcmlwdGlvbgAAAwALbWVtb3J5LWNlbGwAD21pY3JvLXByb2Nlc3NvcgANbG9naWMtZGlzcGxheQAAAAMAAAAAAQAAAQAAAAIOAAAEL3icvVjbTtwwEE0rVar2A/rsT4jv9lsRRS3qRVUXqt2nKkAoVIGFXbaUX+3PUNtjx9nES0kiEBJaeybHZ+aMry+y7M3fX+uLKyRQUd0Wdyv0B50W1aqcLK7Qyflv9GOJ0XSOiG0XJyemTdDB3HZHDwoeJ8viFi3L4xt0MAO/D/u7H509R/lkVd6gt8eL9eVNuTSdbOLGxfnWgXkC1gwdUHkKVXhUlUAF+tLCTGe2Y7U+Mh0KOi1qHFu3gjY0XdS6kRfc5gdY1tVTNC4JjpgAScK2ksS0zRIz373JE3eS5FwbacLJPGGfKKK3c5AWZjpvcFC+23FoyW2M05kfNTWghgEp36o3yduVhiHpJI8cCPGGFAdjfIgDoZ5DpzraNfYgiq9ckqf0q8rV6uCsuLSOHL3bf79/gDB8wDUqr9dFBaZ2tnUcw/uTVKp8ZljHm6Zm8MIRFuhyXVXuX4ToIuCtADKiRADRAZBbARSgbAJg0qWwnYMGnBZElwROVbSDoDngOAgvIX1YQoq9hH7KCllLaExtCR8ZzxDqpCHhI6lTT90XvWKROh1ZfbRbfallHKizVPX1KmCzZtQ4A8vHgDucwSVMJaD0UUB5BeqtDkcJ1HNKoEdLwPKIM1AChgFnxAxmBHB6iMDCNOCBH69FYJ158LhFcUjw6VnQR0XGI87Q/AnA6ZM/6fMXTlZmKarzJ8cVcY8tiKnx+dMRZ2D+eA44IyYSx4DTQwJOvATS8+NRAvPzuSTgdLQEnEWcoRJwwBkjgQCcwXsBl4DSR8OwFygfoKBRw5F7Qa+FiCf3gl4SiDziPDJ8Ec5ROtzPRB2+6B6knm4rFGT0VmiUq3EGTSTBAGVw/QkOKCM2YyEAZ0wZSMD5Xxk8vabpvaGXpjriDNJU5oAyQhKJAWeEJJIAjoNoXVslhVvucVUWS3uvDX+TZVm4hxGGjsuqwv7G+33n0+Ge67bwP42TwbHTee/a9nLvgPPcq4nj6VaG660FMk0RLiEEp4q6Ay5r8PBZPLRJuYmtwt2M4I68tQuOTGzbtb4cfnY9rvFtb4pUHt8ipEZmghkXZ53OXBf8nvt3mUBI5Q4qREhE09LkoXBN1RyiummoPyMOMMwSU/gNywYgDdsJoZ2yql1YHN62XSs8Din3inexduDMxmlDjk9j3CXG2mJFmqUb6NXJUhJ8rQ1y9HVnd2/mLA0w5cDgQcl/qKGfxK/mrhtIzjwQtObeoVUxxl+DAiG5PN50dR7Te+5f9nCjck33abVwc0cTMB650WC3sr0uQQsbuKaNL5tTRNPG82Ji5dr+xqZZyBXUlO21L1AzZ0tEyjdKo3GI0LwbqYjTqBmoBFsrUDk4BvVADKqRPp2kY5IJxk0+Xp0ehOzqdlqtV2emuFZXVXGHJ1mWvcxeuVUty+7vs9fBkr28v/8H1a48pwMCAAIAAQADIu0how==
"""

def L1():
    """ Top left vertical glyph """
    M.draw.rect(TX, TY + SY / 2, THICK, SY / 2)


def L2():
    """ Bottom left vertical glyph """
    M.draw.rect(TX, TY, THICK, SY / 2)


def R1():
    """ Top right vertical glyph """
    M.draw.rect(TX + SX - THICK, TY + SY / 2, THICK, SY / 2)


def R2():
    """ Bottom right vertical glyph """
    M.draw.rect(TX + SX - THICK, TY, THICK, SY / 2)


def T1():
    """ Top horizontal glyph """
    M.draw.rect(TX, TY + SY - THICK, SX, THICK)


def T2():
    """ Middle horizontal glyph """
    M.draw.rect(TX, TY + SY / 2 - THICK, SX, THICK)


def T3():
    """ Bottom horizontal glyph """
    M.draw.rect(TX, TY, SX, THICK)


def get_digit(value, place):
    """ Get a decimal place for an integer number """
    return (value // (10 ** (place - 1))) % 10


def draw_digit(v0, v1):
    DIGIT = M.floor(get_digit(v0, v1))
    M.draw.color(255, 255, 255, 255)
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


def setup():
    RES = 80
    SX = 64 / NUM
    SY = 64

    THICK = 8
    SPACEX = (RES - SX * NUM) / (NUM + 1)
    SPACEY = (RES - SY) / 2

    TX = SPACEX
    TY = SPACEY


display = display1
M.draw.clear(0, 0, 0)
VALUE = cell1[0]

if display2 != 0:
    VALUE = M.min(VALUE, 9999)

    if VALUE < 10:
        NUM = 1
        setup()

        draw_digit(0, 1)
        display.drawFlush()

        display = display2
        M.draw.clear(0, 0, 0)
        draw_digit(VALUE, 1)
        display.drawFlush()

    elif VALUE < 100:
        NUM = 1
        setup()

        draw_digit(VALUE, 2)

        display.drawFlush()
        display = display2
        M.draw.clear(0, 0, 0)

        draw_digit(VALUE, 1)
        display.drawFlush()

    elif VALUE < 1000:
        NUM = 2
        setup()

        TX += SPACEX + SX
        draw_digit(VALUE, 3)
        TX -= SPACEX + SX

        display.drawFlush()
        display = display2
        M.draw.clear(0, 0, 0)

        draw_digit(VALUE, 2)
        TX += SPACEX + SX
        draw_digit(VALUE, 1)
        display.drawFlush()

    else:
        NUM = 2
        setup()

        draw_digit(VALUE, 4)
        TX += SPACEX + SX
        draw_digit(VALUE, 3)

        display.drawFlush()
        display = display2
        M.draw.clear(0, 0, 0)
        TX -= SPACEX + SX

        draw_digit(VALUE, 2)
        TX += SPACEX + SX
        draw_digit(VALUE, 1)
        display.drawFlush()

else:
    VALUE = M.min(VALUE, 999)

    if VALUE < 10:
        NUM = 1
        setup()
        draw_digit(VALUE, 1)
        TX += SPACEX + SX

    elif VALUE < 100:
        NUM = 2
        setup()
        draw_digit(VALUE, 2)
        TX += SPACEX + SX
        draw_digit(VALUE, 1)
        TX += SPACEX + SX

    else:
        NUM = 3
        setup()
        draw_digit(VALUE, 3)
        TX += SPACEX + SX
        draw_digit(VALUE, 2)
        TX += SPACEX + SX
        draw_digit(VALUE, 1)

    display.drawFlush()
