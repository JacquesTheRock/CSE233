with open("BoyNames.txt") as boy:
	boylines = boy.read().splitlines()
#boy.close()

with open("GirlNames.txt") as girl:
	girllines = girl.read().splitlines()
#girl.close()
bf = 0
gf = 0
nm = raw_input('Enter a name: ')

for e in boylines:
	if e == nm:
		bf = 1

for e in girllines:
	if e == nm:
		gf = 1

if bf == 1 and gf == 1:
	print(nm + " is one of the most popular boy and girl names.")
elif bf == 1 and gf == 0:
	print(nm + " is one of the most popular boy names.")
elif bf == 0 and gf == 1:
	print(nm + " is one of the most popular girl names.")
else:
	print(nm + " is not one of the most popular names.")

boy.close()
girl.close()
