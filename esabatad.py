

import sys

t, b = [int(s) for s in input().split(" ")]
for i in range(1, t + 1):
    guess = ['-'] * b
    guessNumber = 1
    ready = False
    backGuess = False
    index = 0
    transfigurationConfirmed = True
    negatedFromOriginal = False
    reversedFromOriginal = False
    while guessNumber < 151 and not ready:
        if guessNumber % 10 == 1 and guessNumber != 1:
            transfigurationConfirmed = False
        if transfigurationConfirmed:
            if backGuess:
                print(b - index, flush=True)
            else:
                print(index + 1, flush=True)
            nextPosition = int(input())
            if backGuess:
                guess[b - index - 1] = nextPosition
                index += 1
                
            else:
                guess[index] = nextPosition
            backGuess = not backGuess
        else:
            pass
        ready = guess.count('-') == 0
        guessNumber += 1
    print(''.join(list(map(str, guess))), flush=True)
    response = input()
    if response == 'N':
        break
    

