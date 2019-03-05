# gallows
Everyone else makes a "hangman" style game, why not?  A few weeks into LaunchCode with Python gave me the idea to make my own version, and
taking note from classmates.

This script requires to PIP installs;
  +pypandoc
  +randomwordgenerator
  
We start by fetching 20 random words from the web, with a backup list in the event the web is down.  These are stored into a list with one
word selected by a random number generated using the random module.
The random word is tored into a list, and a "duplicate list is made of the same length, but with "-"s instead of letters.  The dashes list
is stored to a tkinter StringVar() to be displayed in a label.  Also stored in a StringVar() is the attempts remaining and already used 
letters that are wrong.
The user enters a letter via a text entry box, using the <Enter> key.  The entry is compared to the original random word and if the geuss
is valid, the "-"s list is updated with the geuss.  If it is not, the worng geuss is added to the wrong geuss label and the attempts is
decremented by one.
This is where the asciiArt changes.  In the future the GIFS in the resources folder will take the asciiArt's place.

This script functions as is, however buggy, it is in development and due some fine tweaking.  One day at a time.
I am always down for input, collab, etc.
