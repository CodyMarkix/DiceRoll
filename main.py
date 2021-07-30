# Importing all the modules
import time
import random
import os

# Variable for clearing the terminal
global cls_command
cls_command = 'clear'
if os.name in ('nt', 'dos'):
  cls_command = 'cls'

print("Welcome to the Dice roll program!\n\n")

# Function for menu
def menuInput():
  global menu_input
  menu_input = input("What would you like to do?\n(Available commands: roll, credits)\n\n")

menuInput()

# Function for the credits menu
def creditsMenu():
  os.system(cls_command)
  print("Program written by: CodyMarkix (a.k.a Markix | u/Hplr63)\nDice icon by Icons8\nProgram built with Pyinstaller\n")

# Function for rolling the die
def roll():
  # Unnecessary loop for dramatic effect :D
  t_end = time.time() + 3
  while time.time() < t_end:
      os.system(cls_command)
      print(".")
      os.system(cls_command)
      print("..")
      os.system(cls_command)
      print("...")

  # Random diceroll
  roll = ['It\'s heads!', 'It\'s tails!']
  os.system(cls_command)
  print(random.choice(roll))

  time.sleep(1)
  global roll_choice
  roll_choice = input("\nDo you want to roll again or exit to the menu?\n(r = roll; e = exit to menu)\n\n")

# If statements for the menu_input
if menu_input == ('roll'):
  roll()

if menu_input == ('credits'):
  creditsMenu()
  menuInput()

if roll_choice == ('r'):
    roll()
if roll_choice == ('e'):
   os.system(cls_command)
   menuInput()
