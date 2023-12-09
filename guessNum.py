def guessNumber():
    import random
    rnum = random.randrange(0,51)
    print("I'm thinking of a number in the range of 0-50. You have five tries to guess it.")
    count = 0
    while count < 5:
        num = input('Guess the number: ')
        if int(num) > rnum:
            print(str(num) + ' is too high.')
            count += 1
            continue
        elif int(num) < rnum:
            print(str(num) + ' is too low.')
            count += 1
            continue
        elif int(num) == rnum:
            return('You got it correct! I was thinking of ' + str(rnum) + '!')
            break
    if count == 5:
        return('The correct answer was ' + str(rnum) + '. Better luck next time.')
print(guessNumber())
