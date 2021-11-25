# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s):
# Date:
# Description:

from cmpt120imageProjHelper import *
from cmpt120imageManip import *
import tkinter.filedialog
import pygame
pygame.init()

# list of system options
# ***TO-DO: populate it to provide more functionalities***
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Original Image"
         ]

# list of basic operation options
# ***TO-DO: populate it to provide more functionalities***
basic = [
          "1: Apply Red Filter",
          "2: Apply Green Filter",
          "3: Apply Blue Filter",
          "4: Apply Sepia Filter",
          "5: Apply Warm Filter",
          "6: Apply Cold Filter",
          "7: Switch to Avanced Functions"
         ]

# list of advanced operation options
# ***TO-DO: populate it to provide more functionalities***
advanced = [
                "1: Switch to Basic Functions",
             ]
# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("***TO-DO: Update this line to show the proper information***")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("***TO-DO: Update this line to show the proper information***")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
    Input:  state - a dictionary containing the state values of the application
            img - the 2d array of RGB values to be operated on
    Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        # ***TO-DO: add the rest to handle other system functionalities***
        elif userInput == 'O':
            tkinter.Tk().withdraw()
            openFilename = tkinter.filedialog.askopenfilename()
            image = getImage(openFilename)
            state['lastOpenFilename'] = openFilename
            showInterface(image, "Open", generateMenu(state))
            return image
        elif userInput == 'S':
            tkinter.Tk().withdraw()
            saveFilename = tkinter.filedialog.asksaveasfilename()
            saveImage(currentImg, saveFilename)
            state['lastSaveFilename'] = saveFilename

            showInterface(currentImg, "Open", generateMenu(state))
            return currentImg

        elif userInput == 'R':
            image = getImage(state['lastOpenFilename'])
            showInterface(image, "Open", generateMenu(state))
            return image

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        # ***TO-DO: add the rest to handle other manipulation functionalities***
        if state["mode"] == "basic":
            if userInput == "1":
                print("Log: Performing " + basic[int(userInput)-1])
                image = getImage(state['lastOpenFilename'])
                image = applyRedFilter(image)
                showInterface(image, "Open", generateMenu(state))
                return image
            elif userInput == '2':
                print("Log: Performing " + basic[int(userInput)-1])
                image = getImage(state['lastOpenFilename'])
                image = applyGreenFilter(image)
                showInterface(image, "Open", generateMenu(state))
                return image
            elif userInput == '3':
                print("Log: Performing " + basic[int(userInput)-1])
                image = getImage(state['lastOpenFilename'])
                image = applyBlueFilter(image)
                showInterface(image, "Open", generateMenu(state))
                return image
            elif userInput == '4':
                print("Log: Performing " + basic[int(userInput)-1])
                image = getImage(state['lastOpenFilename'])
                image = applySepiaFilter(image)
                showInterface(image, "Open", generateMenu(state))
                return image
            elif userInput == '5':
                print("Log: Performing " + basic[int(userInput)-1])
                image = getImage(state['lastOpenFilename'])
                image = applyWarmFilter(image)
                showInterface(image, "Open", generateMenu(state))
                return image
            elif userInput == '6':
                print("Log: Performing " + basic[int(userInput)-1])
                image = getImage(state['lastOpenFilename'])
                image = applyColdFilter(image)
                showInterface(image, "Open", generateMenu(state))
                return image

                # state["mode"] = "advanced"

                # ***TO-DO: use this format when you add the manipulation functionalities***
                # ***instead of setting the value of state["mode"]***
                # ***it is ok to go a bit beyond 100 characters when calling the showUserInterface***
                #img = cmpt120imageManip.applyRedFilter(img)
                #cmpt120imageProjHelper.showUserInterface(img, "Apply Red Filter ", generateMenu(state))

    else: # unrecognized user input
        print("Log: Unrecognized user input: " + userInput)
    return img

# *** DO NOT change any of the code below this point ***

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = getBlackImage(300, 200) # create a default 300 x 200 black image
showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.QUIT: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")