#PERRO NEGRO

nombreCliente=input("cual es su nombre? ")
paisCliente=input("Cual es su pais? ")
cantidadPersonas=int(input("cuantas personas van a reservar? "))
añoNacimiendoCliente=int(input("en que año nacio? "))

#recalcular la edad del cliente
añoActual=2024
edadCliente=añoActual-añoNacimiendoCliente

#clasificar, preguntar, decidir

if edadCliente >= 18 :
     #tab es lo que viene a replazar las llaves
    print("Usted es mayor de edad")
else:
    print("usted es mayor de menor de edad")