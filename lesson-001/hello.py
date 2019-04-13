name = input("What is your name? ")
print ("Hello %s!" % name)
offset = ''
for letter in name:
   offset += ' '
   print(offset+letter)
