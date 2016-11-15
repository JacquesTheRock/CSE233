# Group 3
# Question 7.9
# Donald Freeman

import re

f = open('text9.txt', 'r')
data = []
for line in f:
  newLine = re.sub('[\n]', '', line)
  data.append(newLine)

increase = []
for i in range(len(data)-1):
  diff = int(data[i+1]) - int(data[i])
  increase.append(diff)

lowest = increase[0]
highest = increase[0]
tally = 0
for i in range(len(increase)-1):
  if(increase[i]>highest):
    highest = increase[i]
  if(increase[i]<lowest):
    lowest = increase[i]
  tally = tally + increase[i]  

average = tally / len(increase)

print 'Average increase = ',
print average
print 'Lowest increase = ',
print lowest
print 'Highest increase = ',
print highest
