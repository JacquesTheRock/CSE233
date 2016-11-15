import random
ranVar = ""
for num in range(0, 7):
	ranVar += str(random.SystemRandom().randrange(0, 9)) + " "
listy = ranVar.split()
print("Lottery Numbers are: ")
for e in listy:
	print(e)
