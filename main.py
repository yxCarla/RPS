import random

options = ['rock', 'paper', 'scissors']

player = False

playerscore = 0
aiscore = 0

while not player:
    ai = random.choice(options)
    player = input('Rock, Paper, Scissors? ')
    print(f'The AI played a... {ai}')
    if player == ai:
        print('Tie!')
        print(f'AI - {aiscore}')
        print(f'Player - {playerscore}')
    elif player == 'rock':
        if ai == 'paper':
            print('You lose! Paper beats rock!')
            aiscore += 1
            print(f'AI - {aiscore}')
            print(f'Player - {playerscore}')
        if ai == 'scissors':
            print('You win! Rock beats scissor!')
            print(f'AI - {aiscore}')
            playerscore += 1
            print(f'Player - {playerscore}')
    elif player == 'paper':
        if ai == 'scissors':
            print('You lose! Scissor beats paper!')
            aiscore += 1
            print(f'AI - {aiscore}')
            print(f'Player - {playerscore}')
        if ai == 'rock':
            print('You win! Paper beats rock!')
            print(f'AI - {aiscore}')
            playerscore += 1
            print(f'Player - {playerscore}')
    elif player in ('scissors', 'scissor'):
        if ai == 'rock':
            print('You lose! Rock beats scissor!')
            aiscore += 1
            print(f'AI - {aiscore}')
            print(f'Player - {playerscore}')
        if ai == 'paper':
            print('You win! Scissors beats paper!')
            print(f'AI - {aiscore}')
            playerscore += 1
            print(f'Player - {playerscore}')
    again = input('Would you like to go another round? ')
    if again.lower() in ('yes', 'y'):
        player = False
    elif again.lower() in ('no', 'n'):
        print('Goodbye!')
        player = True
