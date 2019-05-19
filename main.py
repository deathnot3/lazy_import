from importlib import import_module

def da_paja_importar(module_name):
	try:
		module = import_module(module_name)

	except ImportError:
		print("Che ese modulo no existe")

	else:
		globals()[module_name] = module

da_paja_importar('math')

print(math.sqrt(4))
