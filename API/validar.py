import re

MAX_STR_SIZE = 200


class main:
	def validarYconvertir(self, dato, tipo, d_size=MAX_STR_SIZE):
		if not isinstance(dato, str):return None
		if(len(dato)>MAX_STR_SIZE):return None
		match(tipo):
			case "int":
				if dato.isdigit():
					dato = int(dato)
					return dato if dato <= d_size else None
				return None
			case "txt":
				return None if self.reText.search(dato) == None else dato
			case "mail":
				return None if self.reMail.search(dato) == None else dato
			case "float":
				if dato.replace(".", "", 1).isdigit():
					return float(dato)
				return None
	#def validarBoletaAlumno(self, num):
	def __init__(self):
		self.reText = re.compile(r"^[a-zA-Z| áéíóúÁÉÍÓÚ]+$", flags=0)
		self.reMail = re.compile(r"^[\w\-\.]+@([\w-]+\.)+[\w-]{2,4}$", flags=0)
		#self.reMailIPN = re.compile(r"" ,flags=0)



