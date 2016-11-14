# Group 3
# Question 7.3
# Donald Freeman

print "Please input rainfall in inches"
rainfall = []
rainfall.append(input('Input rainfall for Jan: '))
rainfall.append(input('Input rainfall for Feb: '))
rainfall.append(input('Input rainfall for Mar: '))
rainfall.append(input('Input rainfall for Apr: '))
rainfall.append(input('Input rainfall for May: '))
rainfall.append(input('Input rainfall for Jun: '))
rainfall.append(input('Input rainfall for Jul: '))
rainfall.append(input('Input rainfall for Aug: '))
rainfall.append(input('Input rainfall for Sep: '))
rainfall.append(input('Input rainfall for Oct: '))
rainfall.append(input('Input rainfall for Nov: '))
rainfall.append(input('Input rainfall for Dec: '))
total = 0
highest = rainfall[0]
lowest = rainfall[0]
for i in range(12):
  total = total + rainfall[i]
  if(rainfall[i] > highest):
    highest = rainfall[i]
  if(rainfall[i] < lowest):
    lowest = rainfall[i]

average = total / 12
print "Total rainfall: "
print total,
print " "
print "Average rainfall: "
print average,
print " "
print "Lowest rainfall: "
print lowest,
print " "
print "Highest rainfall: "
print highest,
