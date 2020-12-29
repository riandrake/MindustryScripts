# MindustryScripts

### About
This is a collection of the python scripts I use to implement my logic processors in Mindustry. They are primarily for my personal use, but feel free to use the scripts as a reference or to copy/paste some of the code for yourself.

---

### Prerequisites
#### Minpiler
Description: Used to transpile python code into mlogic  
Link: https://github.com/neumond/minpiler/issues/14

---

### Compiling

You can simply follow the Minpiler instructions to get the same result, but I prefer to work from my IDE. To do so, I implemented `make.py` to make it easy for me to transpile any script file I'm looking at from PyCharm.

Very basically, either:

- Commandline: `python make.py $FileName$`
- IDE Configuration; Script: `make.py`, Arguments: `$FileName`

Here's a screenshot of my PyCharm configuration:

![alt text](https://github.com/riandrake/MindustryScripts/blob/main/images/pycharm_setup.png?raw=true)
---

### Using In-Game

After running/compiling, you should have both:
- A print-out of the transpiled code (for debugging)
- The transpiled code copied to your clipboard (for use in-game)

Just open your processor and paste in the code from your clipboard. Done!

Where relevant, I'll try to include a schematic link as well.