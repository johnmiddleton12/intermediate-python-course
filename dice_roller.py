import random


def roll_dice():
    dice_rolls = [random.randint(1, 6) for i in range(3)]
    return dice_rolls


def find_score(rolls):  # score if doubles is first index
    if rolls[0] == rolls[1] == rolls[2]:  # if trips, level is first, second index is 7
        score = [rolls[0], 7]  # score if nothing is [0,0]
    elif rolls[0] == rolls[1]:
        score = [rolls[2], rolls[0]]
    elif rolls[1] == rolls[2]:
        score = [rolls[0], rolls[1]]
    else:
        score = [0, 0]
    return score


def find_winner(a, b):
    if a == b:  # if equal, is a tie
        winner = 0
    elif a[1] == b[1]:
        if a[0] > b[0]:
            winner = 1
        else:
            winner = 2
    elif a[1] == 7:
        winner = 1
    elif b[1] == 7:
        winner = 2
    elif a[0] == b[0]:
        if a[1] > b[1]:
            winner = 1
        else:
            winner = 2
    elif a[0] > b[0]:
        winner = 1
    else:
        winner = 2

    return winner


def main():
    # old program

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
        # dice = [1, 1, 1]
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
            # dice2 = [4, 4, 6]
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
                winner = find_winner(score1, score2)
                if winner == 0:
                    print('Tie!')
                elif winner == 1:
                    print('Congrats,', user1, 'you won!')
                else:
                    print('Congrats,', user2, 'you won!')

        var = input('Do you want to keep playing? Y/N \n')


if __name__ == "__main__":
    main()
