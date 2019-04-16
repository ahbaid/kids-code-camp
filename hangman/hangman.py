words=[]

f = open('words.txt','r')
for line in f:
   words.append(line.strip())
f.close()

print(words)
