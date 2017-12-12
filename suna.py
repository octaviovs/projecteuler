def matriz(base,NumA,NumB):
		#tabla de valores 00 XX ZZ
	tabla=[]
		#tabla de concatenacion
	conca=[]
		#valores 
	
	m1=[]
	m2=[]
	m=[m1,m2] 
		#estados
	
	e1=[]
	e2=[]
	e=[e1,e2]

	maquina=[tabla,e,m]
	#maquina[] muestra indices de combiacnioes
	#maquina [][] muestra cada lista 0 indice de combiaciones 1 estados 2 resultados
	limite=base**2
	bandera=False
	#Se genero la matriz bidimencional Ex y o0
	#for x in xrange(base):
	#	m.append([0]*limite)
	#	e.append([0]*limite)
		###
		#el siguiente codifo genera la tabla de estados y de valores 
		#en el primer ciclo genera los estados e0 si hay un acarreo pasa al e1
		#en el segundo ciclo cada valor lleva un acarreo
	print "Combiacion de numero"
	for proceso in xrange(2):
		for x in xrange(base):
			for y in xrange(base):
				#print	x,y
				#E0
				if not bandera:
					value=x+y
					tabla.append(str(x)+""+str(y))
					if value>=base:
						e1.append("e1")
						value=value-base
						m1.append(value)
						#print "e1---"
					else:
						m1.append(value)
						e1.append("e0")
						#print "e0---"
				else:
				#E1
					value=x+y+1
					if value>=base:
						e2.append("e1")
						value=value-base
						m2.append(value)
						#print "e1"
					else:
						e2.append("e0")
						m2.append(value)
						#print "e0"
		bandera=True

	print tabla
	print "Tabla de estado"
	print e1
	print e2
	print "Tabla de valores"
	print m1
	print m2




# los valores recibidos son dividios en una matriz para evaluarlos
	c = NumA.split("|")
	cc = NumB.split("|")

	for x in xrange(len(cc)):
		conca.append(str(c[x]+cc[x]))
		
	
	print "tabla de concatenacion \n"

	print conca.reverse()
	print "tabla asociativa"
	print maquina
	print""
	print "------------------------Proceso de suma-------------"
	print	""
	cadena=""
	Ed=True
	sumador=0
	bandera=True
	#en el siguiente ciclo se buscan las combinaciones en la tabla de estados
	for x in xrange(len(c)):
		sumador=0
		bandera=True
		if Ed:
			print "Buscar E0 , cadena es=>:",conca[x]
			while bandera:
				if maquina[0][sumador]==conca[x]:
					bandera=False
				sumador=sumador+1
			#print "sumador es->",sumador
			#print sumador-1
			print "Resultado de valor",maquina[2][0][sumador-1]
			cadena=cadena+str(maquina[2][0][sumador-1])
			print maquina[1][0][sumador-1]
			if maquina[1][0][sumador-1]=="e0":
				Ed=True
			else:
				Ed=False
		else:
			print "Buscar E1 , cadena es=>:",conca[x]


			while bandera:
				if maquina[0][sumador]==conca[x]:
					bandera=False
				sumador=sumador+1
			#print "sumador es->",sumador
			print sumador-1
			print "Resultado de valor",maquina[2][1][sumador-1]
			cadena=cadena+str(maquina[2][1][sumador-1])
			print maquina[1][1][sumador-1]
			if maquina[1][1][sumador-1]=="e0":
				Ed=True
			else:
				Ed=False


				
#como resultado nos regresa un valor entro
	print "Resultado->",cadena[::-1]
	
#Incio de la maquina de suma
if __name__ == "__main__":
	##vaiables
	
	print "Maquina de estado finito-suma"
	print""
	print""
	print "ingrese la base"
	base=400
	print "ingrese primer numero"
	a="0|0|399"
	print "ingrese segundo numero"
	b="0|0|1"
	matriz(base,a,b)

	

	
