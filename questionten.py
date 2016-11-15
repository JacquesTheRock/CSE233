with open("WorldSeriesWinners.txt") as f:
	flines = f.read().splitlines()

winner = raw_input("Enter a team: ")
wins = 0

for e in flines:
	if e == winner:
		wins += 1

print(winner + " has won " + str(wins) + " times.")

f.close()	
