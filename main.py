# Importing all the modules
import time
import random

# Unnecessary loop for dramatic effect :D
t_end = time.time() + 3
while time.time() < t_end:
    cls_command = 'clear'
    if os.name in ('nt', 'dos'):
        cls_command = 'cls'
    os.system(cls_command)
    print(".")
    os.system(cls_command)
    print("..")
    os.system(cls_command)
    print("...")

# Random diceroll
roll = ['It\'s heads!', 'It\'s tails!']
print(random.choice(roll))
print("Dice icon by Icons8")
# Keep the window open
time.sleep(86400)