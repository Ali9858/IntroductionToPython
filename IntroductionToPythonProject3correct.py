# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random as r
import simplegui

num = 0
counter = 0
num_range = 0

# helper function to start and restart the game
def new_game():
    global num, counter
    if num_range != 1:
        num = r.randrange(0,100) # The range shouldn't include 100 as secret number
        counter = 7 # 7 tries for 100
        print "\nNew game.\nRange is between 0 and 100\
        \nNumber of remaining guesses ", counter
        print""
    else:
        num = r.randrange(0,1000) # The range shouldn't include 1000 as secret number
        counter = 10 # 10 tries for 1000
        print "\nNew game.\nRange is between 0 and 1000\
        \nNumber of remaining guesses ", counter
        print""

def range100():
    # button that changes the range to [0,100) and starts a new game
    global num_range
    num_range = 0
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global num_range
    num_range = 1
    new_game()   
    
def input_guess(guess):
    global counter, player
    counter -= 1
    player = guess
    g = int(guess)
    
    # check if entered value is out of range
    if g > 99 and num_range != 1:
        print "Your input is out of range.\
        \nPlease select a number between [0,100)\
        \nYou have {} remaining guesses\
        \nLower".format(counter)
        print""
        return 
    elif g > 999 and num_range == 1:
        print "Your input is out of range.\
        \nPlease select a number between [0,1000)\
        \nYou have {} remaining guesses\
        \nLower".format(counter)
        print""
        return
    else:
        if g > num:
            response = "Lower"
        elif g < num:
            response = "Higher"
        else:
            response = "Correct!"
        if counter > 0 and g != num:
            print "Guess was {}\
            \nnumber of remaining guess is {}\
            \n{}".format(player, counter, response)
            print ""
        elif counter > 0 and g == num:
            print "Guess was {}\
            \nnumber of remaining guess is {}\
            \n{}".format(player, counter, response)
            print ""
            new_game()
        else:
            print "Guess was {}\
            \nThat was your last chance\
            \nThe correct number was {}".format(player, num)
            new_game()
    
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

reset = f.add_button("Reset", new_game, 200)
button100 = f.add_button("Range [0,100)", range100, 200)
button1000 = f.add_button("Range [0,1000)", range1000, 200)

inp = f.add_input("Enter a guess", input_guess, 200)
# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
