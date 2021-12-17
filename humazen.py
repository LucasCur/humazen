import os
from os import walk

def create_profile():
    print("Creating goes here")

def load_profile(profile):
    strength = 0 
    vitality = 0 
    focus = 0 
    state = 0 
    for i, row in enumerate(open("saves/" + profile + ".hz")): 
    #  LOAD STRENGTH
        if i in range(0,1): 
            strength = (row)
    #  LOAD VITALITY
        if i in range(1,2): 
            vitality = (row)
    #  LOAD FOCUS
        if i in range(2,3): 
            focus = (row)
    #  LOAD STATE
        if i in range(3,4): 
            state = (row)
    display_profile(strength, vitality, focus, state)

filenames = next(walk("saves"), (None, None, []))[2]  # [] if no file
if len(filenames) < 1:
    print("No prior saves found - initialising profile creation.")
    create_profile()
else:
    debounce = False
    for i in range(0, len(filenames)):
        if ".hz" in filenames[i]:
            debounce = True
    if debounce == True:
        amount = 0
        for i in range(0, len(filenames)):
            if ".hz" in filenames[i]:
                amount += 1
        print("We've found " + str(amount) + " save/s for you, would you like to load any of them or create a new profile?\n\nSaves: ")
        for i in range(0, len(filenames)):
            if ".hz" in filenames[i]:
                savedisplay = filenames[i]
                savedisplay = savedisplay[:-3]
                print(" | " + savedisplay)
        print("\n[Type 'NEW' to create a new save, or specify the save name to load it!]")
        choice = input(" | ")
        load_profile(choice)
    else:
        print("No prior saves found - initialising profile creation.")
        create_profile()
input()

