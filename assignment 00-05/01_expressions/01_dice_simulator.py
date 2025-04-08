import random


def roll_dice():
    die1: int = random.randint(1, 6)
    die2: int = random.randint(1, 6)

    print(f'''
{die1, die2}
Total of two dice: {die1 + die2}
''')



def main():
    roll_dice()
    roll_dice()
    roll_dice()



if __name__ == '__main__':
    main()