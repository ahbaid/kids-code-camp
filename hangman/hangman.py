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
   if errors == 0:
      print(" +=====+=====+ ")
      print(" +     |     + ")
      print(" +           + ")
      print(" +           + ")
      print(" +           + ")
      print(" +           + ")
      print(" + 0 errors  + ")
      print("=+===========+=")
   elif errors == 1:
      print(" +=====+=====+ ")
      print(" +     |     + ")
      print(" +     O     + ")
      print(" +           + ")
      print(" +           + ")
      print(" +           + ")
      print(" + 1 error!  + ")
      print("=+===========+=")
   elif errors == 2:
      print(" +=====+=====+ ")
      print(" +     |     + ")
      print(" +     O     + ")
      print(" +     |     + ")
      print(" +           + ")
      print(" +           + ")
      print(" + 2 errors! + ")
      print("=+===========+=")
   elif errors == 3:
      print(" +=====+=====+ ")
      print(" +     |     + ")
      print(" +     O     + ")
      print(" +    /|     + ")
      print(" +           + ")
      print(" +           + ")
      print(" + 3 errors! + ")
      print("=+===========+=")
   elif errors == 4:
      print(" +=====+=====+ ")
      print(" +     |     + ")
      print(" +     O     + ")
      print(" +    /|\    + ")
      print(" +           + ")
      print(" +           + ")
      print(" + 4 errors! + ")
      print("=+===========+=")
   elif errors == 5:
      print(" +=====+=====+ ")
      print(" +     |     + ")
      print(" +     O     + ")
      print(" +    /|\    + ")
      print(" +    /      + ")
      print(" +           + ")
      print(" + 5 errors! + ")
      print("=+===========+=")
   elif errors == 6:
      print(" +=====+=====+ ")
      print(" +     |     + ")
      print(" +     O     + ")
      print(" +    /|\    + ")
      print(" +    / \    + ")
      print(" + You Died! + ")
      print(" + 6 errors! + ")
      print("=+===========+=")
   # }}}

def main():
   # {{{ main code

   if (sys.argv.__len__() != 2):
      usage()
      sys.exit()
   else:
      # Assign first argument to filename
      filename = sys.argv[1]

   # Validate that the file is readable
   if not os.path.isfile(filename):
      print ("\nError file {} is not readable.\n".format(filename))
      sys.exit()

   # A list to hold the words we will be working with
   words=[]

   # Open the file and assign it to a handler
   wordfile = open(filename,'r')
 
   # read each line of the file, stripping off the end of line character
   for line in wordfile:
      # Append each word in the file (each line) to the words list
      words.append(line.strip().lower())

   # close the file
   wordfile.close()

   # Pick a random word from the list of words
   word = words[random.randrange(0,words.__len__())]

   # Initialize a string to represent the word being guessed
   guessed = '_' * word.__len__()

   # Initialize counters for guesses, errors & letter
   guesses=0
   errors=0
   letter=''

   
   while ((letter != '0') and (errors < 7)):
      letter=input("\nGuess a letter [0 quits]: ")
      letter.strip()
      gallows(errors)
      errors += 1

   print("\nThanks for playing....\n")

   # }}}
   
if __name__ == '__main__':
   main()
