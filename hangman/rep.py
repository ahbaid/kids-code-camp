def rep(guesses,word,guess):
   return 'x'


if __name__ == "__main__":
   w = 'elephant'
   g = '_' * w.__len__()
   g = list(g)

   l = 'e'

   p=0
   while p != -1:
      p = w.find(l,p)
      if p != -1:
         g[p] = l
         p += 1

   g = ''.join(g)
   
   print (w)
   print (g)
