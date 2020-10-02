import readchar
import sys
import random
import time

global startingObs
global xDim
global yDim
global currentX
global currentY
global points
global targX
global targY
global obMax
global obNum
global obs
global lives
global dificulty
global mysMax
global mysMin
global myss
global mysNum

def printGrid():
	for y in range(0, yDim):
		for x in range(0, xDim):
			if (x == currentX and y == currentY):
				sys.stdout.write("@")
			elif (x == targX and y == targY):
				sys.stdout.write("$")
			elif (list((x, y)) in obs):
				sys.stdout.write("!")
			elif (list((x, y)) in myss):
				sys.stdout.write("?")
			else:
				sys.stdout.write("█")
				# sys.stdout.write("=")
		print("")

def genObs():
	for i in range(0, obNum):
		x = 0
		y = 0
		while True:
			x = random.randint(0, xDim)
			y = random.randint(0, yDim)
			if (x == currentX or y == currentY):
				continue

			break

		obs.append(list((x, y)))
		if (obs[i][0] == targX and obs[i][1] == targY):
			obs.pop()
			continue
		if (obs[i][0] == currentX and obs[i][1] == currentY):
			obs.pop()
			continue
	return obs

def genMys():
	for i in range(0, mysNum):
		myss.append(list((random.randint(0, xDim), random.randint(0, yDim))))
		if (myss[i][0] == targX and obs[i][1] == targY):
			myss.pop()
			continue
		if (myss[i][0] == currentX and myss[i][1] == currentY):
			myss.pop()
			continue
	return myss	

dificulty = input("E(EASY)M(MEDIUM)H(HARD)I(INSANE): ")
dificulty = dificulty.upper()

if ("E" in dificulty): 
	lives = 2
	obMax = 20
	obMin = 19
	startingObs = 1
elif ("M" in dificulty): 
	lives = 2
	obMax = 20
	obMin = 5
	startingObs = 3
elif ("H" in dificulty): 
	lives = 1
	obMax = 20
	obMin = 10
	startingObs = 8
elif ("I" in dificulty):
	lives = 1
	obMax = 30
	obMin = 20
	startingObs = 12 
else:
	print("Unknown dificulty. Going for medium!")
	lives = 2
	obMax = 20
	obMin = 5
	startingObs = 3

mysMax = 2
mysMin = 1
xDim = 50
yDim = 25
currentX = 0
currentY = 0
points = 0
targX = random.randint(0, xDim - 1)
targY = random.randint(0, yDim - 1)
obNum = random.randint(obMin, obMax - 1)
mysNum = random.randint(mysMin, mysMax - 1)
obs = list(())
myss = list(())

print(startingObs)

for i in range(0, 10):
	genObs()

genMys()

while True:
	# move = input("W(UP)A(LEFT)S(DOWN)D(RIGHT): ")
	move = readchar.readchar()
	move = move.upper()

	print("\n" * 1000)

	if ("W" in move):
		currentY = currentY - 1
	elif ("A" in move):
		currentX = currentX - 1
	elif ("S" in move):
		currentY = currentY + 1
	elif ("D" in move):
		currentX = currentX + 1
	elif ("Q" in move):
		exit()
	else:
		print("Not a move!")

	if (currentX == -1):
		currentX = xDim - 1
	elif (currentX == xDim):
		currentX = 0
	elif (currentY == -1):
		currentY = yDim - 1
	elif (currentY == yDim):
		currentY = 0

	if (list((currentX, currentY)) in obs):
		print("You ran into a obstical!")
		obs.remove(list((currentX, currentY)))
		points = points - 1
		lives = lives - 1

	if (list((currentX, currentY)) in myss):
		print("You found a mystery box!")
		myss.remove(list((currentX, currentY)))
		mysOutcome = random.randint(0, 1)
		if (mysOutcome == 0):
			print("You lose a life!")
			lives = lives - 1
		elif (mysOutcome == 1):
			print("You get a life!")
			lives = lives + 1

	if (currentX == targX and currentY == targY):
		print("You got a point!")
		points = points + 1
		targX = random.randint(0, xDim - 1)
		targY = random.randint(0, yDim - 1)
		obNum = random.randint(1, obMax - 1)
		mysNum = random.randint(mysMin, mysMax - 1)
		myss.clear()

		for i in range(0, startingObs):
			genObs()
		
		genMys()

	if (lives == 0):
		print("You died!")
		time.sleep(3)
		print("\n" * 1000)
		exit()

	print("POINTS: " + str(points) + ", LIVES: " + str(lives), ", AMOUNT COMPLETE: " + str(int(len(obs + myss)/(xDim * yDim) * 100)))
	print("Player Cords: X" + str(currentX) + ", Y" + str(currentY) + ". Target Cords: X" + str(targX) + ", Y" + str(targY))
	printGrid()
