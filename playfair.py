
matrixOfLetters = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
keyword = input('enter keyword')
presentInMatrix = {}

for letter in keyword:
	presentInMatrix[letter] = False
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for letter in letters:
	presentInMatrix[letter] = False
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
if(not presentInMatrix['I'] and not presentInMatrix['J']):
	presentInMatrix['I'] = True
if(presentInMatrix['I'] == True):
	presentInMatrix['J'] = True
if(presentInMatrix['J'] == True):
	presentInMatrix['I'] = True
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
text = text.replace(" ", "")
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
	i1,j1 = findInMatrix(item[0])
	i2,j2 = findInMatrix(item[1])
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
