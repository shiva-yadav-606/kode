def kbc():
    print("------------------------------->WELCOME TO KBC<----------------------")
    var1 = input("enter your name= ")
    print()
    print("THIS GAME CONSISTS OF 3 QUESTIONS")
    print()
    print("EACH QUESTION HAS 3 CHOICES")
    print()
    print("FOR EACH CORRECT ANSWER YOU WIN $25,000")
    print()
    print("LET'S START THE GAME")
    while True:
        q1 = '''
            WHO INVENTED THE WORLD'S FIRST EVER ATOMIC BOMB ?\n
            (1)= Albert Einstein\n
            (2)= Rosalind Franklin\n
            (3)= Robert Oppenheimer
            '''
        print(q1)
        a = input('enter your choice = ')
        if a=='3':
            print("Robert Oppenheimer is the correct answer\n",var1,",YOU WON $25,000")
            print()
            print("TO ANSWER  SECOND QUESTION PRESS ENTER")
            input()
        else:
            print("wrong answer! ", var1, ",BETTER LUCK NEXT TIME")
            print("THANK U")
            break
        q2 = '''
        WHO INVENTED DESIGN OF THE MODERN ALTERNATING CURRENT ELECTRICITY SUPPLY SYSTEM?\n
        (1) Michael Faraday\n
        (2) C. V. Raman\n
        (3) Nikola Tesla
        '''
        print(q2)
        a = input('enter your choice = ')
        if a == '3':
            print("Nikola Tesla is the correct answer\n",var1,",YOU WON $50,000")

            print("TO ANSWER THIRD QUESTION PRESS ENTER")
            input()
        else:
            print("wrong answer! ", var1, ",BETTER LUCK NEXT TIME\nYOU WON $25,000")
            print("THANK U")
            # return 0
            break
        q3 = '''
        THE FIRST PRACTICAL PETROL ENGINE WAS BUILT IN 1876 IN GERMANY BY__\n
        (1) Camillo Castiglioni\n
        (2) Nicolaus Otto\n
        (3) Rudolf Diesel
        '''
        print(q3)
        a = input('enter your choice = ')
        if a == '2':
            print("Nicolaus Otto is the correct answer\n",var1,"YOU WON $75,000")
            print("-------------THANK U FOR PLAYING---------------")
            break
        else:
            print("wrong answer! ", var1, "BETTER LUCK NEXT TIME\nYOU WON $50,000")
            print("-------------THANK U FOR PLAYING---------------")
            break
    print('\n'*4)
    kbc()
kbc()