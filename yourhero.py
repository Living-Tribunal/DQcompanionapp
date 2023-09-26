#================ imports needed libraries
from tkinter import *
from tkinter import font, Tk
from PIL import ImageTk, Image
import random
import Images
import combatTracker


#================ function used to call Combat Tracker  
def onCombatTracker():
    combatTracker.combatTrackerSheet()

def openYourHero():
    yourHero = Toplevel()
    yourHero.title("Your Hero")
    yourHero.iconbitmap("Images/sword.ico")
    yourHero.attributes('-fullscreen', True)

#================ Creating canvas for background for the Hero sheet window    
    yourHeroCanvas = Canvas(yourHero, highlightthickness=0, bd = 0)
    yourHeroCanvas.pack(expand = True, fill = BOTH)
    yourHeroCanvas.create_image(0,0, anchor = NW, image = Images.Images["heroSheet"])
    
    
#================ Button to kill the program on Hero sheet Window
    exitButton = Button(yourHero, image = Images.Images["backArrowImage"], highlightthickness = 0, bd = 0, command = yourHero.destroy)
    exitButton.pack()
#================ Adjusting the position of the exit button on Hero sheet window     
    exitButton.place(relx = 0.040, rely = 0.0, anchor = NE)

#================ Button to go to combat tracker on Hero sheet window
    combatFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    combatButton= Button(combatFrame, highlightthickness = 0, font = ("Rockwell Extra Bold", 18, "bold"), fg = "white", bg = "#191919", command = onCombatTracker, relief = FLAT, width=15,height=2, text=("Combat Tracker"))
    combatFrame.place(relx = 0.0, rely = 0.08) 
    combatButton.pack(pady=(0,.5))

#================ header for special abilites    
    specialAbilitesFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    specialAbilitesLabel = Label(specialAbilitesFrame, highlightthickness = 0, font = ("Steelworks Vintage Demo", 34, "bold"), text = "Special Abilities", fg = "#191919", bg = "white", relief = FLAT, width = 20, height = 2)
    specialAbilitesFrame.place(relx = 0.655, rely = 0.07) 
    specialAbilitesLabel.pack(pady = (0,.5))

#================ header for backpack  
    backpackFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    backpackLabel = Label(backpackFrame, highlightthickness = 0, font = ("Steelworks Vintage Demo", 30, "bold"), text = "Backpack", fg = "#191919", bg = "white", relief = FLAT, width = 20, height = 1)
    backpackFrame.place(relx = 0.375, rely = .77)
    backpackLabel.pack(pady = (0,.5))

#=============== this is the same for the buttons on the combat tracker too
#=============== the following function is the same down until line 896, so I'll only explain this first one
#=============== defined the function name
    def updateName():
#=============== function name for what happens when a button is clicked
        def onSubmit():
#=============== checks to see if entry as a value, if it does it sets the value of nameText to entry (so what you enter replaces the nameText on the button)            
            if entry.get():
                nameText.set(entry.get())
#=============== opens the file HeroFile in read mode
                with open("save\heroFile.txt", "r") as f:
#=============== reads through the lines                    
                    lines = f.readlines()
                for i, line in enumerate(lines):
#=============== reads through the file looking for "Name", if it starts with Name:, with the value from entry.                 
                    if line.startswith("Name:"):
                        lines[i] = "Name: " + entry.get() + "\n"
                        break
#=============== writest the information to the file
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
#=============== if entry it emptpy, the buttons name is returtned to nameText, in this case its Name
                nameText.set("Name")
            name.destroy()
#=============== creates a new window for the submit button
        name = Toplevel()
#=============== window name, resoultion, and with an entry box        
        name.title("Name")
        name.geometry("200x50")
        entry = Entry(name)
#=============== packs entry to parent       
        entry.pack()
#=============== creates a submit button        
        submit = Button(name, text="Submit", command=onSubmit)
#=============== packs submit to parent       
        submit.pack()

#=============== the following is the atrributes, location, and name of this specific button. This is the same for each and every button. Just with different attributes 
#=============== and locations
    nameText = StringVar()
    nameText.set("Name")
    nameFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    nameButton = Button(nameFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = nameText, command = updateName, relief = FLAT, width=30,height=1)
    nameFrame.place(relx = 0.15, rely = 0.0) 
    nameButton.pack(pady=(0,.5))
    
    
    def updateCareer():
        def onSubmit():
            if entry.get():
                careerText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Career:"):
                        lines[i] = "Career: " + entry.get() + "\n"
                    break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                careerText.set("Career")
            career.destroy()
#================= Inputvaldation
        def validateInput(entryText):
#================= Checks to see if my inputs are letters or spaces in the entryText field. Also sets the limit of characters allowed in the entry field.            
            return all(char.isalpha() or char.isspace() for char in entryText) and len(entryText) <= 20

        career = Toplevel()
        career.title("Career")
        career.geometry("250x50")
        validateCmd = career.register(validateInput)
        entry = Entry(career, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(career, text="Submit", command=onSubmit)
        submit.pack()

    careerText = StringVar()
    careerText.set("Career")
    careerFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    careerButton = Button(careerFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = careerText, command = updateCareer, relief = FLAT, width = 30, height = 1)
    careerFrame.place(relx = 0.47, rely = 0.0) 
    careerButton.pack(pady = (0,.5))
    
    def updatePath():
        def onSubmit():
            if entry.get():
                pathText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Path:"):
                        lines[i] = "Path: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                pathText.set("Path")
            path.destroy()

        path = Toplevel()
        path.title("Path")
        path.geometry("250x50")
        entry = Entry(path)
        entry.pack()
        submit = Button(path, text="Submit", command=onSubmit)
        submit.pack()
        
    pathText = StringVar()
    pathText.set("Path")
    pathFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    pathButton = Button(pathFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = pathText, command = updatePath, relief = FLAT, width = 20, height = 1)
    pathFrame.place(relx = 0.78, rely = 0.0) 
    pathButton.pack(pady = (0,.5))
    
    def updateCloak():
        def onSubmit():
            if entry.get():
                cloakText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Cloak:"):
                        lines[i] = "Cloak: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                cloakText.set("Cloak")
            cloak.destroy()
        cloak = Toplevel()
        cloak.title("Cloak")
        cloak.geometry("250x50")
        entry = Entry(cloak)
        entry.pack()
        submit = Button(cloak, text="Submit", command=onSubmit)
        submit.pack()
        
    cloakText = StringVar()
    cloakText.set("Cloak")
    cloakFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    cloakButton = Button(cloakFrame, highlightthickness = 0, font = ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = cloakText, command = updateCloak, relief = FLAT, width = 10, height = 5, wraplength=150)
    cloakFrame.place(relx = 0.15, rely = 0.08)
    cloakButton.pack(pady = (0,.5))
    
    def updateHead():
        def onSubmit():
            if entry.get():
                headText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Head:"):
                        lines[i] = "Head: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                headText.set("Head")
            head.destroy()
        head = Toplevel()
        head.title("Head")
        head.geometry("250x50")
        entry = Entry(head)
        entry.pack()
        submit = Button(head, text="Submit", command=onSubmit)
        submit.pack()
        
    headText = StringVar()
    headText.set("Head")
    headFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    headButton = Button(headFrame, highlightthickness = 0, font = ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = headText, command = updateHead, relief = FLAT, width = 10, height = 5, wraplength=150)
    headFrame.place(relx = 0.26, rely = 0.08)
    headButton.pack(pady = (0,.5))
    
    def updateGloves():
        def onSubmit():
            if entry.get():
                glovesText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Gloves:"):
                        lines[i] = "Gloves: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                glovesText.set("Gloves")
            gloves.destroy()
        gloves = Toplevel()
        gloves.title("Gloves")
        gloves.geometry("250x50")
        entry = Entry(gloves)
        entry.pack()
        submit = Button(gloves, text="Submit", command=onSubmit)
        submit.pack()
        
    glovesText = StringVar()
    glovesText.set("Gloves")
    glovesFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    glovesButton = Button(glovesFrame, highlightthickness = 0, font = ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = glovesText, command = updateGloves, relief = FLAT, width = 10, height = 5, wraplength = 150)
    glovesFrame.place(relx = 0.37, rely = 0.08)
    glovesButton.pack(pady = (0,.5))
    
    def updateMainHand():
        def onSubmit():
            if entry.get():
                mainHandText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("MainHand:"):
                        lines[i] = "MainHand: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                mainHandText.set("Main Hand")
            mainHand.destroy()
        mainHand = Toplevel()
        mainHand.title("Main Hand")
        mainHand.geometry("250x50")
        entry = Entry(mainHand)
        entry.pack()
        submit = Button(mainHand, text = "Submit", command = onSubmit)
        submit.pack()
    
    mainHandText = StringVar()
    mainHandText.set("Main Hand")
    mainHandFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)
    mainHandButton = Button(mainHandFrame, highlightthickness = 0, font= ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = mainHandText, command = updateMainHand, relief = FLAT, width = 10, height = 5, wraplength = 250)
    mainHandFrame.place(relx = 0.15, rely = .27)
    mainHandButton.pack(pady = (0,.5))
        
    def updateChest():
        def onSubmit():
            if entry.get():
                chestText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Chest:"):
                        lines[i] = "Chest: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                chestText.set("Chest")
            chest.destroy()
        chest = Toplevel()
        chest.title("Chest")
        chest.geometry("250x50")
        entry = Entry(chest)
        entry.pack()
        submit = Button(chest, text = "Submit", command = onSubmit)
        submit.pack()
    
    chestText = StringVar()
    chestText.set("Chest")
    chestFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT) 
    chestButton = Button(chestFrame, highlightthickness = 0, font= ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = chestText, command = updateChest, relief = FLAT, width = 10, height = 5, wraplength = 150)  
    chestFrame.place(relx = .26, rely = .27)
    chestButton.pack(pady = (0,.5))
    
    def updateLeftHand():
        def onSubmit():
            if entry.get():
                leftHandText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("LeftHand:"):
                        lines[i] = "LeftHand: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                leftHandText.set("Left Hand")
            leftHand.destroy()
        leftHand = Toplevel()
        leftHand.title("Left Hand")
        leftHand.geometry("250x50")
        entry = Entry(leftHand, bg= "white", fg = "#191919")
        entry.pack()
        submit = Button(leftHand, text = "Submit", command = onSubmit)
        submit.pack()
    
    leftHandText = StringVar()
    leftHandText.set("Left Hand")
    leftHandFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)
    leftHandButton = Button(leftHandFrame, highlightthickness = 0, font= ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = leftHandText, command = updateLeftHand, relief = FLAT, width = 10, height = 5, wraplength = 150)
    leftHandFrame.place(relx = 0.37, rely = .27)
    leftHandButton.pack(pady = (0,.5))
    
    def updateTalisman():
        def onSubmit():
            if entry.get():
                talismanText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Talisman:"):
                        lines[i] = "Talisman: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                talismanText.set("Talisman")
            talisman.destroy()
        talisman = Toplevel()
        talisman.title("Talisman")
        talisman.geometry("250x50")
        entry = Entry(talisman, bg = "white", fg = "#191919")
        entry.pack()
        submit = Button(talisman, text = "Submit", command = onSubmit)
        submit.pack()
    
    talismanText = StringVar()
    talismanText.set("Talisman")
    talismanFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)
    talismanButton = Button(talismanFrame, highlightthickness = 0, font= ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = talismanText, command = updateTalisman, relief = FLAT, width = 10, height = 5, wraplength = 150)
    talismanFrame.place(relx = 0.15, rely = .46)
    talismanButton.pack(pady = (0,.5))
    
    def updateFeet():
        def onSubmit():
            if entry.get():
                feetText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Feet:"):
                        lines[i] = "Feet: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                feetText.set("Feet")
            feet.destroy()
        feet = Toplevel()
        feet.title("Feet")
        feet.geometry("250x50")
        entry = Entry(feet, bg = "white", fg = "#191919")
        entry.pack()
        sumbit = Button(feet, text = "Submit", command = onSubmit)
        sumbit.pack()
    
    feetText = StringVar()
    feetText.set("Feet")
    feetFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)    
    feetButton = Button(feetFrame, highlightthickness = 0, font= ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = feetText, command = updateFeet, relief = FLAT, width = 10, height = 5, wraplength = 150)   
    feetFrame.place(relx = 0.26, rely = .46)
    feetButton.pack(pady = (0,.5))  
    
    def updateMoney():
        def onSubmit():
            if entry.get():
                moneyText.set(entry.get() + " cr")
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Crowns:"):
                        lines[i] = "Crowns: " + entry.get() + " cr" + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                moneyText.set("Money Pouch")
            money.destroy()
        money = Toplevel()
        money.title("Money Pouch")
        money.geometry("250x50")
        entry = Entry(money, bg = "white", fg = "#191919")
        entry.pack()
        sumbit = Button(money, text = "Submit", command = onSubmit)
        sumbit.pack()
    
    moneyText = StringVar()
    moneyText.set("Money Pouch")
    moneyFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)    
    moneyButton = Button(moneyFrame, highlightthickness = 0, font= ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = moneyText, command = updateMoney, relief = FLAT, width = 10, height = 5, wraplength = 100)   
    moneyFrame.place(relx = 0.37, rely = .46)
    moneyButton.pack(pady = (0,.5))  
        
    def updateSpeed():
        def onSubmit():
            if entry.get():
                speedText.set(entry.get()+ " sp")
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Speed:"):
                        lines[i] = "Speed: " + entry.get() + " sp" + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                speedText.set("Speed")
            speed.destroy()
            
        def validateInput(entryText):
            return all(char.isdigit() or char.isspace() for char in entryText) and len(entryText) <= 2
            
        speed = Toplevel()
        speed.title("Speed")
        speed.geometry("250x50")
        validateCmd = speed.register(validateInput)
        entry = Entry(speed, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(speed, text="Submit", command=onSubmit)
        submit.pack()
    
    speedText = StringVar()
    speedText.set("Speed")
    speedFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    speedButton = Button(speedFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = speedText, command = updateSpeed, relief = FLAT, width = 8, height = 4)
    speedFrame.place(relx = 0.05, rely = 0.20)
    speedButton.pack(pady=(0,.5))
    
    def updateBrawn():
        def onSubmit():
            if entry.get():
                brawnText.set(entry.get()+ " br")
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Brawn:"):
                        lines[i] = "Brawn: " + entry.get() + " br" + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                brawnText.set("Brawn")
            brawn.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isspace() for char in entryText) and len(entryText) <= 2
        
        brawn = Toplevel()
        brawn.title("Brawn")
        brawn.geometry("250x50")
        validateCmd = brawn.register(validateInput)
        entry = Entry(brawn, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(brawn, text="Submit", command=onSubmit)
        submit.pack()
    
    brawnText = StringVar()
    brawnText.set("Brawn")
    brawnFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    brawnButton = Button(brawnFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = brawnText, command = updateBrawn, relief = FLAT, width = 8, height = 4)
    brawnFrame.place(relx = 0.05, rely = 0.37)
    brawnButton.pack(pady=(0,.5))
    
    def updateMagic():
        def onSubmit():
            if entry.get():
                magicText.set(entry.get()+ " ma")
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Magic:"):
                        lines[i] = "Magic: " + entry.get() + " ma" + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                magicText.set("Magic")
            magic.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isspace() for char in entryText) and len(entryText) <= 2
        
        magic = Toplevel()
        magic.title("Magic")
        magic.geometry("250x50")
        validateCmd = magic.register(validateInput)
        entry = Entry(magic, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(magic, text = "Submit", command = onSubmit)
        submit.pack()
    
    magicText = StringVar()
    magicText.set("Magic")
    magicFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    magicButton = Button(magicFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = magicText, command = updateMagic, relief = FLAT, width = 8, height = 4)
    magicFrame.place(relx = 0.05, rely = 0.54)
    magicButton.pack(pady=(0,.5))
    
    def updateArmor():
        def onSubmit():
            if entry.get():
                armorText.set(entry.get()+ " ar")
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Armor:"):
                        lines[i] = "Armor: " + entry.get() + " ar" + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                armorText.set("Armor")
            armor.destroy()
        def validateInput(entryText):
            return all(char.isdigit() or char.isspace() for char in entryText) and len(entryText) <= 2
        
        armor = Toplevel()
        armor.title("Armor")
        armor.geometry("250x50")
        validateCmd = armor.register(validateInput)
        entry = Entry(armor, validate="key", validatecommand=(validateCmd, '%P'))
        entry.pack()
        submit = Button(armor, text = "Submit", command = onSubmit)
        submit.pack()
    
    armorText = StringVar()
    armorText.set("Armor")
    armorFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    armorButton = Button(armorFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = armorText, command = updateArmor, relief = FLAT, width = 8, height = 4)
    armorFrame.place(relx = 0.05, rely = 0.71)
    armorButton.pack(pady=(0,.5))
    
    def updateHealth():
        def onSubmit():
            if entry.get():
                healthText.set(entry.get()+ " hp")
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Health:"):
                        lines[i] = "Health: " + entry.get() + " hp" + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                healthText.set("Health")
            health.destroy()
        health = Toplevel()
        health.title("Health")
        health.geometry("250x50")
        entry = Entry(health)
        entry.pack()
        submit = Button(health, text = "Submit", command = onSubmit)
        submit.pack()
    
    healthText = StringVar()
    healthText.set("Health")
    healthFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    healthButton = Button(healthFrame, highlightthickness = 0, font = ("Trajan Pro", 21, "bold"), fg = "white", bg = "#191919", textvariable = healthText, command = updateHealth, relief = FLAT, width = 19, height = 4)
    healthFrame.place(relx = 0.15, rely = 0.65)
    healthButton.pack(pady =(0,.5))
    
    def updateNecklace():
        def onSubmit():
            if entry.get():
                necklaceText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Necklace:"):
                        lines[i] = "Necklace: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                necklaceText.set("Necklace")
            necklace.destroy()
        necklace = Toplevel()
        necklace.title("Necklace")
        necklace.geometry("250x50")
        entry = Entry(necklace, bg = "white", fg = "#191919")
        entry.pack()
        sumbit = Button(necklace, text = "Submit", command = onSubmit)
        sumbit.pack()
    
    necklaceText = StringVar()
    necklaceText.set("Necklace")
    necklaceFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)    
    necklaceButton = Button(necklaceFrame, highlightthickness = 0, font= ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = necklaceText, command = updateNecklace, relief = FLAT, width = 10,height = 4, wraplength = 200) 
    necklaceFrame.place(relx = 0.54, rely = .19)
    necklaceButton.pack(pady = (0,.5))
    
    def updateLeftRing():
        def onSubmit():
            if entry.get():
                ringLeftText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("LeftRing:"):
                        lines[i] = "LeftRing: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                ringLeftText.set("Left Ring")
            ringLeft.destroy()
        ringLeft = Toplevel()
        ringLeft.title("Left ring")
        ringLeft.geometry("250x50")
        entry = Entry(ringLeft, bg = "white", fg = "#191919")
        entry.pack()
        sumbit = Button(ringLeft, text = "Submit", command = onSubmit)
        sumbit.pack()
    
    ringLeftText = StringVar()
    ringLeftText.set("Left Ring")
    ringLeftFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)    
    ringLeftButton = Button(ringLeftFrame, highlightthickness = 0, font= ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = ringLeftText, command = updateLeftRing, relief = FLAT, width = 10,height = 4, wraplength = 200) 
    ringLeftFrame.place(relx = 0.54, rely = .39)
    ringLeftButton.pack(pady = (0,.5))
    
    def updateRightRing():
        def onSubmit():
            if entry.get():
                ringRightText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("RightRing:"):
                        lines[i] = "RightRing: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                ringRightText.set("Right Ring")
            ringRight.destroy()
        ringRight = Toplevel()
        ringRight.title("Right ring")
        ringRight.geometry("250x50")
        entry = Entry(ringRight, bg = "white", fg = "#191919")
        entry.pack()
        sumbit = Button(ringRight, text = "Submit", command = onSubmit)
        sumbit.pack()
    
    ringRightText = StringVar()
    ringRightText.set("Right Ring")
    ringRightFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)    
    ringRightButton = Button(ringRightFrame, highlightthickness = 0, font= ("Trajan Pro", 19, "bold"), fg = "white", bg = "#191919", textvariable = ringRightText, command = updateRightRing, relief = FLAT, width = 10,height = 4, wraplength = 200) 
    ringRightFrame.place(relx = 0.54, rely = .59)
    ringRightButton.pack(pady = (0,.5))
    
    def updateAbilitySpeed():
        def onSubmit():
            if entry.get():
                abilitySpeedText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("ABSpeed:"):
                        lines[i] = "ABSpeed: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                abilitySpeedText.set("Speed")
            abilitySpeed.destroy()
        abilitySpeed = Toplevel()
        abilitySpeed.title("Speed")
        abilitySpeed.geometry("250x50")
        entry = Entry(abilitySpeed, bg = "white", fg = "#191919")
        entry.pack()
        sumbit = Button(abilitySpeed, text = "Submit", command = onSubmit)
        sumbit.pack()
    
    abilitySpeedText = StringVar()
    abilitySpeedText.set("Speed")
    abilitySpeedFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)
    abilitySpeedButton = Button(abilitySpeedFrame, highlightthickness = 0, font= ("Trajan Pro", 30, "bold"), fg = "white", bg = "#191919", textvariable = abilitySpeedText, command = updateAbilitySpeed, relief = FLAT, width = 20, height = 3, wraplength = 500)
    abilitySpeedFrame.place(relx = 0.65, rely = .19)
    abilitySpeedButton.pack(pady = (0,.5))
    
    def updateAbilityCombat():
        def onSubmit():
            if entry.get():
                abilityCombatText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Combat:"):
                        lines[i] = "Combat: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                abilityCombatText.set("Combat")
            abilityCombat.destroy()
        abilityCombat = Toplevel()
        abilityCombat.title("Combat")
        abilityCombat.geometry("250x50")
        entry = Entry(abilityCombat, bg = "white", fg = "#191919")
        entry.pack()
        sumbit = Button(abilityCombat, text = "Submit", command = onSubmit)
        sumbit.pack()
    
    abilityCombatText = StringVar()
    abilityCombatText.set("Combat")
    abilityCombatFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)
    abilityCombatButton = Button(abilityCombatFrame, highlightthickness = 0, font= ("Trajan Pro", 30, "bold"), fg = "white", bg = "#191919", textvariable = abilityCombatText, command = updateAbilityCombat, relief = FLAT, width = 20, height = 3, wraplength = 500)
    abilityCombatFrame.place(relx = 0.65, rely = .39)
    abilityCombatButton.pack(pady = (0,.5))
    
    def updateAbilityPassive():
        def onSubmit():
            if entry.get():
                abilityPassiveText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Passive:"):
                        lines[i] = "Passive: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                abilityPassiveText.set("Passive")
            abilityPassive.destroy()
        abilityPassive = Toplevel()
        abilityPassive.title("Passive")
        abilityPassive.geometry("250x50")
        entry = Entry(abilityPassive, bg = "white", fg = "#191919")
        entry.pack()
        sumbit = Button(abilityPassive, text = "Submit", command = onSubmit)
        sumbit.pack()
    
    abilityPassiveText = StringVar()
    abilityPassiveText.set("Passive")
    abilityPassiveFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)
    abilityPassiveButton = Button(abilityPassiveFrame, highlightthickness = 0, font= ("Trajan Pro", 30, "bold"), fg = "white", bg = "#191919", textvariable = abilityPassiveText, command = updateAbilityPassive, relief = FLAT, width = 20, height = 3, wraplength = 500)
    abilityPassiveFrame.place(relx = 0.65, rely = .59)
    abilityPassiveButton.pack(pady = (0,.5))
    
    def updateAbilityModifier():
        def onSubmit():
            if entry.get():
                abilityModifierText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("Modifier:"):
                        lines[i] = "Modifier: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                abilityModifierText.set("Modifier")
            abilityModifier.destroy()
        abilityModifier = Toplevel()
        abilityModifier.title("Modifier")
        abilityModifier.geometry("250x50")
        entry = Entry(abilityModifier, bg = "white", fg = "#191919")
        entry.pack()
        sumbit = Button(abilityModifier, text = "Submit", command = onSubmit)
        sumbit.pack()
    
    abilityModifierText = StringVar()
    abilityModifierText.set("Modifier")
    abilityModifierFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background = "white", relief = FLAT)
    abilityModifierButton = Button(abilityModifierFrame, highlightthickness = 0, font= ("Trajan Pro", 30, "bold"), fg = "white", bg = "#191919", textvariable = abilityModifierText, command = updateAbilityModifier, relief = FLAT, width = 20, height = 3, wraplength = 500)
    abilityModifierFrame.place(relx = 0.65, rely = .79)
    abilityModifierButton.pack(pady = (0,.5))
    
    def updateBackpackOne():
        def onSubmit():
            if entry.get():
                backpackOneText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("BackpackOne:"):
                        lines[i] = "BackpackOne: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                backpackOneText.set("Slot 1")
            backpackOne.destroy()
        backpackOne = Toplevel()
        backpackOne.title("Slot 1")
        backpackOne.geometry("250x50")
        entry = Entry(backpackOne)
        entry.pack()
        submit = Button(backpackOne, text="Submit", command = onSubmit)
        submit.pack()
    
    backpackOneText = StringVar()
    backpackOneText.set("Slot 1")
    backpackOneFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    backpackOneButton = Button(backpackOneFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = backpackOneText, command = updateBackpackOne, relief = FLAT, width = 8, height = 4, wraplength = 200)
    backpackOneFrame.place(relx = 0.190, rely = 0.83)
    backpackOneButton.pack(pady=(0,.5))

    def updateBackpackTwo():
        def onSubmit():
            if entry.get():
                backpackTwoText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("BackpackTwo:"):
                        lines[i] = "BackpackTwo: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                backpackTwoText.set("Slot 2")
            backpackTwo.destroy()
        backpackTwo = Toplevel()
        backpackTwo.title("Slot 2")
        backpackTwo.geometry("250x50")
        entry = Entry(backpackTwo)
        entry.pack()
        submit = Button(backpackTwo, text="Submit", command=onSubmit)
        submit.pack()
    
    backpackTwoText = StringVar()
    backpackTwoText.set("Slot 2")
    backpackTwoFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    backpackTwoButton = Button(backpackTwoFrame, highlightthickness = 0, font = ("Trajan Pro", 20 , "bold"), fg = "white", bg = "#191919", textvariable = backpackTwoText, command = updateBackpackTwo, relief = FLAT, width = 8, height = 4, wraplength = 200)
    backpackTwoFrame.place(relx = 0.280, rely = 0.83)
    backpackTwoButton.pack(pady=(0,.5))

    def updateBackpackThree():
        def onSubmit():
            if entry.get():
                backpackThreeText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("BackpackThree:"):
                        lines[i] = "BackpackThree: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                backpackThreeText.set("Slot 3")
            backpackThree.destroy()
        backpackThree = Toplevel()
        backpackThree.title("Slot 3")
        backpackThree.geometry("250x50")
        entry = Entry(backpackThree)
        entry.pack()
        submit = Button(backpackThree, text="Submit", command=onSubmit)
        submit.pack()       
    
    backpackThreeText = StringVar()
    backpackThreeText.set("Slot 3")
    backpackThreeFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    backpackThreeButton = Button(backpackThreeFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = backpackThreeText, command = updateBackpackThree, relief = FLAT, width = 8, height = 4, wraplength = 200)
    backpackThreeFrame.place(relx = 0.371, rely = 0.83)
    backpackThreeButton.pack(pady=(0,.5))
    
    def updateBackpackFour():
        def onSubmit():
            if entry.get():
                backpackFourText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("BackpackFour:"):
                        lines[i] = "BackpackFour: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                backpackFourText.set("Slot 4")
            backpackFour.destroy()
        backpackFour = Toplevel()
        backpackFour.title("Slot 4")
        backpackFour.geometry("250x50")
        entry = Entry(backpackFour)
        entry.pack()
        submit = Button(backpackFour, text="Submit", command=onSubmit)
        submit.pack()        
    
    backpackFourText = StringVar()
    backpackFourText.set("Slot 4")
    backpackFourFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    backpackFourButton = Button(backpackFourFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = backpackFourText, command = updateBackpackFour, relief = FLAT, width = 8, height = 4, wraplength = 200)
    backpackFourFrame.place(relx = 0.461, rely = 0.83)
    backpackFourButton.pack(pady=(0,.5))
    
    def updateBackpackFive():
        def onSubmit():
            if entry.get():
                backpackFiveText.set(entry.get())
                with open("save\heroFile.txt", "r") as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    if line.startswith("BackpackFive:"):
                        lines[i] = "BackpackFive: " + entry.get() + "\n"
                        break
                with open("save\heroFile.txt", "w") as f:
                    f.writelines(lines)
            else:
                backpackFiveText.set("Slot 5")
            backpackFive.destroy()
        backpackFive = Toplevel()
        backpackFive.title("Slot 5")
        backpackFive.geometry("250x50")
        entry = Entry(backpackFive)
        entry.pack()
        submit = Button(backpackFive, text="Submit", command=onSubmit)
        submit.pack()
    
    backpackFiveText = StringVar()
    backpackFiveText.set("Slot 5")
    backpackFiveFrame = Frame(yourHero, highlightthickness = 0, bd = 3, background= "white", relief = FLAT)
    backpackFiveButton = Button(backpackFiveFrame, highlightthickness = 0, font = ("Trajan Pro", 20, "bold"), fg = "white", bg = "#191919", textvariable = backpackFiveText, command = updateBackpackFive, relief = FLAT, width = 8, height = 4, wraplength = 200)
    backpackFiveFrame.place(relx = 0.551, rely = 0.83)
    backpackFiveButton.pack(pady=(0,.5))
    
#================== This is also the same on the combat tracker window
#================== The follwing code saves the information in the nameText.set fields and read its from the file
#================== the information entered is loaded upon startup of the program. It "saves" your character    
    def load_data():
        with open("save\heroFile.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            if line.startswith("Name:"):
                nameText.set(line.split(":")[1].strip())
            elif line.startswith("Career:"):
                careerText.set(line.split(":")[1].strip())
            elif line.startswith("Path:"):
                pathText.set(line.split(":")[1].strip())
            elif line.startswith("Cloak:"):
                cloakText.set(line.split(":")[1].strip())
            elif line.startswith("Head:"):
                headText.set(line.split(":")[1].strip())
            elif line.startswith("Gloves:"):
                glovesText.set(line.split(":")[1].strip())
            elif line.startswith("MainHand:"):
                mainHandText.set(line.split(":")[1].strip())
            elif line.startswith("Chest:"):
                chestText.set(line.split(":")[1].strip())
            elif line.startswith("LeftHand:"):
                leftHandText.set(line.split(":")[1].strip())
            elif line.startswith("Talisman:"):
                talismanText.set(line.split(":")[1].strip())
            elif line.startswith("Feet:"):
                feetText.set(line.split(":")[1].strip())
            elif line.startswith("Crowns:"):
                moneyText.set(line.split(":")[1].strip())
            elif line.startswith("Speed:"):
                speedText.set(line.split(":")[1].strip())
            elif line.startswith("Brawn:"):
                brawnText.set(line.split(":")[1].strip())
            elif line.startswith("Magic:"):
                magicText.set(line.split(":")[1].strip())
            elif line.startswith("Armor:"):
                armorText.set(line.split(":")[1].strip())
            elif line.startswith("Health:"):
                healthText.set(line.split(":")[1].strip())
            elif line.startswith("Necklace:"):
                necklaceText.set(line.split(":")[1].strip())
            elif line.startswith("LeftRing:"):
                ringLeftText.set(line.split(":")[1].strip())
            elif line.startswith("RightRing:"):
                ringRightText.set(line.split(":")[1].strip())
            elif line.startswith("ABSpeed:"):
                abilitySpeedText.set(line.split(":")[1].strip())
            elif line.startswith("Combat:"):
                abilityCombatText.set(line.split(":")[1].strip())
            elif line.startswith("Passive:"):
                abilityPassiveText.set(line.split(":")[1].strip())
            elif line.startswith("Modifier:"):
                abilityModifierText.set(line.split(":")[1].strip())
            elif line.startswith("BackpackOne:"):
                backpackOneText.set(line.split(":")[1].strip())
            elif line.startswith("BackpackTwo:"):
                backpackTwoText.set(line.split(":")[1].strip())
            elif line.startswith("BackpackThree:"):
                backpackThreeText.set(line.split(":")[1].strip())
            elif line.startswith("BackpackFour:"):
                backpackFourText.set(line.split(":")[1].strip())
            elif line.startswith("BackpackFive:"):
                backpackFiveText.set(line.split(":")[1].strip())
            
    load_data()