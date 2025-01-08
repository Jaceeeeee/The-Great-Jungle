import os
from time import sleep
import sys

def type(text):
    for i in text :
        print(i, end = "", flush=True)
        sleep(.04)
type("\nTo begin this choose your own adventure journey,\nWhat is your travelers name?:\n")
name = input("\n")
#different so the text after the 'type' line will be on the same line#
def type(text, end = ""):
    for i in text :
        print(i, end = "", flush=True)
        sleep(.04)

type("\nHello, ")
print(name, end = "!")
#same as the first typewriter code#
def type(text):
    for i in text :
        print(i, end = "", flush=True)
        sleep(.04)
    print("")

#restart code function#
def restart_code():
    type("\nRestart?\n\n(yes/no)")
    answer = input("\n")
    if answer == "yes":
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif answer == "no":
        print()
    else:
        print()

type( "\nMake sure to read all instructions carefully!\nYou have just woken up in the middle of the forest, confused.\nWhen you first wake up, there is a strange man on a horse.")
type("Talk to him? \n(yes/yes)<-these are your options, make sure to type EXACTLY what they read:\n")
answer = input("")
if answer == "yes" :
    print("")
    print(name, end = "")
    type(": Where am I??")
    sleep(0.5)
    type("\nInconspicuous Stranger : You are in the great jungle, filled with various temples, ancient trees and beautiful waterfalls.")
    sleep(1)
    print("")
    print(name, end = "")
    type(": How do I get home?")
    sleep(0.5)
    type("\nInconspicuous Stranger : I may deliver you home, for a price of 10 rubies")
    sleep(1)
    print("")
    print(name, end = "")
    type(": I don't have 10 rubies though...")
    sleep(0.5)
    type("\nInconspicuous Stranger : Well then you have to find some...")
    type("...")
    sleep(1)
    type("Where would you like to go?" " (left/right):\n")
    answer = input("")
    if answer == "left" :
        type("\nAfter walking for 5 minutes, you see a temple, would you like to enter or keep walking?" " (enter/walk):\n")
        answer = input("")
        if answer == "enter":
            print("")
            type("Upon entering, you see two staircases, one going up and down, both staircases are flooded with darkness and you cannot see anything.")
            type("\nWhat to do, what to do... (up/down):\n")
            answer = input("")
            if answer == "up":
                type("\nYou didn't see a tripwire and stepped on it. It triggered an arrow and you died. You Lose!")
                restart_code()
            elif answer == "down":
                    type("\nYou enter the basement and find a chest! Open it? (yes/no):\n")
                    answer = input("")
                    if answer == "yes":
                        type("\nYou find 10 rubies in the chest!")
                        type("\nYou return to the Inconspicuous Stranger. Talk to him? (yes/no):")
                        answer = input ("")
                        if answer == "yes":
                            type("\nInconspicuous Stranger : I see you have 10 rubies! Would you like to spend them on a trip back?")
                            sleep(1)
                            print(name, end = " ")
                            type(": Yes!")
                            type("YOU WIN!!!")
                        elif answer == "no":
                            type("\nYou went through all that trouble to NOT talk to him? Wow, just wow. You lose.")
                            restart_code()
                        else:
                            type("Invalid response! You lose!")
                            restart_code()
                    elif answer == "no":
                        type("\nWell then, what was the point in entering the temple in the first place??!?! You lose.")
                        restart_code()
                    else: 
                        type("Invalid response! You lose!")
                        restart_code()
            else: 
                type("Invalid response! You lose!")
                restart_code()
        elif answer == "walk":
            print("")
            type("You keep walking and see a huge waterfall.")
            type("Upon looking closer, there seems to be rubies behind the waterfall as well as deep inside the water pool.")
            type("It seems you could dive to get the rubies in the pool and jump to get the rubies behind the waterfall. \n\nWhich one would you like to go for? (dive/jump): \n")
            answer = input("")
            if answer == "dive":
                type("\nAfter diving into pool of the waterfall, you can't hold you breath and end up dying! Sorry, but you lose!")
                restart_code()
            elif answer == "jump":
                type("\nThere seems to be atleast 20 rubies here! Would you like to try to collect them all of only take 10? (10/20):\n")
                answer = input("")
                if answer == "20":
                    type("\nYou grab all 20 rubies and rush out the waterfall. \nBut, uh oh! It was too heavy! You end up falling in the pool of the waterfall and drowning. \nYou lose!")
                elif answer == "10":
                    type("\nYou grab only 10 rubies and make it out the waterfall unscathed! ")
                    type("\nWould you like to go back now? (yes/no):\n")
                    answer = input("")
                    if answer == "no":
                        type("You wander around the jungle a bit more and get lost! No way back home :( You lose!)")
                        restart_code()
                    elif answer == "yes":
                        type("\nYou return to the Inconspicuous Stranger. Talk to him? (yes/no):\n")
                        answer = input ("")
                        if answer == "yes":
                            type("\nInconspicuous Stranger : I see you have 10 rubies! Would you like to spend them on a trip back?")
                            input("\n>>>\n")
                            print(name, end = " ")
                            type(": Yes!")
                            type("YOU WIN!!!")
                        elif answer == "no":
                            type("What is the point of this? All these rubies to eat??? You lose.")
                            restart_code()
                        else:
                            type("Invalid response! You lose.")
                            restart_code()
                    else:
                        type("Invalid response! You lose.")
                        restart_code()
                else:
                    type("Invalid response! You lose.")
                    restart_code()
            else:
                type("Invalid response! You lose.")
                restart_code()
        else:
            type("Invalid response! You lose.")
            restart_code()



                        
    elif answer == "right" :
        type("\nYou walk about ten minutes to the right and see a bustling village.\nYou hear mutters of wolves, and there seems to be a village to do lists filled with quests for rubies!\nWould you like to see it? (yes/no):\n")
        answer = input("")
        if answer == "yes" :
            type("\nUpon looking at the tasks, you see two that will get you your ten rubies and that seem not too difficult!" )
            type("The tasks are 'Find Tyrone's Dog' and 'Make me a sword.'\nWhich would you like to do? (dog/sword):")
            answer = input("")
            if answer == "dog":
                type("After searching around for 30 minutes you see 2 tracks of what could be a dog's footprints, one that goes left and one that goes forward.\nWhat to do what to do... (left/forward)")
                answer = input("")
                if answer == "\nleft\n":
                    type("You follow the path left and it leads you to a pack of wolves! Unfortunately, they eat you. You lose.")
                    restart_code()
                elif answer == "forward":
                    type("You follow the path forward and low and behold, you see a dog!\nYou check its tag, and it says Tyrone!\nYou then pick the dog up and go to Tyrone to collect your payment.")
                    type("\nYou return to the Inconspicuous Stranger. Talk to him? (yes/no):")
                    answer = input ("")
                    if answer == "yes":
                        type("\nInconspicuous Stranger : I see you have 10 rubies! Would you like to spend them on a trip back?")
                        input("\n>>>\n")
                        print(name, end = " ")
                        type(": Yes!")
                        type("YOU WIN!!!")
                    elif answer == "no":
                        type("Did you even want to go home? You lose :()")
                        restart_code()
                    else:
                        type("Invalid response! You lose!")
                        type("\nRestart?\n\n(yes/no)")
                        restart_code()
                else:
                    type("Invalid respose! You lose!")
                    restart_code()
            elif answer == "sword":
                type("You look closer at the pamphlet and see the materials to make a sword are only two wooden sticks!")
                type("Realising you don't have any, you look around and see two wooden sticks on a windowsill. Would you like to steal them or find your own?")
                type("(steal/find):\n\n")
                answer = input()
                if answer == "steal":
                    type("While trying to steal the wooden sticks the man who owns the house catches you and beats you up... You lose!")
                    restart_code()
                elif answer == "find":
                    type("You look around the forest and realize you're in a forest! There are so many wooden sticks laying around! Who would be dumb enough to steal them right?")
                    type("Anyways, you find some and magically, BOOM! A sword!")
                    type("Returning the sword to the person in the flier, you recieve 10 rubies!")
                    type("\nYou return to the Inconspicuous Stranger. Talk to him? (yes/no):")
                    answer = input ("")
                    if answer == "yes":
                        type("\nInconspicuous Stranger : I see you have 10 rubies! Would you like to spend them on a trip back?")
                        input("\n>>>\n")
                        print(name, end = " ")
                        type(": Yes!")
                        type("YOU WIN!!!")
                    elif answer == "no":
                        type("All that effort for nothing? Thats not that smart... You lose!")
                        restart_code()
                    else:
                        type("Invalid response! You lose!")
                        type("\nRestart?\n\n(yes/no)")
                        restart_code()
            else: 
                type("Invalid response! You lose!")
                restart_code()

        elif answer == "no":
            print("")
            type("You think of other ways to make money, and the two that come to your head are busking and begging, almost the same, but different.\nHow would you lke to make your money? (busk/beg):\n")
            answer = input("")
            if answer == "busk":
                type("\nYou begin singing and dancing on the street, and it's so horrendous that a villager pays you 10 rubies to stop!\n")
                sleep(1)
                type("...\n")
                sleep(1)
                type("Will you actually stop though? (yes/no):\n")
                answer = input("")
                if answer == "yes":
                    type("Okok, you're a good person I see. Would you like to return to the Inconspicuous Stranger? (yes/no)")
                    answer = input("")
                    if answer == "yes":
                        type("\nYou return to the Inconspicuous Stranger. Talk to him? (yes/no):\n")
                        answer = input ("")
                        if answer == "yes":
                            type("\nInconspicuous Stranger : I see you have 10 rubies! Would you like to spend them on a trip back?")
                            input("\n>>>\n")
                            print(name, end = " ")
                            type(": Yes!")
                            type("YOU WIN!!!")
                        elif answer == "no":
                            type("You have no other use for the rubies. Put the fries in the bag lil' bro. You lose!")
                            restart_code()
                        else:
                            type("Invalid response! You lose.")
                            restart_code()
                elif answer == "no":
                    type("The villager came back with a group and they all beat you up. You lose!")
                    restart_code()
                else:
                    print()
                    type("Invalid response! You lose.")
                    restart_code()
            if answer == "beg":
                type("\nThe villages get annoyed at your begging and they pick you up and walk 15 minutes to a waterfall where they throw you in. You drown and die. You lose :(")
                restart_code()
        else: 
            type("Invalid response! You lose.")
            restart_code()
    else:
        type("Invalid response! You lose." )
        restart_code()
else:
    type("\nThe only answer was yes! You lose!")
    restart_code()
   
    
  
