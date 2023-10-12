'''
DQ - Combat Tracker
Author: Cody Dalton
Date: 10/12/2023

Purpose: This module is used to populate the combat tracker window. 
Stats for the Hero and their opponent are tracked here as well as
having a handy-dandy dice roller avaliable if the player so wishes it. There are 
multiple boxes for each round of combat with an opponent.

'''


#================ imports needed libraries
from tkinter import *
from tkinter import messagebox
import Images
import diceroll

def onButtonClick():
    diceroll.showDice()

#================ Sets resolution, icon, and windowtitle
def combatTrackerSheet():
    combatTrackerWindow = Toplevel()
    combatTrackerWindow.title("Combat Tracker")
    combatTrackerWindow.iconbitmap("Images/sword.ico")
    combatTrackerWindow.attributes('-fullscreen', True)

    
#================ Creating canvas for background for the "Combat Tracker" window    
    combatTrackerWindowCanvas = Canvas(combatTrackerWindow, highlightthickness = 0, bd = 0)
    combatTrackerWindowCanvas.pack(expand = True, fill = BOTH)
    combatTrackerWindowCanvas.create_image(0,0, anchor = NW,image = Images.Images["combatTrackerBackground"])
        
#================ Button to kill the program on "Combat Tracker" window 
    exitButton = Button(combatTrackerWindow, image = Images.Images["backArrowImage"], highlightthickness = 0, bd = 0, command = combatTrackerWindow.destroy)

#================ Adjusting the position of the exit button on "Combat Tracker" window 
    exitButton.place(relx = 0.040, rely = 0.0, anchor = NE)

#================ Button to roll the dice on "Combat Tracker" window 
    rollTheDiceFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    rollDiceButton= Button(rollTheDiceFrame, highlightthickness = 0, font = ("Rockwell Extra Bold", 30, "bold"), fg = "white", bg = "#191919", command = onButtonClick, relief = FLAT, width=10,height=2, text=("Dice (2D6)"))
    rollTheDiceFrame.place(relx = 0.563, rely = 0.47) 
    rollDiceButton.pack(pady=(0,.5))

#================ This creates the banner on the combat tracker window for Opponents    
    opponentFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    opponentLabel = Label(opponentFrame, highlightthickness = 0, font = ("Steelworks Vintage Demo", 35, "bold"), text = "Opponents", fg = "#191919", bg = "white", relief = FLAT, width = 26, height = 1)
    opponentFrame.place(relx = 0.218, rely = 0.163) 
    opponentLabel.pack(pady = (0,.5))

#================ This creates the banner on the combat tracker window for the Hero
    heroFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    heroLabel = Label(heroFrame, highlightthickness = 0, font = ("Steelworks Vintage Demo", 35, "bold"), text = "Hero", fg = "#191919", bg = "white", relief = FLAT, width = 13, height = 1, wraplength= 250)
    heroFrame.place(relx = 0.629, rely = 0.163) 
    heroLabel.pack(pady = (0,.5))
 
#================ This creates the banner on the combat tracker window for the words combat tracker 
    combatTrackerBannerFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "black", relief = FLAT)
    combatTrackerBannerLabel = Label(combatTrackerBannerFrame, highlightthickness = 0, font = ("Steelworks Vintage Demo", 50, "bold"), text = "Combat Tracker", fg = "#191919", bg = "white", relief = FLAT, width = 20, height = 1)
    combatTrackerBannerFrame.place(relx = 0.5, rely = 0.07, anchor= CENTER) 
    combatTrackerBannerLabel.pack(pady = (0,.5))

    """ 
    enemiesOut=StringVar(combatTrackerWindow)
    enemiesOut.set("Output")
    
    enemiesList = ['Vampire', 
           'Werewolf \n Sp: 1 Ar: 2, HP: 25', 
           'Zombie', 
           'Dragon', 
           'Giant Spider', 
           'Goblin', 
           'Orc', 
           'Skeleton Warrior \n Sp: 1 Ar: 2, HP: 25']
    options = StringVar(combatTrackerWindow)
    options.set("Enemies")
    with open('save\enemies.txt', 'w') as f:
        for enemy in enemiesList:
            f.write("%s\n" % enemy)
    
    enemiesMenu = OptionMenu(combatTrackerWindow, options, *enemiesList)
    enemiesMenu.configure(font = ("Trajan Pro", 80, "bold"), fg = "white", bg = "#191919")
    menu = (combatTrackerWindow.nametowidget(enemiesMenu.menuname))
    menu.configure(font = ("Trajan Pro", 40, "bold"), fg = "white", bg = "#191919")   
    enemiesMenu.place(relx = 0, rely = 0.60) """

#================ See comments on heroSheet. All of this does the same thing as over there.     
    def updateHeroPassive():
        def onSubmit():
            if entry.get():
                heroPassiveText.set(entry.get())
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Passive:"):
                        lines[i] = "Passive: " + entry.get() + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                heroPassiveText.set("Passive")
            heroPassive.destroy()
        def validateInput(entryText):
            return all(char.isalpha() or char.isspace() for char in entryText) and len(entryText) <= 30

        heroPassive = Toplevel()
        heroPassive.title("Passive")
        heroPassive.geometry("250x50")
        validateCmd = heroPassive.register(validateInput)
        entry = Entry(heroPassive, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(heroPassive, text="Submit", command=onSubmit)
        submit.pack()
        
    heroPassiveText = StringVar()
    heroPassiveText.set("Passive")
    heroPassiveFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    heroPassiveButton = Button(heroPassiveFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = heroPassiveText, command = updateHeroPassive, relief = FLAT, width = 10, height = 3, wraplength = 250)
    heroPassiveFrame.place(relx = 0.63, rely = 0.23)
    heroPassiveButton.pack(pady=(0,.5))
    
    def updateHeroSpeed():
        def onSubmit():
            if entry.get():
                heroSpeedText.set(entry.get() + " sp")
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Speed:"):
                        lines[i] = "Speed: " + entry.get() + " sp" + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                heroSpeedText.set("Speed")
            heroSpeed.destroy()
        def validateInput(entryText):
            return all(char.isdigit() for char in entryText) and len(entryText) <= 3

        heroSpeed = Toplevel()
        heroSpeed.title("Speed")
        heroSpeed.geometry("250x50")
        validateCmd = heroSpeed.register(validateInput)
        entry = Entry(heroSpeed, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(heroSpeed, text="Submit", command=onSubmit)
        submit.pack()
        
    heroSpeedText = StringVar()
    heroSpeedText.set("Speed")
    heroSpeedFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    heroSpeedButton = Button(heroSpeedFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = heroSpeedText, command = updateHeroSpeed, relief = FLAT, width = 10, height = 3, wraplength = 250)
    heroSpeedFrame.place(relx = 0.7355, rely = 0.23)
    heroSpeedButton.pack(pady=(0,.5))
    
    def updateHeroBrawn():
        def onSubmit():
            if entry.get():
                heroBrawnText.set(entry.get() + " br")
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Brawn:"):
                        lines[i] = "Brawn: " + entry.get() + " br" + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                heroBrawnText.set("Brawn")
            heroBrawn.destroy()
        def validateInput(entryText):
            return all(char.isdigit() for char in entryText) and len(entryText) <= 3
        heroBrawn = Toplevel()
        heroBrawn.title("Brawn")
        heroBrawn.geometry("250x50")
        validateCmd = heroBrawn.register(validateInput)
        entry = Entry(heroBrawn, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(heroBrawn, text="Submit", command=onSubmit)
        submit.pack()
        
    heroBrawnText = StringVar()
    heroBrawnText.set("Brawn")
    heroBrawnFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    heroBrawnButton = Button(heroBrawnFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = heroBrawnText, command = updateHeroBrawn, relief = FLAT, width = 10, height = 3, wraplength = 250)
    heroBrawnFrame.place(relx = 0.7355, rely = 0.35)
    heroBrawnButton.pack(pady=(0,.5))
    
    def updateHeroMagic():
        def onSubmit():
            if entry.get():
                heroMagicText.set(entry.get() + " ma")
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Magic:"):
                        lines[i] = "Magic: " + entry.get() + " ma" + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                heroMagicText.set("Magic")
            heroMagic.destroy()
        def validateInput(entryText):
            return all(char.isdigit() for char in entryText) and len(entryText) <= 3
        heroMagic = Toplevel()
        heroMagic.title("Magic")
        heroMagic.geometry("250x50")
        validateCmd = heroMagic.register(validateInput)
        entry = Entry(heroMagic, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(heroMagic, text="Submit", command=onSubmit)
        submit.pack()
    
    heroMagicText = StringVar()
    heroMagicText.set("Magic")
    heroMagicFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    heroMagicButton = Button(heroMagicFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = heroMagicText, command = updateHeroMagic, relief = FLAT, width = 10, height = 3, wraplength = 250)
    heroMagicFrame.place(relx = 0.7355, rely = 0.47)
    heroMagicButton.pack(pady=(0,.5))
    
    def updateHeroArmor():
        def onSubmit():
            if entry.get():
                heroArmorText.set(entry.get()+ " ar")
                with open("save\combat.txt", "r") as f:   
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Armor:"):
                        lines[i] = "Armor: " + entry.get()+ " ar" + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                heroArmorText.set("Armor")
            heroArmor.destroy()
        def validateInput(entryText):
            return all(char.isdigit() for char in entryText) and len(entryText) <= 3
        heroArmor = Toplevel()
        heroArmor.title("Armor")
        heroArmor.geometry("250x50")
        validateCmd = heroArmor.register(validateInput)
        entry = Entry(heroArmor, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(heroArmor, text="Submit", command=onSubmit)
        submit.pack()
        
    heroArmorText = StringVar()
    heroArmorText.set("Armor")
    heroArmorFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    heroArmorButton = Button(heroArmorFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = heroArmorText, command = updateHeroArmor, relief = FLAT, width = 10, height = 3, wraplength = 250)
    heroArmorFrame.place(relx = 0.7355, rely = 0.59)
    heroArmorButton.pack(pady=(0,.5))
    
    def updateHeroHealth():
        def onSubmit():
            if entry.get():
                heroHealthText.set(entry.get()+ " hp")
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Health:"):
                        lines[i] = "Health: " + entry.get() + " hp" + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                heroHealthText.set("Health")
            heroHealth.destroy()
        def validateInput(entryText):
            return all(char.isdigit() for char in entryText) and len(entryText) <= 3
        heroHealth = Toplevel()
        heroHealth.title("Health")
        heroHealth.geometry("250x50")
        validateCmd = heroHealth.register(validateInput)
        entry = Entry(heroHealth, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(heroHealth, text="Submit", command=onSubmit)
        submit.pack()
        
    heroHealthText = StringVar()
    heroHealthText.set("Health")
    heroHealthFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    heroHealthButton = Button(heroHealthFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = heroHealthText, command = updateHeroHealth, relief = FLAT, width = 10, height = 3, wraplength = 250)
    heroHealthFrame.place(relx = 0.63, rely = 0.35)
    heroHealthButton.pack(pady=(0,.5))
    
    def updateOppPassiveOne():
        def onSubmit():
            if entry.get():
                oppPassiveOneText.set(entry.get())
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Passive1:"):
                        lines[i] = "Passive1: " + entry.get() + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                oppPassiveOneText.set("Passive 1")
            oppPassiveOne.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isalpha() or char.isspace() for char in entryText) and len(entryText) <= 10
        oppPassiveOne = Toplevel()
        oppPassiveOne.title("Passive 1")
        oppPassiveOne.geometry("250x50")
        validateCmd = oppPassiveOne.register(validateInput)
        entry = Entry(oppPassiveOne, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(oppPassiveOne, text="Submit", command=onSubmit)
        submit.pack()
        
    oppPassiveOneText = StringVar()
    oppPassiveOneText.set("Passive 1")
    oppPassiveOneFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    oppPassiveOneButton = Button(oppPassiveOneFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = oppPassiveOneText, command = updateOppPassiveOne, relief = FLAT, width = 10, height = 3, wraplength = 250)
    oppPassiveOneFrame.place(relx = 0.22, rely = 0.23)
    oppPassiveOneButton.pack(pady=(0,.5))
    
    def updateOppPassiveTwo():
        def onSubmit():
            if entry.get():
                oppPassiveTwoText.set(entry.get())
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Passive2:"):
                        lines[i] = "Passive2: " + entry.get() + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                oppPassiveTwoText.set("Passive 2")
            oppPassiveTwo.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isalpha() or char.isspace() for char in entryText) and len(entryText) <= 10
        oppPassiveTwo = Toplevel()
        oppPassiveTwo.title("Passive 2")
        oppPassiveTwo.geometry("250x50")
        validateCmd = oppPassiveTwo.register(validateInput)
        entry = Entry(oppPassiveTwo, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(oppPassiveTwo, text="Submit", command=onSubmit)
        submit.pack()
        
    oppPassiveTwoText = StringVar()
    oppPassiveTwoText.set("Passive 2")
    oppPassiveTwoFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    oppPassiveTwoButton = Button(oppPassiveTwoFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = oppPassiveTwoText, command = updateOppPassiveTwo, relief = FLAT, width = 10, height = 3, wraplength = 250)
    oppPassiveTwoFrame.place(relx = 0.32, rely = 0.23)
    oppPassiveTwoButton.pack(pady=(0,.5))

    def updateOppPassiveThree():
        def onSubmit():
            if entry.get():
                oppPassiveThreeText.set(entry.get())
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Passive3:"):
                        lines[i] = "Passive3: " + entry.get() + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                oppPassiveThreeText.set("Passive 3")
            oppPassiveThree.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isalpha() or char.isspace() for char in entryText) and len(entryText) <= 10
        oppPassiveThree = Toplevel()
        oppPassiveThree.title("Passive 3")
        oppPassiveThree.geometry("250x50")
        validateCmd = oppPassiveThree.register(validateInput)
        entry = Entry(oppPassiveThree, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(oppPassiveThree, text="Submit", command=onSubmit)
        submit.pack()
        
    oppPassiveThreeText = StringVar()
    oppPassiveThreeText.set("Passive 3")
    oppPassiveThreeFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    oppPassiveThreeButton = Button(oppPassiveThreeFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = oppPassiveThreeText, command = updateOppPassiveThree, relief = FLAT, width = 10, height = 3, wraplength = 250)
    oppPassiveThreeFrame.place(relx = 0.42, rely = 0.23)
    oppPassiveThreeButton.pack(pady=(0,.5))

    def updateOppPassiveFour():
        def onSubmit():
            if entry.get():
                oppPassiveFourText.set(entry.get())
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Passive4:"):
                        lines[i] = "Passive4: " + entry.get() + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                oppPassiveFourText.set("Passive 4")
            oppPassiveFour.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isalpha() or char.isspace() for char in entryText) and len(entryText) <= 10
        oppPassiveFour = Toplevel()
        oppPassiveFour.title("Passive 4")
        oppPassiveFour.geometry("250x50")
        validateCmd = oppPassiveFour.register(validateInput)
        entry = Entry(oppPassiveFour, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(oppPassiveFour, text="Submit", command=onSubmit)
        submit.pack()
        
    oppPassiveFourText = StringVar()
    oppPassiveFourText.set("Passive 4")
    oppPassiveFourFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    oppPassiveFourButton = Button(oppPassiveFourFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = oppPassiveFourText, command = updateOppPassiveFour, relief = FLAT, width = 10, height = 3, wraplength = 250)
    oppPassiveFourFrame.place(relx = 0.52, rely = 0.23)
    oppPassiveFourButton.pack(pady=(0,.5))
    
    
    def updateOppHealthOne():
        def onSubmit():
            if entry.get():
                oppHealthOneText.set(entry.get()+ " hp")
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Health1:"):
                        lines[i] = "Health1: " + entry.get() + " hp" + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                oppHealthOneText.set("Health 1")
            oppHealthOne.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isspace() for char in entryText) and len(entryText) <= 5
        
        oppHealthOne = Toplevel()
        oppHealthOne.title("Health 1")
        oppHealthOne.geometry("250x50")
        validateCmd = oppHealthOne.register(validateInput)
        entry = Entry(oppHealthOne, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(oppHealthOne, text="Submit", command=onSubmit)
        submit.pack()
        
    oppHealthOneText = StringVar()
    oppHealthOneText.set("Health 1")
    oppHealthOneFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    oppHealthOneButton = Button(oppHealthOneFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = oppHealthOneText, command = updateOppHealthOne, relief = FLAT, width = 10, height = 3, wraplength = 250)
    oppHealthOneFrame.place(relx = 0.22, rely = 0.35)
    oppHealthOneButton.pack(pady=(0,.5))
        
    def updateOppHealthTwo():
        def onSubmit():
            if entry.get():
                oppHealthTwoText.set(entry.get()+ " hp")
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Health2:"):
                        lines[i] = "Health2: " + entry.get() + " hp" + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                oppHealthTwoText.set("Health 2")
            oppHealthTwo.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isspace() for char in entryText) and len(entryText) <= 5
        
        oppHealthTwo = Toplevel()
        oppHealthTwo.title("Health 2")
        oppHealthTwo.geometry("250x50")
        validateCmd = oppHealthTwo.register(validateInput)
        entry = Entry(oppHealthTwo, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(oppHealthTwo, text="Submit", command=onSubmit)
        submit.pack()

    oppHealthTwoText = StringVar()
    oppHealthTwoText.set("Health 2")
    oppHealthTwoFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    oppHealthTwoButton = Button(oppHealthTwoFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = oppHealthTwoText, command = updateOppHealthTwo, relief = FLAT, width = 10, height = 3, wraplength = 250)
    oppHealthTwoFrame.place(relx = 0.32, rely = 0.35)
    oppHealthTwoButton.pack(pady=(0,.5))
    
    def updateOppHealthThree():
        def onSubmit():
            if entry.get():
                oppHealthThreeText.set(entry.get()+ " hp")
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Health3:"):
                        lines[i] = "Health3: " + entry.get()+ " hp" + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                oppHealthThreeText.set("Health 3")
            oppHealthThree.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isspace() for char in entryText) and len(entryText) <= 5
        
        oppHealthThree = Toplevel()
        oppHealthThree.title("Health 3")
        oppHealthThree.geometry("250x50")
        validateCmd = oppHealthThree.register(validateInput)
        entry = Entry(oppHealthThree, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(oppHealthThree, text="Submit", command=onSubmit)
        submit.pack()

    oppHealthThreeText = StringVar()
    oppHealthThreeText.set("Health 3")
    oppHealthThreeFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    oppHealthThreeButton = Button(oppHealthThreeFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = oppHealthThreeText, command = updateOppHealthThree, relief = FLAT, width = 10, height = 3, wraplength = 250)
    oppHealthThreeFrame.place(relx = 0.42, rely = 0.35)
    oppHealthThreeButton.pack(pady=(0,.5))
 
   
    def updateOppHealthFour():
        def onSubmit():
            if entry.get():
                oppHealthFourText.set(entry.get()+ " hp")
                with open("save\combat.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Health4:"):
                        lines[i] = "Health4: " + entry.get() + " hp" + "\n"
                        break
                with open("save\combat.txt", "w") as f:
                    f.writelines(lines)
            else:
                oppHealthFourText.set("Health 4")
            oppHealthFour.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isspace() for char in entryText) and len(entryText) <= 5
        
        oppHealthFour = Toplevel()
        oppHealthFour.title("Health 4")
        oppHealthFour.geometry("250x50")
        validateCmd = oppHealthFour.register(validateInput)
        entry = Entry(oppHealthFour, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(oppHealthFour, text="Submit", command=onSubmit)
        submit.pack()

    oppHealthFourText = StringVar()
    oppHealthFourText.set("Health 4")
    oppHealthFourFrame = Frame(combatTrackerWindow, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    oppHealthFourButton = Button(oppHealthFourFrame, highlightthickness = 0, font = ("Trajan Pro", 18, "bold"), fg = "white", bg = "#191919", textvariable = oppHealthFourText, command = updateOppHealthFour, relief = FLAT, width = 10, height = 3, wraplength = 250)
    oppHealthFourFrame.place(relx = 0.52, rely = 0.35)
    oppHealthFourButton.pack(pady=(0,.5))

#================== The follwing code saves the information in the nameText.set fields and read its from the file
#================== the information entered is loaded upon startup of the program. It "saves" your character       
    def loadData():
        with open("save\combat.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith("Health2:"):
                oppHealthTwoText.set(line.split(":")[1].strip())
            elif line.startswith("Health3:"):
                oppHealthThreeText.set(line.split(":")[1].strip())
            elif line.startswith("Health4:"):
                oppHealthFourText.set(line.split(":")[1].strip())
            elif line.startswith("Health1:"):
                oppHealthOneText.set(line.split(":")[1].strip())
            elif line.startswith("Passive1:"):
                oppPassiveOneText.set(line.split(":")[1].strip())
            elif line.startswith("Passive2:"):
                oppPassiveTwoText.set(line.split(":")[1].strip())
            elif line.startswith("Passive3:"):
                oppPassiveThreeText.set(line.split(":")[1].strip())
            elif line.startswith("Passive4:"):
                oppPassiveFourText.set(line.split(":")[1].strip())
            elif line.startswith("Speed:"):
                heroSpeedText.set(line.split(":")[1].strip())
            elif line.startswith("Brawn:"):
                heroBrawnText.set(line.split(":")[1].strip())
            elif line.startswith("Magic:"):
                heroMagicText.set(line.split(":")[1].strip())
            elif line.startswith("Armor:"):
                heroArmorText.set(line.split(":")[1].strip())
            elif line.startswith("Health:"):
                heroHealthText.set(line.split(":")[1].strip())
            
    loadData()
    
