pop = open('word.txt','r')
x = pop.read()

rp = x.lower()

str1 = ''.join(rp)



import string
out = str1.translate(string.maketrans("",""), string.punctuation)
print(out)

words = out.split()
for word in words:
  print(word)
