import os
from os import walk

def display_profile(s1, v, f, s2):
    print("Strength:\n | " + str(s1))
    print("Vitality:\n | " + str(v))
    print("Focus:\n | " + str(f))
    print("State:\n | " + str(s2))

def create_profile():
    print("Creating goes here")

def load_profile(profile):
    #  LOAD STRENGTH
    strength = 0 
    for i, row in enumerate(open("saves/" + profile + ".hz")): 
        if i in range(0,0): 
            strength = int(row)
    #  LOAD VITALITY
    vitality = 0 
    for i, row in enumerate(open("saves/" + profile + ".hz")): 
        if i in range(1,1): 
            vitality = int(row)
    #  LOAD FOCUS
    focus = 0 
    for i, row in enumerate(open("saves/" + profile + ".hz")): 
        if i in range(2,2): 
            focus = int(row)
    #  LOAD STATE
    state = 0 
    for i, row in enumerate(open("saves/" + profile + ".hz")): 
        if i in range(3,3): 
            state = int(row)
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
