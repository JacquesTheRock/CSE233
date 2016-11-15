# Group 3
# Question 7.7
# Donald Freeman

import re

correct = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
f = open('text7.txt', 'r')
data = []
for line in f:
  newLine = re.sub('[\n]', '', line)
  data.append(newLine)

totalScore = 0
wrong = []
for i in range(20):
  if(correct[i]==data[i]):
    totalScore = totalScore + 1
  else:
    wrong.append(i)

if(totalScore>11):
  print 'You passed!'
else:
  print 'Sorry chump, you are the worst and you failed...'

print 'You scored ',
print totalScore,
print 'out of 20'
print 'You got ',
print wrong,
print 'wrong.'
