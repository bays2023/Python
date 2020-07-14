import math
minNum = 1
maxNum = 1000000000
primeList = []
def resetDoc():
	doc = open("primeNumbers.txt", "w")
	doc.write("")
	doc.close
def addLine(num):
	doc = open("primeNumbers.txt", "a")
	doc.write(str(num) + "\n")
	doc.close
resetDoc()
if minNum == 1:
	minNum = 2
for number in range(minNum, maxNum + 1):
	prime = True
	for divisor in range(2, (round(math.isqrt(number) + 1))):
		if number % divisor == 0:
			prime = False
	if prime == True:
		primeList.append(number)
		addLine(number)
print(primeList)
