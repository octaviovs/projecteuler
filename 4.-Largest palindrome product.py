value=0
lista=[]	
for x in xrange(999,-1,-1):
	for y in xrange(999,-1,-1):
		value= x*y
		if str(value)==str(value)[::-1]:
			lista.append(value)
			break
lista.sort() 
print lista[-1]
