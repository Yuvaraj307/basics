pop = open('word.txt','r')
x = pop.read()

rp = x.lower()

str1 = ''.join(rp)
words = str1.split()
for word in words:
  print(word)
