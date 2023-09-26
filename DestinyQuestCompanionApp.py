#================ imports needed libraries
from tkinter import *
from tkinter import Tk
import diceroll
import Images
import yourhero

#================ function used to call "Enter, Hero!"
def onEnterHero():
     yourhero.openYourHero()   
    
#================ function used to call diceroll
def onButtonClick():
    diceroll.showDice()   

def main():
    root = Tk()
    Images.destinyQuestImages()

#================ Sets resolution, icon and app name at the top of the window
    root.title("Destiny Quest")
    root.iconbitmap("Images/sword.ico")
    root.attributes('-fullscreen', True)
#================ Creating background for the main window
    destinyLabel = Label(root, image = Images.Images["destinyDungeonImage"])
    destinyLabel.pack()

#================ Enter Hero button on main window
    enterYourHero = Frame(root, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    enterYourHeroButton= Button(enterYourHero, highlightthickness = 0, font = ("Trajan Pro", 30, "bold"), fg = "white", bg = "#191919", command = onEnterHero, relief = FLAT, width=15,height=2, text=("Enter, Hero!"))
    enterYourHero.place(relx = 0.001, rely = 0.12) 
    enterYourHeroButton.pack(pady=(0,.5))

#================ Adjusting the position of the enter Hero button on main window
    enterYourHero.place(relx = 0.5, rely = 0.7, anchor = CENTER)

#================ Button to kill the program on main window
    exitButton = Button(root, image = Images.Images["backArrowImage"], highlightthickness = 0, bd = 0, command = exit)
    exitButton.pack()
#================ Adjusting the position of the exit button on main window
    exitButton.place(relx = 0.040, rely = 0.0, anchor = NE)
    
    root.mainloop()

if __name__ == "__main__":
    main()
