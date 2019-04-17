import sys
import os

def usage():
   print ("\nUsage:")
   print ("======")
   print ("hangman.py <filename>")
   print ("- filename: path to file with words, one per line.\n")

def main():

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

   # print the words
   for word in words:
       print(word)

if __name__ == '__main__':
   main()
