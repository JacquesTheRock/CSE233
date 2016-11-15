# Group 3
# Question 7.5
# Donald Freeman
f = open("Accounts.txt",'r')
acc = input("Please input an account")
acc = acc + "\n"
if acc in f.readlines():
	print("Account found")
else:
	print("Account not found")
