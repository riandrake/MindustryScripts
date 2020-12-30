"""
Name: Steam Switch

Description: Enables a distributor when power falls below 25%, then disables it again once power hits 75%.
             Intended for use on coal lines that are headed towards steam generators. Useful when you typically have enough
             solar power + batteries to manage the power of your base, but would like a contingency.

Schematic: bXNjaAF4nAFyAY3+AAIAAwIABG5hbWUADFN0ZWFtIFN3aXRjaAALZGVzY3JpcHRpb24AAAMAC2Rpc3RyaWJ1dG9yAAdiYXR0ZXJ5AA9taWNyby1wcm9jZXNzb3IAAAADAAAAAAAABAEAAAACAAICAAEAAg4AAAEFeJyFkU1OwzAQhR2xAFkcYk6AmpaSLqmiLNiUqkRCrJCTDGqQsYPtEHJoroCxk/QHFBV54/G8970nOSAk+NIotFTwrELImDGo2hBuK9mgWqF5MFJhQTUaWN8/Jhsvo3vHdMQRs4rlpWk7T7xcL+O79MlrqaygKD/cdTawdtsen2ziZJX69SHg2jm0UWVWux4uBAXLuOvzWr9VEM4A32vGO90L4xp9BEet0y0T7nW+h06uojnNpTBKchggv9FePfHnD+PmNEM3pcm3YSfs7X21CBhvWKvhc7RZdESd/tssGm22OM04NFsMdhQFJYSckYvdr1nr5vNBSQI3XB5HW2u/fwAfSbFmAsKBlf0=
"""

POWER = battery1.sensor(M.at.powerNetStored)
CAPACITY = battery1.sensor(M.at.powerNetCapacity)
PERCENT = POWER / CAPACITY

if switch1.enabled:
    distributor1.setEnabled(True)
else:
    if distributor1.enabled:
        distributor1.setEnabled(PERCENT < 0.75)
    else:
        distributor1.setEnabled(PERCENT < 0.25)

