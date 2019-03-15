#Gallows v1
#02/08/2019
#kilo.kilo.delta8@gmail.com
#
#Hangman type game using radnom word generation and tkinter gui.
#I made this as a goof and because why not?  Everyone else who picks up Python does. Lol!
#Enjoy....
#
#This script requires installs to run;
#    pip install pypandoc
#    pip install randomwordgenerator

from tkinter import *
from tkinter import ttk
from randomwordgenerator import randomwordgenerator
import random


#begin the root
root = Tk()
root.title("Gallows")
#setup the mainFrame Var to hold all widgets
mainFrame = ttk.Frame(root, padding="3 3 12 12", height=400, width=800)
mainFrame.grid(column=0, row=0, sticky=(N, S, E, W))


#global list that holds each image init
images = [PhotoImage(file='C:\dev\gallows\\resources\\youWin.gif'), 
    PhotoImage(file='C:\dev\gallows\\resources\\youLost.gif'), 
    PhotoImage(file='C:\dev\gallows\\resources\\008.gif'), 
    PhotoImage(file='C:\dev\gallows\\resources\\007.gif'), 
    PhotoImage(file='C:\dev\gallows\\resources\\006.gif'), 
    PhotoImage(file='C:\dev\gallows\\resources\\005.gif'), 
    PhotoImage(file='C:\dev\gallows\\resources\\004.gif'), 
    PhotoImage(file='C:\dev\gallows\\resources\\003.gif'), 
    PhotoImage(file='C:\dev\gallows\\resources\\002.gif'), 
    PhotoImage(file='C:\dev\gallows\\resources\\001.gif')]



def randomWord():
    '''
    fetch random word from internet, or backup text list
    '''
    try:
        randNum = random.randrange(0, 20)        #gen random number between 1 and 20
        num_words = 20                           #int var of 20
        wordList = randomwordgenerator.generate_random_words(n = num_words)
        return wordList[randNum]  #<-returnword from list, ^gen random word list
    except UnicodeEncodeError:    #if the above fails
        backupList = ['test', 'bounce', 'child', 'golf', 'whim']
        randNum = random.randrange(0, (len(backupList))) #choose random word from backup list
        return backupList[randNum]    #return random word


def stringToList(stringToConvert):
    '''
    Converts a single word string to a list.
    Takes 1 argument as a string.
    '''
    newList = []                 #init a empty list
    for x in stringToConvert:    #iter over func param (string)
        newList.append(x)        #add item to list
    return newList               #return list


def listToString(listToConvert):
    '''
    Converts a single word list to a string.
    Takes 1 argument as a list.
    '''
    newString = ""               #init an empty string
    for x in listToConvert:      #iter over list
        newString += x           #add to string
    return newString             #return the string


def updateWrongGeusses(letter):
    '''
    Updates a tkinter StringVar() with each letter that is incorrect.
    Takes 1 argument as a char.
    ''' 
    word2 = wrongGeussesVar.get() #get the current string/list
    newWord = word2 + letter  #add old list and wrong geuss param to new string
    wrongGeussesVar.set(newWord) #set new list/string to StringVar


def updateAttempts(): 
    '''
    Updates tkinter label as "AttemptsMade".
    Takes no arguments.
    '''           
    attempts = int(failedAttempts.get())    #fetch the StringVar() and convert to an int
    attempts -= 1                           #decrement by 1
    failedAttempts.set(attempts)            #set the StringVar() to the new value


def numAttempts():
    '''
    Returns/Sets attempts made during gameplay.
    Takes no arguments.
    '''
    attempt = failedAttempts.get()
    if attempt == None or attempt == '':
        return 8
    else:
        return int(attempt)

#sets the hidden list to start with all "-"'s
def initHiddenWordList(word):#for gui
    '''
    Creates a list the length of the word being geussed.
    Takes 1 argument as a a string.
    '''
    hidden = ''                    #init empty string
    for x in word:                 #iter through word param
        hidden += '-'              #for each iter add a "-" to the string 
    hiddenWordList.set(hidden)     #set the string to the StringVar()


def updateImage(num):
    '''
    Updates the image in a tkinter label.
    Takes 1 argument as a int.
    '''
    global images
    im = images[num]
    im.image = im
    photoPreview.configure(image = im)
    

def gameDriver():
    '''
    Drives the entire game, calling all functions each call.
    Takes no arguments.
    '''
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
    updateImage(numAttempts())
    if hidden == secretWord:
        wrong.append(" YOU WIN!!!!")#logic in this IF statement needs revisted hard!
        updateImage(-1)


def gameStartSetup():
    '''
    Called once when app is started and when new game clicked.
    Takes no arguments.
    '''
    updateImage(8)
    newWord = randomWord()        #generate a random word
    word.set(newWord)             #set StringVar to randWord
    initHiddenWordList(newWord)   #set hidden word list to size of randWord
    failedAttempts.set('8')       #set failed attempts to 8
    wrongGeussesVar.set('')       #set wrong geusses to empty
    


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


#using an 8 column by 6 row grid??
#images are 400x400
photoPreview = ttk.Label(mainFrame, width=50, textvariable=updateImage)
photoPreview.grid(column=0, row=0, columnspan=4, rowspan=4, sticky=(N, S, E, W))

#displays the hidden word array
lettersGeussedCorrect = ttk.Label(mainFrame, textvariable=hiddenWordList)
lettersGeussedCorrect.grid(column=0, row=5, columnspan=4, sticky=S)
lettersGeussedCorrect.config(font=("Courier", 25)) #<<----changes font size

#button for a new game
button1 = ttk.Button(mainFrame, text='New Game', command=gameStartSetup)
button1.grid(column=5, row=5, sticky=E)

#label stating attempts made
attemptsMade = ttk.Label(mainFrame, text="Remaining Attempts: ")
attemptsMade.grid(column=4, row=0, sticky=(N, W))

#label to diplay attempts
attemptedGeusses = ttk.Label(mainFrame, textvariable=failedAttempts)
attemptedGeusses.grid(column=5, row=0, sticky=(N, W))

#label to head letters already geussed
alreadyGeussed = ttk.Label(mainFrame, text='You have already geussed these letters:')
alreadyGeussed.grid(column=4, row=0, sticky=(S, W))

#displays all the letters geussed that are wrong
wrongGeusses = ttk.Label(mainFrame, textvariable=wrongGeussesVar)
wrongGeusses.grid(column=4, row=1, sticky=W)
wrongGeusses.config(font=("Courier", 15)) #<<--------changes font size

#label to display previous geusses
#text entery to submit geusses
textEntry = ttk.Entry(mainFrame, textvariable=gameDriver)
textEntry.grid(column=4, row=2, sticky=W)
textEntry.bind("<Return>", lambda e: gameDriver())



#init the first game on startup
gameStartSetup()
root.mainloop()




