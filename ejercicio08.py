#Estilo de python Pep8
platillos = ["Pollo Tipico", "Pinchos", "Chuleta", "Lasagna", "Camarones Empanizados"]

pedidos = []


def imprimir_menu():
	print("1 Mostrar Platillos")
	print("2 Agrgar Pedido")
	print("3 Imprimir Pedidos")
	print("4 Eliminar Pedidos")
	print("5 Salir")

	valor = int(input("Escriba el numero de la accion que dea realizar"))
	return valor

def mostrar_platillos():
	print("Lista de platillos Disponible")

	for platillo in platillos:
		print(platillo)

def agregar_pedido():
	plato = input("Escribir el nombre del platillo que desea")
	cantidad = int(input("Escriba la cantidad de platillos que desea"))
	mesa = int(input("Escriba el numero de la mesa"))
	pedido = "{0}, cantidad: {1}, mesa: {2}".format(plato, cantidad, mesa)

	pedidos.append(pedido)

def mostrar_pedidos():
	print("Lista de pedidos pendientes")

	for pedido in pedidos:
		print(pedido)

def eliminar_pedido():
	pedidos = []
	print("Se eliminaron todos los pedidos")

def almacenar():
	f = open("pedido.txt", "w+")
	for pedido in pedidos:
		f.write("{0} \n".format(pedido))

continuar = True

while continuar:
	accion = imprimir_menu()
	if accion == 1:
		mostrar_platillos()
	elif accion == 2:
		agregar_pedido()
	elif accion == 3:
		mostrar_pedidos()
	elif accion == 4:
		eliminar_pedido()
	elif accion == 5:
		continuar = False
	elif accion == 0:
		almacenar()

	else: 
		print("Accion desconocida")
