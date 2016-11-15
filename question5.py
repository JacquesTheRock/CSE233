# Group 3
# Question 7.5
# Donald Freeman

#import re
#userAcc = input('Enter you 7 digit user account: ')
#userAcc = str(userAcc)
#f = open('text5.txt', 'r')
#data = []
#for line in f:
#  newLine = re.sub('[\n]', '', line)
#  data.append(newLine)
#
#if any(userAcc in s for s in data):
#  print 'Your account is valid and exists.'
#else:
#  print 'Invalid account number.'

f = open("text5.txt",'r')
acc = input("Please input an account")
if acc in f:
	print("Account found")
else:
	print("Account not found")
