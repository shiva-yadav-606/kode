def g():
    for i in range (5,0,-1):
        print('--------------TO GUESS THE NUMBER PRESS ENTER---------------')
        input()
        print('total guesses remaining =',i)
        m=int(input('enter your number = '))
        if m<0:
            print('enter a positive integer')
            g()
        elif m==23:
            print('23 is the correct number')
            break
        else :
            if m>=35:
                print('too high')
            elif 20<=m<=25:
                print('just there')
            elif  m<=10:
                print('too low')
            elif 11<=m<=19:
                print('a bit higher')
            elif 26<=m<=34:
                print('a bit lower')
    print("----------------thank u for playing-----------------")
    print('\n'*4)
    g()
g()