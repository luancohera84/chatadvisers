# Script  actulizacion repositorios Dev  => Prod
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Ejecucion python3 git.py  -n <Nombre> -s <seudonimo>


import os
import argparse

nombre = ''
seudonimo = ''


def menu(pos):
	os.system('clear')
	print ('##########   SELECCIONE UNA OPCION    ##########')
	print ('\t( 1 ) Ver el Estado')
	print ('\t( 2 ) Ver el log')
	print ('\t( 3 ) Listar ramas')
	print ('\t( 4 ) Cambiar de rama')
	print ('\t( 5 ) Generar commit')
	print ('\t( 6 ) Realizar un push')
	print ('\t( 7 ) Realizar un merge')
	print ('\t( 8 ) Crear una rama')
	print ('\t( 9 ) Eliminar una rama')
	print ("\t( 0 )  Salir")


def continuar():
	input('\n\nPERSIONE ENTER PARA CONTINUAR')
	

def estado():
	os.system('clear')
	print ('##########   ESTADO DEL REPOSITORIO    ##########\n\n')
	os.system('git status')
	continuar()
	

def log():
	os.system('clear')
	print ('##########   ULTIMOS 10 COMMITS GENERADOS    ##########\n\n')
	os.system('git log -10 --oneline')
	continuar()
	

def listar_ramas():
	os.system('clear')
	print ('##########   LISTA DE RAMAS    ##########\n\n')
	os.system('git branch -a')
	continuar()
	

def cambiar_rama():
	os.system('clear')
	print ('##########   CAMBIAR DE RAMA    ##########\n\n')
	os.system('git branch')
	rama = input("\n\nIngrese una rama o ( q ) para cancelar: ")
	if rama != 'q':
		os.system('git checkout '+rama)
		pass
	continuar()
	

def commit(nombre):
	os.system('clear')
	print ('##########   GENERAR UN COMMIT    ##########\n\n')
	rama = input("\n\nEnter para continuar con el commit o ( q ) para cancelar: ")
	if rama != 'q':
		app = input("Ingrese la aplicacion (web/movil): ")
		tipo = input("Ingrese el tipo: ")
		msj = input("Ingrese el mensaje: ")
		os.system('git add --all')
		os.system("""git commit -am '{"aplicacion": "%s","responsable": "%s","tipo": "%s", "msj": "%s"}' """ %(app,nombre,tipo,msj))
		pass
	continuar()
	

def push(seudonimo):
	os.system('clear')
	print ('##########   REALIZAR UN PUSH    ##########\n\n')
	rama = input("\n\nEnter para realizar el push con la rama %s o ( q ) para cancelar: " %(seudonimo))
	if rama != 'q':
		os.system('git push origin %s' %(seudonimo))
		pass
	continuar()
	

def salir():
	os.system('clear')
	print ('##########   SALIR    ##########\n\n')
	os.system('clear')
	

def merge():
	os.system('clear')
	print ('##########   REALIZAR UN MERGE    ##########\n\n')
	os.system('git branch')
	rama = input("\n\nIngrese la rama a unir o ( q ) para cancelar: ")
	if rama != 'q':
		os.system('git merge '+rama)
		pass
	continuar()

def crear_rama():
	os.system('clear')
	print ('##########   CREAR UNA RAMA    ##########\n\n')
	os.system('git branch')
	rama = input("\n\nIngrese el nombre de la nueva rama o ( q ) para cancelar:  ")
	if rama != 'q':
		os.system('git checkout -b '+rama)
		pass
	continuar()

def eliminar_rama():
	os.system('clear')
	print ('##########   ELIMINAR UNA RAMA    ##########\n\n')
	os.system('git branch')
	rama = input("\n\nIngrese el nombre de la rama a eliminar o ( q ) para cancelar: ")
	if rama != 'q':
		os.system('git branch -d '+rama)
		pass
	continuar()



parser = argparse.ArgumentParser()

parser.add_argument("-n", "--nombre", help="Nombre de la persona que esta trabajando")
parser.add_argument("-s", "--seudonimo", help="seudonimo de la persona que esta trabajando, generalmente se trata del primer nombre en minuscula")
args = parser.parse_args()
os.system('clear')
print('args.nombre',args.nombre)

if args.nombre:
	nombre = args.nombre
else:
	nombre = input("\n\nIngrese un Nombre, Nombre de la persona que esta trabajando: ")
	pass

if args.seudonimo:
	seudonimo = args.seudonimo
else:
	seudonimo = input("\n\nIngrese un Seudonimo, generalmente se trata del primer nombre en minuscula: ")
	pass


os.system('clear')

print ("""
####################################################################################
##########                                                                ##########
##########                        RAMAS ACTUALES                          ##########
##########                                                                ##########
####################################################################################
""")
os.system('git branch')
print ('\n\n')
print ("""
####################################################################################
##########                                                                ##########
##########                 ESTADO ACTUAL DEL REPOSITORIO                  ##########
##########                                                                ##########
####################################################################################
""")
os.system('git status')
pos = 1
continuar()


while True:
	# Mostramos el menu
	menu(pos)
	opcionMenu = input("\n\tDigita la opcion deseada >> ")
	print (opcionMenu)
	if opcionMenu=='1': # VER EL ESTADO DEL REPOSITORIO
		estado()
	elif opcionMenu=='2': # VER EL LOG
		log()
	elif opcionMenu=='3': # LISTAR RAMAS
		listar_ramas()
	elif opcionMenu=='4': # CAMBIAR DE RAMA
		cambiar_rama()
	elif opcionMenu=='5': # GENERAR COMMIT1
		commit(nombre)
	elif opcionMenu=='6': # REALIZAR UN PUSH
		push(seudonimo)
	elif opcionMenu=='7': # REALIZAR UN MERGE
		merge()
	elif opcionMenu=='8': # CREAR UNA RAMA
		crear_rama()
	elif opcionMenu=='9': # ELIMINAR UNA RAMA
		eliminar_rama()
	elif opcionMenu=='0': # SALIR
		salir()
		break