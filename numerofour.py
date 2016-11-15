numbers = []
size = 0
for num in range(0, 20):
	blank = input('Enter number ' + str(num+1) + ': ')
	int(blank)
	numbers.append(blank)
	size += blank
minimum = min(numbers)
maximum = max(numbers)
mean = size/20
print("\nMinimum value is: " + str(minimum))
print("Maximum value is: " + str(maximum))
print("Size of the list is: " + str(size))
print("Mean value is: " + str(mean))
