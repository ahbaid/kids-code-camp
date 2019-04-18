import sys
import os
import random

def usage():
   print ("\nUsage:")
   print ("======")
   print ("hangman.py <filename>")
   print ("- filename: path to file with words, one per line.\n")

def gallows(errors):
   # {{{ gallows code
   print()
   EL = [
          " +=====+=====+ ",
          " +     |     + ",
          " +           + ",
          " +           + ",
          " +           + ",
          " +           + ",
          " +           + ",
          "=+===========+="
        ]
   if errors == 0:
      EL[6] = " + 0 errors  + "
   elif errors == 1:
      EL[2] = " +     O     + "
      EL[6] = " + 1 error   + "
   elif errors == 2:
      EL[2] = " +     O     + "
      EL[3] = " +     |     + "
      EL[6] = " + 2 errors  + "
   elif errors == 3:
      EL[2] = " +     O     + "
      EL[3] = " +    /|     + "
      EL[6] = " + 3 errors  + "
   elif errors == 4:
      EL[2] = " +     O     + "
      EL[3] = " +    /|\    + "
      EL[6] = " + 4 errors  + "
   elif errors == 5:
      EL[2] = " +     O     + "
      EL[3] = " +    /|\    + "
      EL[4] = " +    /      + "
      EL[6] = " + 5 errors  + "
   elif errors == 6:
      EL[2] = " +     O     + "
      EL[3] = " +    /|\    + "
      EL[4] = " +    / \    + "
      EL[5] = " + You Died! + "
      EL[6] = " + 6 errors! + "

   for e in EL:
      print(e)

   # }}}

def updateguess(guesslist,word,letter):
   # {{{ updateguess code

   guesslist = list(guesslist)

   pos=0
   while pos != -1:
      pos = word.find(letter,pos)
      if pos != -1:
         guesslist[pos] = letter
         pos += 1

   return ''.join(guesslist)
   
   # }}}

def main():
   # {{{ main code

   # {{{ Check for arguments
   if (sys.argv.__len__() != 2):
      usage()
      sys.exit()
   else:
      # Assign first argument to filename
      filename = sys.argv[1]
   # }}}

   # {{{ Validate word file is readable
   if not os.path.isfile(filename):
      print ("\nError file {} is not readable.\n".format(filename))
      sys.exit()
   # }}}

   # Declare an empty list to hold the words 
   words=[]

   # {{{ read each line of the file, stripping off the end of line character into words list

   # Open the word file and assign it to a handler
   wordfile = open(filename,'r')
 
   for line in wordfile:
      # Append each word in the file (each line) to the words list
      words.append(line.strip().lower())

   # close the file
   wordfile.close()

   # }}}

   # Pick a random word from the list of words
   word = words[random.randrange(0,words.__len__())]

   # Initialize a string to represent the word being guessed
   guessed = '_' * word.__len__()

   # Initialize a string to capture all guesses
   allguesses = ''

   # Initialize counters for guesses, errors, guess & tries
   guesses=0
   errors=0
   guess=''
   tries=0
   
   while ((guess != '0') and (errors < 6)) and (guessed != word):
      gallows(errors)
      print("\nYour current guess: %s\n" % guessed)
      guess=input("\nGuess a letter [0 quits]: ")
      guess.strip()

      if guess != '0':
         if word.find(guess) != -1:
            guessed = updateguess(guessed,word,guess)
         else:
            if guessed.find(guess) == -1:
               if allguesses.find(guess) == -1:
                  errors += 1
                  allguesses += guess
            else:
               print("\nYou guessed %s already\n" % guess)

         tries += 1

   # Failed
   if errors == 6:
      gallows(errors)

   # Quit early
   if guess == '0':
      print("\nYour word was: %s\n" % word)
      if tries == 1:
         print("You gave up after %d try....\n" % tries)
      else:
         print("You gave up after %d tries....\n" % tries)
   # Guessed
   else:
      # Won!
      if (guessed == word):
         print("\n!! %s !!\n" % word)
         print("You Won!\n")
      # Did not win
      else:
         print("\nThanks for playing, your word was %s\n" % word)

   # }}}
   
if __name__ == '__main__':
   main()
