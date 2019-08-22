#***************************************************************************
#***********************************PRUEBA**********************************
#***************************************************************************

#Ejercicio 1: considere las deniminaciones tipicas de las monedas
#Guatemaltecas escriba una funncion que reciba un numero real positivo
def unidades(x):
      if x == 0:
            unidad = "0C"
      if x == 1:
            unidad = "5C"
      if x == 2:
            unidad = "10C"
      if x == 3:
            unidad = "25C"
      if x == 4:
            unidad = "50C"
      if x == 5:
            unidad = "75C"
      return unidad

def billetes(x):
      if x == 0:
            billetes = "Q1.oo"
      if x == 1:
            billetes = "Q5.00"
      if x == 2:
            billetes = "Q10.00"
      if x == 3:
            billetes = "Q20.00"
      if x == 4:
            billetes = "Q50.00"
      if x == 5:
            billetes = "100.00"
      if x == 6:
            billetes = "200.00"
      return billetes

def eje_1():
      n= int(input("Ingrese un valor a convertir: "))



#Ejercicio 2: suma del numero y su reflejo      
def eje_2(numero):
      invertir = str(numero)
      vuelta = invertir[::-1]
      total = int(vuelta)
      return total+numero

#Verificacion si es palindromo o machete
def eje_3(numero):
      invertir = str(numero)
      vuelta = invertir[::-1]
      total = int(vuelta)
      if total == numero:
            return ("El valor es palindromo")
      else:
            return ("El numero es machete")
