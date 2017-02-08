class postit:
	
	last_id = 0
	
	def __init__(self, mensaje, tags = ''):
		self.mensaje = mensaje
		self.tags = tags
		self.id = postit.last_id
		postit.last_id += 1
	
	def match(self, keyword):
		return keyword in self.mensaje or keyword in self.tags

#s = postit('hello world','frase')
#print(s.mensaje,s.tags)

class panel:
	
	def __init__(self):
		self.postit_dict = {}
	
	def nuevo_postit(self, mensaje, tags):
		s= postit(mensaje, tags)
		self.postit_dict.update({s.id : s})

	def modificar_mensaje(self, id, nuevo_mensaje):
		self.postit_dict[id].mensaje = nuevo_mensaje
	
	def modificar_tags(self,id,nuevos_tags):
		self.postit_dict[id].tags = nuevos_tags
	
	def buscar_postit(self, keyword):
		return [p for p in self.postit_dict.values() if p.match(keyword)]

	def display(self, keyword=None):
		result = []
        if keyword is not None:
            result = [p for p in self.buscar_postit(keyword)]
        else:
            result = self.postit_dict

        for p in result:
            print("post it {0}: \n Mensaje: {1} \n Tags: {2}".format(p._id, p.mensaje, p.tags))



'''holo = {}
holo.update({'comida':'carne'})
holo.update({'no comida':'plastico'})
print holo
print holo['comida']
print holo.values()
'''

'''p = panel()
p.nuevo_postit('hello world','frase')
p.nuevo_postit('putos','insulto')
p.nuevo_postit('hola mundo','frase')
p.nuevo_postit('qlio','insulto')
p.nuevo_postit('hola wn','frase')
print p.buscar_postit('hola')
'''
print 'hola'
