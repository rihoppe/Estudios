import jsonReader
import os

def cargar(name, path = None):
	current_path = os.getcwd()
	if path:
		new_path = current_path + '/' + path
		os.chdir(new_path)
	probando = jsonReader.jsonToDict(name)
	os.chdir(current_path)
	return probando
	
	
#a = cargar('gyms.json', 'data')
#a = jsonReader.jsonToDict(a)
#print(a)

def guardar(name, data, path = None):
	current_path = os.getcwd()
	if path:
		new_path = current_path + '/' + path
		os.chdir(new_path)
	probando = jsonReader.dictToJson(name, data)
	os.chdir(current_path)
	return probando


class programon:
	def __init__(self, id, nombre, tipo, evolve_to, hp, sp_defence, defence, attack, sp_attack, speed, moves, evolve_lvl, current_lvl = 1, salvaje = True):
		self._id = id
		self.nombre = nombre
		self.tipo = tipo
		self.current_lvl = current_lvl
		self.evolve_to = evolve_to
		self.hp = hp
		self.sp_defence = sp_defence
		self.defence = defence
		self.attack = attack
		self.sp_attack = sp_attack
		self.speed = speed
		self.moves = moves
		self.evolve_level = evolve_lvl
		self.salvaje = salvaje
		self.current_hp = hp
	def evolve():
		if self.current_lvl == self.evolve_lvl:
			print(0)
			
class prograbola:
		print('prograbola')

class caja_medallas():
		nombres_medallas = {1:'medalla pucon city',
							2:'medalla villarica city',
							3:'medalla santiago city',
							4:'medalla maitencillo city',
							5:'medalla tongoy city'}
		def __init__(self, diccionario = None):
			if diccionario:
				self.lista = diccionario
			else:
					self.lista = {}
					for i in range(8):
						i += 1
						self.lista[i] = False
		def obtener_medalla(self, num_medalla):
			self.lista[str(num_medalla)] = True
			print('felicidades ahora posees la medalla {}'.format(self.nombres_medallas[num_medalla]))
		
class progradex():
				
		def __init__(self, diccionario = None):
			'''funcion que crea una progradex vacia o carga una existente si se le entrega un id correcto
			'''
			if diccionario:
				self.lista = diccionario
			else:
				self.lista = {}
		
		def agregar(self, id_programon, status):
					self.lista[id_programon] = status

class jugador(progradex, caja_medallas):
	def __init__(self, admin = False):
			if admin:
				self._id = '0'
				self.nombre = 'admin'
				self._password = 'admin_pass'
				self.dinero = 1000000
				self.dex = progradex()
				self.medallas = caja_medallas()
			else:
				self.jugadores = cargar('jugadores.json', 'data')
				self.last_id = 2
				for i in self.jugadores:
					if int(i) > self.last_id:
						self.last_id = int(i)
				print(self.last_id)
				self.opciones = {'1': self.nuevo_usuario,
							'2': self.usuario_existente}
				self.nombre_no_ocupado = True
				self.run()
	def run(self):
		estado = True
		while estado:
			eleccion = input('1-Nuevo usuario	2-usuario existente \nrespuesta:\t')
			accion = self.opciones.get(eleccion)
			if accion:
				s = accion()
				estado = False
			else:
				print ('opcion invalida')
				
	def login_jugador(self):			
				opciones_2 = {'1':self.usuario_existente, '2':self.run}
				nombre = input('nombre: \t')
				password = input('contrasena: \t')
				for i in self.jugadores:
					if nombre == self.jugadores[i]['nombre'] and self.jugadores[i]['contrasena'] == password:
						print ('login exitoso')
						return True, i
				print('usuario o contrasena incorrectos')
				estado = True
				while estado:
					eleccion_2 = input('1-reintentar	2-volver \nrespuesta: \t')
					accion_2 = opciones_2.get(eleccion_2)
					if eleccion_2 == '1':
						s = accion_2()
					elif eleccion_2 == '2':
						estado = False
						return False,'string para evitar error al volver'
					else:
						print ('opcion invalida')
	def nuevo_usuario(self):
			nombre = input("seleccione el nombre: \t")
			while self.nombre_no_ocupado:
				if nombre in self.jugadores:
					print('nombre ya ocupado')
					nombre = input("seleccione el nombre: \t")
				else:
					self.nombre_no_ocupado = False
			password = input("seleccione la contrasena: \t")
			self.last_id += 1
			self._id = self.last_id
			self.nombre = str(nombre)
			self._password = str(password)
			self.dinero = 1000
			self.dex = progradex()
			self.medallas = caja_medallas()
			print(self.jugadores)
			new_player = {'nombre':self.nombre, 'contrasena':self._password, 'dinero':self.dinero,
			'progradex':self.dex.lista, 'medallas':self.medallas.lista}
			print(new_player)
			self.jugadores[self._id] = new_player
			guardar('jugadores.json', self.jugadores, 'data')
			print(self.jugadores)
			
			
	def usuario_existente(self):
			carga = self.login_jugador()
			if carga[0]:
				print('cargando datos')
				datos_cargados = self.jugadores[carga[1]]
				for i in self.jugadores:
					self.last_id = i
				self._id = carga[1]
				self.nombre = datos_cargados['nombre']
				self._password = datos_cargados['contrasena']
				self.dinero = datos_cargados['dinero']
				self.dex = progradex(datos_cargados['progradex'])
				self.medallas = caja_medallas(datos_cargados['medallas'])
				print('cargado exitoso.\nBienvenido {}.'.format(self.nombre))
			else:
				self.run()	

s = jugador()
print(s.dex.lista)
s.dex.agregar('2', 'capturado')
print(s.dex.lista)
print (s.medallas.lista)
s.medallas.obtener_medalla(1)
print(s.medallas.lista)
print(s.jugadores)

def eleccion_archivos(path = None):
	'''funcion que toma el direcctorio actual o uno dado, imprime los archivos existentes en dicho directorio
	y luego retorna un archivo a eleccion
	'''
	if path:
		if '/' in path:
			current_path = os.getcwd()
			os.chdir(path)
		else:
			current_path = os.getcwd()
			new_path = current_path + '/' + path
			os.chdir(new_path)
	archivos = os.listdir()
	lista = {}
	string = ''
	conteo = 0
	for i in range(len(archivos)):
		if archivos[i] != '__pycache__' and archivos[i] != 'data':
			lista[i+1] = archivos[i]
			if conteo != 1:
				string += '{0}- {1:{width}} \t \t'.format(str(i+1), str(archivos[i]), width = 20)
				conteo += 1
			else:
				string += '{0}- {1:{width}} \n'.format(str(i+1), str(archivos[i]), width = 20)
				conteo = 0
	print (string)
	eleccion = input('elija el achivo:\t')
	print(eleccion)
	return lista.get(int(eleccion))

#a = open(str(eleccion_archivos('data')), 'r')
#print(a)
#archivo = os.listdir()

def sistema():
	
	
	while True:
		print (0)
'''			
jugadores = {1:{'nombre':'rai', 'contrasena':'italia', 'dinero':5000, 'progradex':{1:'capturado', 2:'visto'}, 'medallas':{1:True, 2:True, 3:True, 4:True, 5:True, 6:True, 7:True, 8:True}},
				2:{'nombre':'pepe', 'contrasena':'hola', 'dinero':1000, 'progradex':{3:'capturado'}, 'medallas':{1:False, 2:False, 3:False, 4:False, 5:False, 6:False, 7:False, 8:False}}}
#jsonReader.dictToJson('jugadores', jugadores)
guardar('jugadores.json', jugadores, 'data')
'''
