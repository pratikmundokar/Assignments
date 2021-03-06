matrixOfLetters = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
keyword = input('enter keyword')
presentInMatrix = {} #dictionary to track if letter in matrix or not
# set all false initially for both letters array and keyword array
for letter in keyword:
	presentInMatrix[letter] = False
for letter in letters:
	presentInMatrix[letter] = False
# handle case where keyword has I and J both 
if('I' in keyword and 'J' in keyword):
	presentInMatrix['I'] = True
	
# assign letters in matrix first from keyword and then from letters array
i,j = 0,0
for letter in keyword:
	if(presentInMatrix[letter] == False):
		matrixOfLetters[i][j] = letter
		presentInMatrix[letter] = True
		if(j<4):
			j = j+1
		elif(i<4):
			j = 0
			i = i+1
# ensure all cases of I and J
if(not presentInMatrix['I'] and not presentInMatrix['J']):
	presentInMatrix['I'] = True
	presentInMatrix['IORJ'] = 'J'
elif(presentInMatrix['I'] == True):
	presentInMatrix['J'] = True
	presentInMatrix['IORJ'] = 'I'
elif(presentInMatrix['J'] == True):
	presentInMatrix['I'] = True
	presentInMatrix['IORJ'] = 'J'
for letter in letters:
	if(presentInMatrix[letter] == False):
		matrixOfLetters[i][j] = letter
		if(j<4):
			j = j+1
		elif(i<4):
			j = 0
			i = i+1
		

		
			
print(matrixOfLetters)


text = input('Enter text')
betterText = ''
text = text.replace(" ", "")
for i in range(len(text)):
	if(i!=len(text)-1):
		if(text[i] == text[i+1]):
			if(i%2 == 0 and (i+1)%2 == 1):
				text = text[:i+1]+'X'+text[i+1:len(text)]
		
print(text)

out = [(text[i:i+2]) for i in range(0, len(text), 2)]
if(len(out[-1])== 1):
	out[-1] = out[-1]+'X'
print(out)

def findInMatrix(letter):
	for i in range(5):
		for j in range(5):
			if(matrixOfLetters[i][j] == letter):
				return i,j
finalAns = list()
for item in out:
	l1 = item[0]
	l2 = item[1]

	if(l1 == 'I' and presentInMatrix['IORJ'] == 'J'):
		i1,j1 = findInMatrix('J')
	elif(l1 == 'J' and presentInMatrix['IORJ'] == 'I'):
		i1,j1 = findInMatrix('I')
	else:
		i1,j1 = findInMatrix(l1)

	if(l2 == 'I' and presentInMatrix['IORJ'] == 'J'):
		i2,j2 = findInMatrix('J')
	elif(l2 == 'J' and presentInMatrix['IORJ'] == 'I'):
		i2,j2 = findInMatrix('I')
	else:
		i2,j2 = findInMatrix(l2)
		




	if(i1 == i2):
		j1 = (j1+1)%5
		j2 = (j2+1)%5
		finalAns.append(matrixOfLetters[i1][j1]+matrixOfLetters[i2][j2])
	elif(j1 == j2):
		i1 = (i1+1)%5
		i2 = (i2+1)%5
		finalAns.append(matrixOfLetters[i1][j1]+matrixOfLetters[i2][j2])
	else:
		finalAns.append(matrixOfLetters[i1][j2]+matrixOfLetters[i2][j1])
print(finalAns)
