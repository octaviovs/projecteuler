if __name__ == '__main__':
	a=0
	b=1
	c=0
	x=4000000
	res=0
	for x in xrange(1,x):
		c=a+b
		a=b
		b=c
		if c>4000000:
			break;
		else:
			if c%2==0:
				res=res+c
	print res