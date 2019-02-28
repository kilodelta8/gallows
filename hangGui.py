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

def lettersGeussed():
    x = randomWord()
    y = len(x)
    geussing = []
    for z in range(y):
        geussing.append("-")
    geussedWord.set(geussing)
    

#using an 8 column by 6 row grid??
#images are 400x400 and 


root = Tk()
root.title("HangPy")
#setup the main frame to hold all widgets
mainFrame = ttk.Frame(root, padding="3 3 12 12", height=400, width=800)
mainFrame.grid(column=0, row=0, sticky=(N, S, E, W))
#if window resized, expand to take up extra space
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#vars
geussedWord = StringVar()


#photos for game
#gallows
photo1 = PhotoImage(file='C:\dev\hangpy\\resources\\001.gif')
photoPreview = ttk.Label(mainFrame, image=photo1)
photo1.image = photo1 # keep a reference!
photoPreview.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=W)
#correct geussed letters
#
lettersGeussedCorrect = ttk.Label(mainFrame, textvariable=geussedWord)
lettersGeussedCorrect.grid(column=0, row=5, columnspan=4, sticky=S)
button1 = ttk.Button(mainFrame, text='setvar', command=lettersGeussed)
button1.grid(column=5, row=5, sticky=E)

    #label to diplay letters already geussed
alreadyGeussedLetters = ttk.Label(mainFrame, text='This area is for already geussed letters')
alreadyGeussedLetters.grid(column=5, row=0, sticky=N)


root.mainloop()




