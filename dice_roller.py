import random

def roll_dice():
  dice_rolls = [random.randint(1, 6) for i in range(3)]
  return dice_rolls

def find_score(rolls):
  if rolls[0] == rolls[1] == rolls[2]:
    score = [rolls[0], 7]
  elif rolls[0] == rolls[1]:
    score = [rolls[2], rolls[0]]
  elif rolls[1] == rolls[2]:
    score = [rolls[0], rolls[1]]
  else:
    score = [0, 0]
  return score


def main():
  """
  dice_rolls = int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  dice_sum = 0

  for i in range(0, dice_rolls):
    roll = random.randint(1, dice_size)
    dice_sum += roll
    if roll == 1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll == 6:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      print(f'You rolled a {roll}')
  print(f'You have rolled a total of {dice_sum}')
  """
  print('Welcome to Ceelo!')

  user1 = input("Enter player 1's name: \n")
  user2 = input("Enter player 2's name: \n")

  var = 0
  while var != 'N':
    phrase = input(user1 + ' enter a lucky phrase: \n')
    dice = roll_dice()
    dice.sort()
    print('{}, you rolled a {}, {}, and a {}.'.format(user1, dice[0], dice[1], dice[2]))
    score1 = find_score(dice)
    if score1[1] == 7:
      print('Nice, trips!')
    if dice == [4, 5, 6]:
      print('Congrats,', user1, 'you won!!')
    elif dice == [1, 2, 3]:
      print('Too bad,', user1, 'you lost.')
    else:
      phrase = input(user2 + ' enter your lucky phrase: \n')
      dice2 = roll_dice()
      dice2.sort()
      print('{}, you rolled a {}, {}, and a {}.'.format(user2, dice2[0], dice2[1], dice2[2]))
      score2 = find_score(dice2)
      if score2[1] == 7:
        print('Nice, trips!')
      if dice2 == [4, 5, 6]:
        print('Congrats,', user2, 'you won!!')
      elif dice2 == [1, 2, 3]:
        print('Too bad', user2, 'you lost.')
      else:
        if score1 == score2:
          print('Tie!')
        elif score1[1] == score2[1]:
          if score1[0] > score2[0]:
            print('Nice job,', user1, 'you won!')
          else:
            print('Nice job,', user2, 'you won!')
        elif score1[0] > score2[0]:
          print('You won,', user1, 'nice job!')
        elif score1[0] == score2[0]:
          if score1[1] > score2[1]:
            print('Nice job,', user1, 'you won!')
          else:
            print('Nice job,', user2, 'you won!')
        else:
          print('You won,', user2, 'nice job!')





    var = input('Do you want to keep playing? Y/N \n')
if __name__== "__main__":
  main()
