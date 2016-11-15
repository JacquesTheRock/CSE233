# Group 3
# Question 7.11
# Donald Freeman

squareA = [[9, 3, 6], [5, 1, 4], [2, 7, 8]] 
squareB = [[4, 9, 2], [3, 5, 7], [8, 1, 6]] 
squareC = [[5, 3, 8], [4, 2, 7], [6, 9, 1]] 
squareD = [[5, 1, 7], [9, 4, 2], [6, 3, 8]] 
print 'Are they a Lo Shu Magic Square?'
checkSquareA = 'Nope, your square is trash!!'
for x in squareA:
	for y in range(3):
		if sum(x) == sum (squareA[y][y] for y in range(3)):
			if sum(x)== sum(x[y] for x in squareA):
				checkSquareA = 'YES, WOOHOO'
			else:
				checkSquareA = 'Nope, your square is trash!!'

print("SquareA is", checkSquareA)
checkSquareB = 'Nope, your square is trash!!'
for x in squareB:
	for y in range(3):
		if sum(x) == sum (squareB[y][y] for y in range(3)):
			if sum(x)== sum(x[y] for x in squareB):
				checkSquareB = 'YES, WOOHOO'
			else:
				checkSquareB = 'Nope, your square is trash!!'

print("SquareB is", checkSquareB)
checkSquareC = 'Nope, your square is trash!!'
for x in squareC:
	for y in range(3):
		if sum(x) == sum (squareC[y][y] for y in range(3)):
			if sum(x)== sum(x[y] for x in squareC):
				checkSquareC = 'YES, WOOHOO'
			else:
				checkSquareC = 'Nope, your square is trash!!'

print("SquareC is", checkSquareC)
checkSquareD = 'Nope, your square is trash!!'
for x in squareD:
	for y in range(3):
		if sum(x) == sum (squareD[y][y] for y in range(3)):
			if sum(x)== sum(x[y] for x in squareD):
				checkSquareD = 'YES, WOOHOO'
			else:
				checkSquareD = 'Nope, your square is trash!!'

print("SquareD is", checkSquareD)
