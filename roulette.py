import random
from time import sleep
from os import system

blackNumbers =  [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
redNumbers = [1, 3, 5, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

def roulette():
    num = random.randint(0, 36)
    return num

def mainGame(bet):
    """
    bet: Parameter to make the user not choose anything besides between 0 and 11.
    maxplay and stop: Defined to make the roulette go slower overtime.
    Returns the number that it stopped.
    """

    maxplay = 21
    stop = 0.10
    if bet in range(1, 11):
        for i in range(0, 3):
            for c in range(1, maxplay):
                system('cls')
                number = roulette()
                if number in blackNumbers:
                    print(f'Black {number}')
                elif number == 0:
                    print(f'Green 0')
                else:
                    print(f'Red {number}')
                sleep(stop)
            maxplay / 2
            stop += 0.20
        return number
    else:
        print('What did you expect? You lost.')
        pass
    

def checkWin(num, bet):
    """
    bet: The bet parameter given by the player
    num: The num recieved from mainGame() function.
    """
    if bet == 2:
        print('Your bet: 1 to 18')
        if num in range(1, 19):
            return "You won!"
    elif bet == 3:
        print('Your bet: Even')
        if num % 2 == 0:
            return "You won!"
    elif bet == 4:
        print('Your bet: Odd')
        if num % 2 != 0:
            return "You won!"
    elif bet == 5:
        print('Your bet: 19 to 36')
        if num in range(19, 37):
            return "You won!"
    elif bet == 6:
        print('Your bet: 1st 12')
        if num in range(0, 13):
            return "You won!"
    elif bet == 7:
        print('Your bet: 2nd 12')
        if num in range(12, 25):
            return "You won!"
    elif bet == 8:
        print('Your bet: 3rd 12')
        if num in range(24, 37):
            return "You won!"
    elif bet == 9:
        print('Your bet: Red')
        if num in redNumbers:
            return "You won!"
    elif bet == 10:
        print('Your bet: Black')
        if num in blackNumbers:
            return "You won!"
    return "Better luck next time."
    
system('cls')
while True:
    bet = int(input("""Place your bet!
[ 1 ] Number
[ 2 ] 1 to 18
[ 3 ] Odd
[ 4 ] Even
[ 5 ] 19 to 36
[ 6 ] 1st 12
[ 7 ] 2nd 12
[ 8 ] 3rd 12
[ 9 ] Red
[ 10 ] Black
"""))
    if bet == 1:
        numberGuess = int(input('Choose a number between 0-36: '))
        num = mainGame(bet)
        print(f'Your number: {numberGuess}')
        if numberGuess == num:
            print('You won!')
        elif numberGuess > 36:
            print('What did you expect?')
        else:
            print('Better luck next time.')
    else:
        num = mainGame(bet)
        print(checkWin(num, bet))
    ans = str(input('Do you wish to play again? [Y/N]: ')).upper().strip()
    if ans == 'N':
        print('Thanks for playing!')
        break
