from importlib import import_module
import random

def lazy_import(module_name):
	"""Funcion para importar un modulo cuando sea necesario usarlo"""
	try:
		# Importamos el modulo con import_module y se lo asignamos a module
		module = import_module(module_name)

	except ImportError:
		print("Che ese modulo no existe")

	else:
		# Con esta linea de codigo le agregamos una clave mas al diccionario de globals y le asignamos como valor
		# la variable con el modulo que acabamos de importar con import_module()
		# De esta manera en lugar de escribir, por ejemplo, module.sqrt(4) al hacer lazy_import('math')
		# pasariamos a escribir math.sqrt(4)
		globals()[module_name] = module

if random.choice([True, False]):
	# Hacemos alguna que otra boludez
	print("Trabajando con algo")

else:
	# En este caso decidimos importar cualquier modulo. En este caso como ejemplo puede ser math
	lazy_import("math")
	
	print(math.sqrt(4))
	
