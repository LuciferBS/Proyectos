#!/usr/bin/python3

# guardar en la carpeta del proyecto
# X:\laragon\www\DWY4001_19_s03_HolaMundo
# con el nombre 'ejemplo_funciones.py'

# las funciones en python se definen con def :

def funcion_tonta(nombre) :
	separador = " "	
	mensaje = separador.join(("Oh", "El tonto de" , nombre))
	print(mensaje)

# una funcion un poco mas compleja: calculo del digito
# verificador de un rut chileno. Use solo tabs, no espacios
def digito_verificador(rut):
	digito = ""
	contador = 2
	suma = 0
	multiplo = 0
	while rut > 0:
		multiplo = ( rut % 10 ) * contador
		suma = suma + multiplo
		rut = rut // 10 # division entera!
		contador = contador + 1
		if contador == 8 :
			contador = 2
	digito = 11 - (suma % 11)
	if digito == 10:
		digito = 'k'
	if digito == 11 :
		digito = 0
	return str(digito)	


mi_rut = 12656568
print("-".join((str(mi_rut), digito_verificador(mi_rut))))







# y llamamos a la funcion...
funcion_tonta("Rafael") # en honor de Rafael Alberti
funcion_tonta("Daniel")

# Para que los cambios se guarden en github master...
# git add ejemplo_funciones.py
# git commit -m "Agregamos ejemplo funciones"
# git checkout master
# git pull
# git merge dm_ejemplo_funciones
# git push

