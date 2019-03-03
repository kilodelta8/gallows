#Gallows v1
#02/08/2019
#kilo.kilo.delta8@gmail.com
#
#Hangman type game using radnom word generation and tkinter gui.
#I made this as a goof and because why not?  Everyone else who picks up Python does. Lol!
#Enjoy....
#

from tkinter import *
from tkinter import ttk
from randomwordgenerator import randomwordgenerator
import random

#fetch random word from internet, or backup text list
def randomWord():
    try:
        randNum = random.randrange(0, 20)        #gen random number between 1 and 20
        num_words = 20                           #int var of 20
        wordList = randomwordgenerator.generate_random_words(n = num_words)
        return wordList[randNum]  #<-returnword from list, ^gen random word list
    except UnicodeEncodeError:    #if the above fails
        backupList = ['test', 'bounce', 'child', 'golf', 'whim']
        randNum = random.randrange(0, (len(backupList))) #choose random word from backup list
        return backupList[randNum]    #return random word

#Setters
def updateGallows(img): # Main imagery
    pass

#converts the StringVar() string to a list, because lists are easier to update.  LOL!
def stringToList(stringToConvert):
    newList = []                 #init a empty list
    for x in stringToConvert:    #iter over func param (string)
        newList.append(x)        #add item to list
    return newList               #return list

#converts a list to a string for the StringVar()'s
def listToString(listToConvert):
    newString = ""               #init an empty string
    for x in listToConvert:      #iter over list
        newString += x           #add to string
    return newString             #return the string

#adds each geuss that is incorrect to the wrongGeuss StringVar()
def updateWrongGeusses(letter): 
    word2 = wrongGeussesVar.get() #get the current string/list
    newWord = word2 + letter  #add old list and wrong geuss param to new string
    wrongGeussesVar.set(newWord) #set new list/string to StringVar

#updates the attempts failed at the top of window
def updateAttempts():            
    attempts = int(failedAttempts.get())    #fetch the StringVar() and convert to an int
    attempts -= 1                           #decrement by 1
    failedAttempts.set(attempts)            #set the StringVar() to the new value

#sets the hidden list to start with all "-"'s
def initHiddenWordList(word):#for gui
    hidden = ''                    #init empty string
    for x in word:                 #iter through word param
        hidden += '-'              #for each iter add a "-" to the string 
    hiddenWordList.set(hidden)     #set the string to the StringVar()

#Initialize/New Game
#Text Entry Box drives entire game
def gameDriver():
    secretWord = stringToList(word.get())       #get the word being geussed adn convert to list
    hidden = stringToList(hiddenWordList.get()) #get the current hidden word and convert to list
    wrong = stringToList(wrongGeussesVar.get()) #get the current wrong geuss list
    geuss = str(textEntry.get())                #get letter from text entry box
    textEntry.delete(0, 'end')                  #clear text entry box
    #print(secretWord)
    for i, x in enumerate(secretWord): #iter over secretWord with a counter
        if geuss == x:                 #if geuss equals letter x at index i
            hidden[i] = geuss          #set index i of hidden list to geuss
    if geuss not in secretWord:
        updateAttempts()               #update attemps left
        wrong.append(geuss)            #add invalid geuss to wrong geuss list
    hiddenWordList.set(listToString(hidden)) #convert list back to string for StringVar()
    wrongGeussesVar.set(listToString(wrong)) #convert list back to string for StringVar()
    #root.update_idletasks()#<--------<<<-??????????
    if hidden == secretWord:
        wrong.append(" YOU WIN!!!!")

#init all variables and the such when the script first executes ad when button pressed
def gameStartSetup():
    newWord = randomWord()        #generate a random word
    word.set(newWord)             #set StringVar to randWord
    initHiddenWordList(newWord)   #set hidden word list to size of randWord
    failedAttempts.set('8')       #set failed attempts to 8
    wrongGeussesVar.set('')       #set wrong geusses to empty
    #update_idletasks(mainFrame)<--------<<<-??????????
    #print("gameStartSetup() function hit.....") #alert me via CLI this func executed
    
#using an 8 column by 6 row grid??
#images are 400x400

#GUIdev---------------------------------------------------------------<<<<<<<<<<<<
root = Tk()
root.title("Gallows")
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
textEntry.bind("<Return>", lambda e: gameDriver())

#init the first game on startup
gameStartSetup()
root.mainloop()




