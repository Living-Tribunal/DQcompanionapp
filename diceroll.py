from tkinter import *
from tkinter import font, Tk
from PIL import ImageTk, Image
import random

#================ Sets resolution, icon and app name at the top of the window
def showDice():

    diceRollWindow = Toplevel()
    diceRollWindow.geometry('360x720')
    diceRollWindow.title('Roll Dice')
    diceRollWindow.configure(bg = "dark gray")
    diceRollWindow.grab_set()
    
#================ list of dice face images and creating variables for random dice roll
    dice = ['Images\dice\Dice1.png', 'Images\dice\Dice2.png',
            'Images\dice\Dice3.png', 'Images\dice\Dice6.png',
            'Images\dice\Dice4.png', 'Images\dice\Dice5.png']
    diceOne = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    diceTwo = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#================ label for each dice
    diceLabelOne = Label(diceRollWindow, image = diceOne)
    diceLabelTwo = Label(diceRollWindow, image = diceTwo)

#================ keeping reference to the image    
    diceLabelOne.image = diceOne
    diceLabelTwo.image = diceTwo

#================ packing the label to the parent    
    diceLabelOne.pack(expand = True, fill = None)
    diceLabelTwo.pack(expand = True, fill = None)

#================ dice roll function
    def rollDice():
        diceOne = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        diceLabelOne.configure(image=diceOne, bg = "black")
#=============== Image reference
        diceLabelOne.image = diceOne
        
        diceTwo = ImageTk.PhotoImage(Image.open(random.choice(dice)))

        diceLabelTwo.configure(image=diceTwo, bg = "black")
#=============== Image reference
        diceLabelTwo.image = diceTwo

    rollDiceFrame = Frame(diceRollWindow, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)    
    rollDiceButton = Button(rollDiceFrame, highlightthickness = 0, font= ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919",  command = rollDice, relief = FLAT, width = 8, height = 1, wraplength = 150, text=("Roll Dice"))   
    rollDiceFrame.place(relx = 0.70, rely = 0.008, anchor = NE)
    rollDiceButton.pack(pady = (0,.5))  

    diceRollWindow.mainloop()