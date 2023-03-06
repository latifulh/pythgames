#GAMES
# create a program using functions that will allow the user to chose 
# from 3 games and play
# Latiful Hoque

import random # allows use of the random function

msg1 = "  Games    "
msg2 = "-----------"
msg3 = "1 - Hangman"
msg4 = "2 - Number Guessing Game"
msg5 = "3 - Dice Game "
msg6 = "4 - Exit"
msg7 = "Please chose an option: "

def menudisp():
  print("\t"),msg1,("\n\t"),msg2,("\n"),msg3,("\n"),msg4,("\n"),msg5,("\n"),msg6,("\n"), # displays options

def hangman():
  print ("\n"),("You have been setenced to death")
  print "Only by guessing the word correctly can you be saved"
  print "Try to guess the word before you are hanged"
  print "You have 5 mistakes" # tells user game info
  lives = 5 # wrong gueses left
  word = "transformers" # word  too be guessed
  letters = "" #already guessed letters
  while lives!= 0: #until game over
    missing = 0 # number of letters left
    print "\n","\n", "you have {0} more tries".format(lives)
    print "here are your previous guesses: "
    print letters # prints previous guesses
    guess = raw_input("Guess a letter: ") #takes in guess letter
    letters = letters + guess # adds to list of guesses
    for  char in word: # for every letter in word
      if char in letters : # check if the guess matches
        print char, # if so print the ltter

      else:
        print "_", # if not then print a blank
        missing = missing +1 # number of missing letters increases
    
    if guess not in word:
      lives = lives -1 #lose a life if guess is wrong
      print "\n","Wrong!" #lt user know its wrong

    if missing ==0: # when no more missing letters
      print "\n","Correct"
      print  "\n","you live" , "\n", "for now" # game win
      break
    if lives == 0: # if lives depleted
      print "\n","Fortune doesnt favour fools"
      print "You lose" # game lose
      break # end


def numgame():
  print ("\n"),("I am thinking of a number between 1 and 100")
  print "Enter in a number and I will say higher or lower"
  print ("try to guess it in as few tries as possible"),("\n")
  # game info
  num = random.randint(1,100)# choses random number
  guessnum =0 # numer of guesse
  guess = input("Enter in a number: ") 
  guessnum = guessnum + 1 #increase number of guesses
  while guess != num: #until number is guessed corectly
    if guess > num:
      print "Lower" # user lower
      guessnum = guessnum + 1
    else :
      print "Higher" #or higher
      guessnum = guessnum + 1#increase number of guesses
    
    guess = input("Enter in a number: ")  
  print ("\n") ,("Correct! :)") 
  print ("You guessed the correct number in {0} tries").format(guessnum) # game win


def dice():
  print ("\n"),("I will roll 2 virtual dice")
  print "Bet odd or even"
  print "Your starting balnce is $10"
  print "If all your money is gone, so will your life"
  #game info
  balance = 10 # money remaining
  while balance> 0: #until all money is gone
    print ("\n") ,("your current balance is {0}".format(balance))
    bet = input("Enter in the amount you wish to bet: ")
    choice = input("(0)Even  or  (1)Odd? : ") 
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6) # rolls 2 dices
    print "Dice Rolling!"
    print(dice1),("and"),(dice2) # displays results
    sum = dice1 + dice2 #adds results
    if (sum % 2) == choice: # check if even or odd
      balance = balance + bet
    else:
      balance = balance - bet # lose or gain money
  print ("\n") ,("This is the end of the line for you")
  # game ends when mobey is gone
  
 

def game():
 option = input(msg7 ) # records choice
 while (option != 4): # until exit option not chosen
    if option == 1: # plays respective game
      hangman()
    elif option == 2:
      numgame()
    elif option ==3:
      dice()
    else:# if number entered not recognized
      game() #repeat this fuction
    print ("\n"),("\n")
    menudisp()
    option = input(msg7 )
 print "Goodbye"
 

menudisp()# display menu
game()# game directory