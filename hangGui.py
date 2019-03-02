from tkinter import *
from tkinter import ttk
from randomwordgenerator import randomwordgenerator
import random



def randomWord():
    try:
        randNum = random.randrange(0, 20)
        num_words = 20
        wordList = randomwordgenerator.generate_random_words(n = num_words)
        return wordList[randNum]
    except UnicodeEncodeError:
        backupList = ['test', 'bounce', 'child', 'golf', 'whim']
        randNum = random.randrange(0, (len(backupList)))
        return backupList[randNum]

#<<<-----------------------New function development-------------------->>>
#Setters
def updateGallows(img): # Main imagery
    pass

def updateWrongGeusses(letter):
    word2 = wrongGeussesVar.get()
    newWord = (word2 + letter)
    wrongGeussesVar.set(newWord)

def updateAttempts():            #displaying but not updating
    attempts = int(failedAttempts.get())
    attempts -= 1
    failedAttempts.set(str(attempts))


def initHiddenWordList(word):#for gui
    hidden = ''
    for x in word:
        hidden += '- '
    hiddenWordList.set(hidden)

def updateHiddenWordList2(letter):#for gui
    hiddenList = hiddenWordList.get()
    word2 = word.get()
    hidden = ''
    count = 0
    for x in word2:
        if letter == x:
            hidden += (letter + ' ')
        else:
            hidden += '- '
        count += 1
    hiddenWordList.set(hidden)


def initHiddenWordListList(word):#for processing
    hidden = []
    for x in word:
        hidden.append('-')
    hiddenWordListList.set(hidden)


def updateHiddenWordList(letter):#returns true or false
    hidden = hiddenWordListList.get() #get the hidden word list
    word2 = word.get()  #get the word being geussed
    print(word2)
    count = 0
    boolFlag = None
    for x in word2:
        if letter == x:
            boolFlag = True
        else:
            boolFlag = False
        count += 1
    hiddenWordListList.set(hidden)
    if boolFlag == True:
        return True
    else:
        return False



#Initialize/New Game
#Text Entry Box drives entire game
def gameDriver():
    geuss = str(textEntry.get()) #get letter from text entry
    textEntry.delete(0, 'end') #clear text entry box
    #word = randomWord() #get a randomword, this needs to go somewhere else
    #initHiddenWordList(word) #This and above line needs moved to an init
    #attempts = int(getRemainingAttempts()) #get the current attempts made
    boolFlag = updateHiddenWordList(geuss)
    if boolFlag == False:
        updateWrongGeusses(geuss)
    elif boolFlag == True:
        updateHiddenWordList2(geuss)
    print(boolFlag)
    
def gameStartSetup():
    newWord = randomWord()
    word.set(newWord)
    initHiddenWordList(newWord)
    failedAttempts.set('8')
    wrongGeussesVar.set('')
    #update_idletasks(mainFrame)<--------<<<-??????????
    print("gameStartSetup() function hit.....")
    
#<<<----------^^^^^--------New function development--------^^^^^------->>>

#using an 8 column by 6 row grid??
#images are 400x400

#GUIdev---------------------------------------------------------------<<<<<<<<<<<<
root = Tk()
root.title("HangPy")
#setup the main frame to hold all widgets
mainFrame = ttk.Frame(root, padding="3 3 12 12", height=400, width=800)
mainFrame.grid(column=0, row=0, sticky=(N, S, E, W))
#if window resized, expand to take up extra space
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#vars for GUI
#word being geussed
word = StringVar()
#hidden string for gui
hiddenWordList = StringVar()#????
#hidden list for processing
hiddenWordListList = StringVar()
#var to hold wrong geussed letters
wrongGeussesVar = StringVar()
#var to hold the amount of attempts made
failedAttempts = StringVar() #should this be intVar???

####>>>>------------------------------------------------Buttons and Labels----<<<<<<<<
#photos for game
#gallows 1
photo1 = PhotoImage(file='C:\dev\hangpy\\resources\\001.gif')
photo2 = PhotoImage(file='C:\dev\hangpy\\resources\\002.gif')
photo3 = PhotoImage(file='C:\dev\hangpy\\resources\\003.gif')
photo4 = PhotoImage(file='C:\dev\hangpy\\resources\\004.gif')
photo5 = PhotoImage(file='C:\dev\hangpy\\resources\\005.gif')
photo6 = PhotoImage(file='C:\dev\hangpy\\resources\\006.gif')
photo7 = PhotoImage(file='C:\dev\hangpy\\resources\\007.gif')
photo8 = PhotoImage(file='C:\dev\hangpy\\resources\\008.gif')
photoPlayAgain = PhotoImage(file='C:\dev\hangpy\\resources\\playAgain.gif')
photoYouLose = PhotoImage(file='C:\dev\hangpy\\resources\\youLost.gif')
photoYouWin = PhotoImage(file='C:\dev\hangpy\\resources\\youWin.gif')
#<<<------------------------------------------->>>
photoPreview = ttk.Label(mainFrame, image=photo1)#
#<<<------------------------------------------->>>
photo1.image = photo1 # keep a reference!
photo2.image = photo2 # keep a reference!
photo3.image = photo3 # keep a reference!
photo4.image = photo4 # keep a reference!
photo5.image = photo5 # keep a reference!
photo6.image = photo6 # keep a reference!
photo7.image = photo7 # keep a reference!
photo8.image = photo8 # keep a reference!
photoPlayAgain.image = photoPlayAgain # keep a reference!
photoYouLose.image = photoYouLose # keep a reference!
photoYouWin.image = photoYouWin # keep a reference!
#<<<--------------------------------------------------------------->>>
photoPreview.grid(column=0, row=0, columnspan=4, rowspan=4, sticky=W)#
#<<<--------------------------------------------------------------->>>^^^

#correct geussed letters
#displays the hidden word array
lettersGeussedCorrect = ttk.Label(mainFrame, textvariable=hiddenWordList)
lettersGeussedCorrect.grid(column=0, row=5, columnspan=4, sticky=S)
lettersGeussedCorrect.config(font=("Courier", 25)) #<<----changes font size
#button for a new game
button1 = ttk.Button(mainFrame, text='New Game', command=gameStartSetup)
button1.grid(column=5, row=5, sticky=E)


#label to diplay attempts
attemptedGeusses = ttk.Label(mainFrame, textvariable=failedAttempts)
attemptedGeusses.grid(column=4, row=0, sticky=(N, W))
#label to head letters already geussed
alreadyGeussed = ttk.Label(mainFrame, text='You have already geussed these letters:')
alreadyGeussed.grid(column=4, row=0, sticky=(S, W))
#displays all the letters geussed that are wrong
wrongGeusses = ttk.Label(mainFrame, textvariable=wrongGeussesVar)
wrongGeusses.grid(column=5, row=1)
wrongGeusses.config(font=("Courier", 15)) #<<--------changes font size
#
#label to display previous geusses
#text entery to submit geusses
textEntry = ttk.Entry(mainFrame, textvariable=gameDriver)
textEntry.grid(column=4, row=2, sticky=W)
textEntry.bind("<Return>", lambda e: gameDriver())#F

gameStartSetup()

root.mainloop()




