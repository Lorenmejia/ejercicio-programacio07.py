pizzeria = ["Pizza normal", "Pizza super suprema", "Pizza 4 estaciones", "Pizza Hawaiana", "Pizza de quezo y pepperoni", "Pizza napolitana"]
saludo = "Bienvenidos a ZiZi Pizza"


def imprimir_menu():
	print("1 Mostrar pizzeria")
	print("2 Eliminar pizzeria")
	print("3 Agregar pizzeria")
	print("4 Salir")
	valor = input(Ingrese el de la accion: ")
	return valor
	
	
def Mostrar_pizzeria():
	For pizzeria in pizzerias:
		print(pizzeria)
		
		
def eliminar_pizzeria():
	pizzeria = []


def agregar_pizzeria(valor_parametro):	
	pizzerias.append(valor_parametro)
	
	
Continuar = True


while continuar:
	#v_retornado = valor retornado
	v_retornado = imprimir_menu()
	if int(v_retonado) == 1:
		for pizzeria in pizzerias:
			print(pizzeria)
	elif int (v_retornado) == 2:
		pizzerias = []
	elif int (v_retornado) == 3:
		valor = input("Ingrese el producto a agregar: ")
		
		pizzerias.append(valor)
	elif int(v_retornado) == 4:
		continuar = False
		
	else:
		print("Opcion no controlada")