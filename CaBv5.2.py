#Cows 'N Bulls
import random


#Rules Function which displays rules for the game
def rules():
    print "*********************************************************"
    print "                         WELCOME                         "
    print "*********************************************************"
    print "                LET'S PLAY COWS 'N BULLS !               "
    print " ********************************************************"
    print "                          RULES"
    print " ********************************************************"
    print
    print " YOU CAN CHOOSE TO PLAY A SINGLE PLAYER GAME WITH THE "
    print "      COMPUTER OR YOU CAN PLAY WITH ANOTHER PLAYER."
    print
    print " ********************************************************"
    print
    print " A COW SIGNIFIES THAT A DIGIT FROM YOUR GUESS IS CORRECT "
    print "            BUT IS AT THE INCORRECT POSITION             "
    print " A BULL SIGNIFIES THAT A DIGIT FROM YOUR GUESS IS CORRECT"
    print "             AND IS AT THE CORRECT POSITION              "
    print
    print " ********************************************************"
    print
    print " YOU WILL HAVE 10 CHANCES TO CORRECLY GUESS THE REQUIRED "
    print "               NUMBER OR WORD (GET 4 BULLS)              "
    print "                 IF YOU DON'T, TRY AGAIN !               "
    print
    print " ********************************************************"
    print
    print "     THIS GAME WAS CREATED BY REUBEN, VISHNU AND AMAN    "
    print
    print " ********************************************************"
    



#Gameplay For Word Guessing Option
def wordGameplay(word):
    count=0
    exitchoice=''
    print
    print
    flag=True
    while count<=9 and flag:
        nflag=True
        bulls=0
        cows=0
        guess=[]

        print "Chance Number: ",count+1
        g=raw_input("Enter Your Guess: ")
        g=g.upper()

        for i in range(len(g)):
            for j in range(i+1,len(g)):
                if g[i]==g[j]:
                    nflag=False
            
        if g.isalpha(): #Checking if the user input is a word
            for i in range(len(g)):
                guess.append(g[i])
                

            if nflag==True:
                if len(g)==4:  #Checking size of user input
                    for i in range(len(guess)):
                        if guess[i] in word:
                            if guess[i]==word[i]:
                                bulls=bulls+1  #Incrementing Bulls Counter
                            else:
                                cows=cows+1    #Incrementing Cows Counter
                    print "Number of Cows: ",cows
                    print "Number of Bulls: ",bulls
                    print
                    count=count+1
                            
                    if bulls==4:  #Checking if user has correctly guessed the word
                        if count==1:
                            word1="TRY"
                        else:
                            word1="TRIES"
                        print "CONGRATULATIONS !!"
                        print "YOU HAVE CORRECTLY GUESSED THE WORD AFTER", count, word1
                        flag=False
                        print

                        #Asking user to continue or stop
                        exitchoice=raw_input("Press Enter To Start Another Round Or Type 'Quit' : ")  
                        exitchoice=exitchoice.upper()
                        if exitchoice!='QUIT':
                            print
                            gamestart()
                        else:
                            print
                            print "Thanks For Playing !"
                    
                else:
                    print "Enter A 4 Letter Word"
                    print
            else:
                print "Letters Must Be Unique"
                print
        else:
            print "Enter Only A Word"
            print
    if count==10 and flag==True:
        print "SORRY, GAME OVER. BETTER LUCK NEXT TIME"
        print "THE CORRECT WORD WAS:",
        for i in range(len(word)):
            print word[i],
        print
        print

        #Asking user to continue or stop
        exitchoice=raw_input("Press Enter To Start Another Round Or Type 'Quit' : ")  
        exitchoice=exitchoice.upper()
        if exitchoice!='QUIT':
            print
            gamestart()
        else:
            print
            print "Thanks For Playing !"
                    
                

        



#Gameplay for number guessing option
def gameplay(number):
    flag=True
    count=0
    exitchoice=''
    print
    print 
    while count<=9 and flag==True:
        bulls=0
        cows=0
        nflag=True
        guess=[]

        print "Chance Number ",count+1
        g=raw_input("Enter Your Guess: ")
        if g.isdigit():  #Checking if the user input is a number
            for i in range(len(g)):
                guess.append(int(g[i]))
            
               
            for i in range(len(guess)):   #Checking if user enters unique digits
                for j in range(i+1,len(guess)):
                    if guess[i]==guess[j]:
                        nflag=False

            if len(g)==4:  #Checking Size of user input
                if guess[0]!=0:  #Checking if number begins with 0
                    if nflag==True: #Checking for unique digits
                
                        for i in range(len(guess)):
                            if guess[i] in number:
                                if guess[i]==number[i]:
                                    bulls=bulls+1  #Incrementing Bulls Counter
                                else:
                                    cows=cows+1    #Incrementing Cows Counter
                        print "Number of Cows: ",cows
                        print "Number of Bulls: ",bulls
                        print
                        count=count+1
                    
                        if bulls==4: #Checking if user has guessed the correct number
                            if count==1:
                                word="TRY"
                            else:
                                word="TRIES"
                            print "CONGRATULATIONS !!"
                            print "YOU HAVE CORRECTLY GUESSED THE NUMBER AFTER", count, word
                            flag=False
                            print

                            #Asking user to continue or stop
                            exitchoice=raw_input("Press Enter To Start Another Round Or Type 'Quit' : ")
                            exitchoice=exitchoice.upper()
                            if exitchoice!='QUIT':
                                print
                                gamestart()
                            else:
                                print
                                print "Thanks For Playing !"
                    
                    else:
                         print "Digits Must Be Unique"
                         print
                else:
                    print "Number must not begin with 0"
                    print

            else:
                     print "Enter a 4 digit number "
                     print
                
                
        else:
             print "Enter Only a Number "
             print

    if count==10 and flag==True:
        print "SORRY, GAME OVER. BETTER LUCK NEXT TIME"
        print "THE CORRECT NUMBER WAS:",
        for i in range(len(number)):
            print number[i],
        print
        print

        #Asking user to continue or stop
        exitchoice=raw_input("Press Enter To Start Another Round Or Type 'Quit' : ")  
        exitchoice=exitchoice.upper()
        if exitchoice!='QUIT':
            print
            gamestart()
        else:
            print
            print "Thanks For Playing !"

    
    
#Singleplayer number mode initialization
def singleplayer():
    number=random.sample(xrange(1,10),4)  #Randomly generating a 4 digit unique number
    gameplay(number)



#Multiplayer number mode initialization
def multiplayer():
    number=[]
    flag=True
    while flag:
        nflag=True
        no=(raw_input("Player 1 Enter a 4 Digit Number For Player 2 To Guess: "))  #Accepting number from Player 1
        for i in range(len(no)):
            for j in range(i+1,len(no)):
                if no[i]==no[j]:
                        nflag=False

                        
        if no.isdigit() and len(no)==4 and nflag==True:
            flag=False
        else:
            print "Invalid Input !"
            print "Enter Only A 4 Digit Number With Unique Digits"
            print
    for i in range(200):
        print 

    for i in range(len(no)):
            number.append(int(no[i]))
    print "Player 2: GUESS THE NUMBER !!"
    gameplay(number)



#Multiplayer Word Mode Initialization
def wordMultiplayer():
    word=[]
    flag=True

    while flag:
        nflag=True
        wd=(raw_input("Player 1 Enter a 4 Letter Word For Player 2 To Guess: ")) #Accepting word from Player 1
        wd=wd.upper()

        for i in range(len(wd)):
            for j in range(i+1,len(wd)):
                if wd[i]==wd[j]:
                    nflag=False

                    
        if wd.isalpha() and len(wd)==4 and nflag==True:
            flag=False
        else:
            print "Invalid Input !"
            print "Enter Only A Word With 4 Unique Letters"
            print
        
    for i in range(200):
        print

    for i in range(len(wd)):
        word.append(wd[i])
    print "Player 2: GUESS THE WORD !!"
    wordGameplay(word)
            
        
#Function to Initialize Game
def  gamestart():

    print
    print "           LET'S PLAY !!         "
    print
    print "***********GAME MODES************"
    print "1. SINGLE PLAYER NUMBER GUESSING"
    print "2. MULTI PLAYER NUMBER GUESSING"
    print "3. MULTI PLAYER WORD GUESSING"
    print "*********************************"
    print

    flag1=True
    while flag1:
        choice=raw_input("Enter Your Choice: ")
        if choice=='1' or choice=='2' or choice=='3':
            flag1=False
            print
        else:
            print "Invalid Choice !"
            print
    if choice=='1':
        singleplayer()
    elif choice=='2':
        multiplayer()
    else:
        wordMultiplayer()


#Main Program Body
rules()
gamestart()

    

