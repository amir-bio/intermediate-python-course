import random

def main():
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))

  s = 0

  for i in range(0, dice_rolls):
    roll = random.randint(1, dice_size)
    s += roll
    if roll == 1:
      print('You rolled a 1! Critical Fail :(')
    elif roll == dice_size:
      print(f'You rolled a {roll}! Critical Success! :)')
    else:
      print(f'You rolled a {roll}')
  print(f'Total rolls: {s}')

if __name__== "__main__":
  main()
