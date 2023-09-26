
#================ imports needed libraries
from PIL import Image, ImageTk
import random

Images = {}

def destinyQuestImages():
    global Images
#========== list for background images    
    background = ['Images/dungeonfp2.png', 'Images/dungeonfp.png', 'Images/dungeonfp3.png',
                  'Images/dungeonfp4.png','Images/dungeonfp5.png','Images/dungeonfp6.png',
                  'Images/dungeonfp7.png','Images/dungeonfp8.png','Images/dungeonfp9.png']    
    Images = {
#========= randomly imports the mainmenu picture       
        "destinyDungeonImage": ImageTk.PhotoImage(Image.open(random.choice(background))),

#========= Background Image for hero sheet
        "heroSheet": ImageTk.PhotoImage(Image.open("Images/twall.png")),
        
#========= Background Image for combat tracker
        "combatTrackerBackground": ImageTk.PhotoImage(Image.open("Images/twall.png")),
        
#========= images for back arrow on combattracker/mainpage
        "backArrowImage": ImageTk.PhotoImage(Image.open("Images/arrow.png").resize((75,75)))
        }

        