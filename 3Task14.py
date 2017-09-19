def double_let(word):
	i = 0
	count = o
	while i < len(word)-1:
		if word[i] == word[i+1]:
			count +=1
			i += 2
		else:
			i +=1
			count = 0
		if count == 3:
			return True
		else:
			return False
		value= double_let("asdasdas")
		print (value)