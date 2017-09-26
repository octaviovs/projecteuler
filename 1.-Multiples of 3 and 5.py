if __name__ == '__main__':
	x=0
	resultado=0
	while x<1000:
		if (x%3)==0 or (x%5)==0:
			resultado=resultado+x
		x=x+1
	print resultado


