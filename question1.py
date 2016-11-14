# Group 3
# Question 7.1
# Donald Freeman

print "Please input dailey sales in $"
sales = []
sales.append(input('Input sales for Sunday: '))
sales.append(input('Input sales for Monday: '))
sales.append(input('Input sales for Tuesday: '))
sales.append(input('Input sales for Wenesday: '))
sales.append(input('Input sales for Thursday: '))
sales.append(input('Input sales for Friday: '))
sales.append(input('Input sales for Saturday: '))
total = 0
for i in range(7):
  total = total + sales[i]

print "The weekly total is: ",
print total,
print "dollars."
