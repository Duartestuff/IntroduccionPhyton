#condiciones multiples

sensorNivelAgua=int(input("Digite el nivel de aua de la represa: "))

#si la represa esta en 0 metros 150 no oper
#si esta entre 150 y 400 opera normla
#si esta en 400 y 420 esta en riesgo pero opero
#si esta por encima de 420 peligro y deja de operar 

print(f"El nivel de agua es: {sensorNivelAgua}")
if sensorNivelAgua > 0 and  sensorNivelAgua <=150:
    print("muy poca agua las puertas estan cerradas ")
elif sensorNivelAgua > 150 and sensorNivelAgua <=400:
    print("El agua es adecuado, se opera normalmmente")
elif sensorNivelAgua > 400 and sensorNivelAgua <= 420:
    print("El nivel de agua se acerca al limite peligrosos, aun se opera con normalidad")
elif sensorNivelAgua < 420:
    print("Niveles por ensima de lo adecuado, peligro")
else:
    print ("revise el sensor, medidad no valida")
#los swich consumen muchos siclos de procesamiento, investigar el operador ternario, cada vez que vos programes debe buscar como evitar una linea repetida
#
