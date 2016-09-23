
from PIL import Image                
import numpy as np  
import matplotlib.pyplot as plt 
import sys

if len(sys.argv)>3:
	m1=int(sys.argv[1])
	m2=int(sys.argv[2])
	fuente = sys.argv[3]


	I = Image.open(fuente)
	I1=I.convert('L') 
	#I1.show()

	var= I1.size
	alto=int(var[0])
	largo=int(var[1])

	print str.format("imagen: {0}",fuente)
	print str.format("alto: {0}, largo: {1}",alto,largo)
	print str.format("generando matriz {0}x{1}",m1,m2)

	largoSubPlot=int(largo)/int(m1)
	altoSubPlot=int(alto)/int(m2)

	print str.format("subplots de {0}x{1}",largoSubPlot,altoSubPlot)
	a=np.asarray(I1,dtype=np.float32)
	y=0
	k=0
	print str.format("guardando salida")
	while y < m1:
		while k < m2:
			segmento=a[y*largoSubPlot:(y*largoSubPlot)+largoSubPlot,k*altoSubPlot:(k*altoSubPlot)+altoSubPlot]
			seg=Image.fromarray(segmento.astype(np.uint8)).save(str.format("salida{0}x{1}.jpg",y,k))
			k=k+1
		y=y+1
		k=0
else:
	print"faltan parametros"



