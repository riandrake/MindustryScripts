"""
Name: Belt Saturation

Description: Displays saturation over a number of connected belts

Schematic: TBD
"""

CAPACITY = conveyor1.sensor(M.at.itemCapacity)
TOTAL = conveyor1.sensor(M.at.totalItems)
SATURATION = TOTAL

AVERAGE = cell1[0]
AVERAGE = AVERAGE if AVERAGE else 0

SAMPLES = cell1[1]
SAMPLES = SAMPLES if SAMPLES else 0
SAMPLES += 1

AVERAGE = (AVERAGE * (SAMPLES-1) + SATURATION) / SAMPLES

cell1[0] = AVERAGE
cell1[1] = SAMPLES

AVERAGE = M.floor(AVERAGE * 100) / 100

M.print(' Saturation: ')
M.print(SATURATION)
M.print(' Average: ')
M.print(AVERAGE)
M.print(' Samples: ')
M.print(SAMPLES)
message1.printFlush()