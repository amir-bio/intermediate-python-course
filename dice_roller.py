import random

def main():
  dice_rolls = 2
  s = 0

  for i in range(0, dice_rolls):
    roll = random.randint(1,6)
    s += roll
    if roll == 1:
      print( 'You rolled a 1! Critical Fail :(')
    elif roll == 6:
      print('You rolled a 6! Critical Success! :)')
    else:
      print(f'You rolled a {roll}')
  print(f'Total rolls: {s}')

if __name__== "__main__":
  main()
