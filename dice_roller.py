import random

def main():
  dice_rolls = 2
  s = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1,6)
    s += roll
    print(f'You rolled {roll}')
  print(f'Total rolls: {s}')

if __name__== "__main__":
  main()
