#CALCULADOR DE INDICADORES CONTA G

'ORDEN DE EJECUCIÓN: RPN - RIT - Apalancamiento - TFP - Punto equilibrio - Margen seguridad - Margen contribución - Margen dupont - Rotacion'

# DEFINICION DE FUNCIONES

#DEFINICIÓN DE FUNCION DE PROMEDIO:

def promedio(x,y):
    prom = (x + y)/2
    return prom

#DEFINICION ANALISIS DE TENDENCIA
def tendencia(x,y):
    trend = ((x / y) - 1) * 100
    return trend

#DEFINICION DE FUNCION DE RPN
def RPN(x,y):
    repn = (x / y) * 100
    return repn

#DEFINICIÓN DE RIT
def RIT(x,y,v):
    ritc = ((x + y)) / v * 100
    return ritc

#DEFINICIÓN DE TFP
def TFP(x,y):
    tfpcalc = (x/y) * 100
    return tfpcalc

#PUNTO DE EQUILIBRIO
def puntoequilibrio(x,y,v):
    equilibrio = x / (1-(y/v))
    return equilibrio

#MARGEN DE SEGURIDAD
#Se usan las ventas actuales y el resultado del punto de equilibrio
def margenseg(x,y):
    segu = (x - y) / x
    return segu

#MARGEN DE CONTRIBUCIÓN
def contribucion(x,y):
    contri = 1 - (x/y)
    return contri

#MARGEN DUPON SOBRE VENTAS

def margdupon(x,y,v):
    duponmargen = ((x + y)/v) * 100
    return duponmargen

#ROTACION
def rotacion(x,y):
    rota = x / y
    return rota


# FIN DE FUNCIONES

# TOMA DE DATOS:

respn1 = float(input("Ingrese el PN total para el Ejercicio 0: "))
respn2 = float(input("Ingrese el PN total para el Ejercicio 1: "))
respn3 = float(input("Ingrese el PN total para el Ejercicio 2: "))
resnet1 = float(input("Ingrese el resultado neto del Ejercicio 1: "))
resnet2 = float(input("Ingrese el resultado neto del Ejercicio 2: "))
resactiv1 = float(input("Ingrese el activo total para el Ejecicio 0: "))
resactiv2 = float(input("Ingrese el activo total para el Ejercicio 1: "))
resactiv3 = float(input("Ingrese el activo total para el Ejercicio 2: "))
respasivo1 = float(input("Ingrese el resultado financiero generado por pasivos del Ejercicio 1 (No incluya signo negativo): "))
respasivo2 = float(input("Ingrese el resultado financicero generado por pasivos del Ejercicio 2 (No inlcuya signo negativo): "))
respasiv1 = float(input("Ingrese el total del pasivo para el Ejercicio 0:"))
respasiv2 = float(input("Ingrese el total del pasivo para el Ejercicio 1:"))
respasiv3 = float(input("Ingrese el total del pasivo para el Ejercicio 2:"))
ventas1 = float(input("Ingrese el total de las ventas del Ejercicio 1: "))
ventas2 = float(input("Ingrese el total de las ventas del Ejercicio 2: "))
costofijo1 = float(input("Ingrese los costos fijos para el Ejercicio 1 (Nota: Los debe calcular usted): "))
costovar1 = float(input("Ingrese los costos variables para el Ejercicio 1 (Nota: Los debe calcular usted): "))
costofijo2 = float(input("Ingrese los costos fijos para el Ejercicio 2 (Nota: Los debe calcular usted): "))
costovar2 = float(input("Ingrese los costos variables para el Ejercicio 2 (Nota: Los debe calcular usted): "))
# FIN DE TOMA DE DATOS

# CALCULOS
prompn1 = promedio(respn1, respn2)
prompn2 = promedio(respn2, respn3)
rpn1 = RPN(resnet1, prompn1)
rpn2 = RPN(resnet2, prompn2)
repntrend = tendencia(rpn2,rpn1)

#PROMEDIO DEL ACTIVO + RIT
promactiv1 = promedio(resactiv1, resactiv2)
promactiv2 = promedio(resactiv2, resactiv3)
rit1 = RIT(resnet1, respasivo1, promactiv1)
rit2 = RIT(resnet2, respasivo2, promactiv2)
ritrend = tendencia(rit2, rit1)

#CALCULO DE APALANCAMIENTO
apalancamiento1 = rpn1 / rit1
apalancamiento2 = rpn2 / rit2
apatrend = tendencia(apalancamiento2,apalancamiento1)

#CALCULO DEL PASIVO + TFP
prompasivo1 = promedio(respasiv1,respasiv2) 
prompasivo2 = promedio(respasiv2, respasiv3)
tfp1 = TFP(respasivo1,prompasivo1) #SE USA EL RESULTADO GENERADO NO EL TOTAL DEL PASIVO!!
tfp2 = TFP(respasivo2,prompasivo2)
tfptrend = tendencia(tfp2,tfp1)

#PUNTO DE EQUILIBRIO433
equilibrium1 = puntoequilibrio(costofijo1,costovar1,ventas1)
equilibrium2 = puntoequilibrio(costofijo2,costovar2,ventas2)
equitrend = tendencia(equilibrium2,equilibrium1)

#MARGEN DE SEGURIDAD
margensegu1 = margenseg(ventas1, equilibrium1)
margensegu2 = margenseg(ventas2, equilibrium2)
margetrend = tendencia(margensegu2,margensegu1)

#MARGEN DE CONTRIBUCIÓN
margencontribucion1 = contribucion(costovar1,ventas1)
margencontribucion2 = contribucion(costovar2,ventas2)
contrend = tendencia(margencontribucion2,margencontribucion1)

#MARGEN DUPON
dupomarg1 = margdupon(resnet1,respasivo1,ventas1)
dupomarg2 = margdupon(resnet2,respasivo2,ventas2)
dupotrend = tendencia(dupomarg2,dupomarg1)

#ROTACION
rota1 = rotacion(ventas1,promactiv1)
rota2 = rotacion(ventas2,promactiv2)
rotatrend = tendencia(rota2,rota1)

# FIN DE CALCULOS

# IMPRESIÓN DE RESULTADOS
print("El RPN de x1 es", round(rpn1,2), "y el RPN de x2 es", round(rpn2,2), "La tendencia es", round(repntrend,2))
print("El RIT para x1 es", round(rit1,2),"y el RIT para x2 es",round(rit2,2),"La tendencia es de", round(ritrend,2))
print("El apalancamiento para x1 es", round(apalancamiento1,2),"y el apalancamiento para x2 es", round(apalancamiento2,2), "La tendencia es", round(apatrend,2))
print("La TFP para x1 es",round(tfp1,2),"y la TFP para x2 es",round(tfp2,2), "La tendencia es",round(tfptrend,2))
print("El punto de equilibrio para x1 es", round(equilibrium1,2), "y el punto de equilibrio para x2 es", round(equilibrium2,2), "La tendencia es",round(equitrend,2))
print("El margen de seguridad para x1 es",round(margensegu1,2),"y el margen de seguridad para x2 es",round(margensegu2,2),"La tendencia es",round(margetrend,2))
print("El margen de contribucion para x1 es", round(margencontribucion1,2),"y el margen de contribucion para x2 es", round(margencontribucion2,2),"La tendencia es",round(contrend,2))
print("El margen sobre ventas de Dupon para x1 es", round(dupomarg1,2),"y el margen sobre ventas Dupon para x2 es",round(dupomarg2,2),"La tendencia es",round(dupotrend,2))
print("La rotación para x1 es",round(rota1,2), "y la rotacion para x2 es",round(rota2,2),"La tendencia es",round(rotatrend,2))
