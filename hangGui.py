from tkinter import *
from tkinter import ttk
from randomwordgenerator import randomwordgenerator
import random

def setGeussVar():
    letter = textEntry.get()
    textEntry.delete(0, 'end')
    geussLetter.set(letter)

def play(word, geussWord):
    geuss = str(input("Enter a letter: "))
    count = 0
    for x in word:
        if geuss == x:
            geussWord[count] = geuss
        count += 1

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

#returns a list of "-", the size of the randomly selected word
def hiddenWordList(selectedWord):
    hideWord = []
    for z in range(len(selectedWord)):
        hideWord.append("-")
    #geussedWord.set(geussing)
    return hideWord
    

#using an 8 column by 6 row grid??
#images are 400x400 and 

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
hiddenWordVar = StringVar()#????
#var to hold the amount of attempts
geussLetter = StringVar()
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
lettersGeussedCorrect = ttk.Label(mainFrame, textvariable=hiddenWordVar)
lettersGeussedCorrect.grid(column=0, row=5, columnspan=4, sticky=S)
lettersGeussedCorrect.config(font=("Courier", 44)) #<<----changes font size
#button for a new game
button1 = ttk.Button(mainFrame, text='New Game', command=None)
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
wrongGeusses.config(font=("Courier", 44)) #<<--------changes font size
#
#label to display previous geusses
#text entery to submit geusses
textEntry = ttk.Entry(mainFrame, textvariable=setGeussVar)
#textEntry.bind(<Enter>, enter)<<<------WTF?!?!?!?!
textEntry.grid(column=4, row=2, sticky=W)





#Game logic/loop
#
#get random word and store it in a list
randWord = randomWord()
print(randWord)

#initialize the hidden word list
hiddenWord = hiddenWordList(randWord)
print(hiddenWord)

#set the maximum allowed geusses (per game)
maxGeusses = len(randWord) - 1
print(maxGeusses)
root.mainloop()
geusses = 0
count = 0
while hiddenWord != randomWord:
    wrongLetters = []
    #update hidden array here??
    if geusses < maxGeusses:
        hiddenWordVar.set(hiddenWord)
        wrongGeussesVar.set(wrongLetters)
        failedAttempts.set(geusses)
        #letter = geussLetter.get()
        for x in randWord:
            if letter == x:
                hiddenWord[count] = letter
            else:
                wrongLetters.append(letter)
                geusses += 1
        count += 1

#root.mainloop()




