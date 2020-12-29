""" Implements the steam power switch """

POWER = battery1.sensor(M.at.powerNetStored)
CAPACITY = battery1.sensor(M.at.powerNetCapacity)
PERCENT = POWER / CAPACITY

if distributor1.enabled:
    distributor1.setEnabled(PERCENT < 0.75)
    switch1.setEnabled(PERCENT < 0.75)
else:
    distributor1.setEnabled(PERCENT < 0.25)
    switch1.setEnabled(PERCENT < 0.25)

