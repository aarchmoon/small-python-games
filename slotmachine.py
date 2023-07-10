import random
from time import sleep
from os import system

def checkPrize(prize):
    prizesDict = {
        "🎱": 1000,
        "🍒": 750,
        "🍋": 500,
        "💲": 400,
        "🍇": 350,
        "🔷": 200,
        "🔔": 150,
        "🎵": 100,
        "📼": 50
    }
    
    return f"You won: {prizesDict.get(prize)} coins!"


slots = ["🎱", "🍒", "🍋", "🍇", "🔷", "🔔", "🎵", "📼", "💲"]
machine = [["", "", ""], 
           ["", "", ""], 
           ["", "", ""]]

count = 0

while count < 4:
    system('cls')
    for row in range(0, 3):
        for col in range(0, 3):
            machine[row][col] = random.choice(slots)
    for row in range(0, 3):
        for col in range(0, 3):
            print(f'[ {machine[row][col]} ]', end='')
        print()
    count += 1
    sleep(1)

if machine[1][0] == machine[1][1] and machine[1][1] == machine[1][2] and machine[1][2] == machine[1][0]:
    print('JACKPOT!')
    prize = machine[1][0]
    print(checkPrize(prize))
else:
    print('Better luck next time!')