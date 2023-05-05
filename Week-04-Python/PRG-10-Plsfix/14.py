'''
The output should be:
True
'''
def rtn(x):
	return(x)

foo = rtn(3)

#changed line---
#if foo > rtn(4):
#	print(True)


if foo < rtn(4):
	print(True)
else:
	print(False)