import time


#sys.path.append('../API')
from API import main as saes


from random import randint
from flask import Flask, render_template, request, Response, make_response, abort, jsonify
from markupsafe import escape

app = Flask(__name__)

class _fila:
	def __init__(self):
		self.gID = 0
		self.clientes = {}
	def generarID(self, n=3):
		q = ""
		for o in range(0,n):
			p = randint(42,57) if randint(0,1) % 2 == 0 else randint(97,122) if randint(0,1) % 2 == 1 else randint(63, 90)
			q += chr(p)
		return q
	def agregar(self):
		print("add")
		self.update()
		self.gID += 1
		id = self.generarID(10)
		self.clientes[id] = [self.gID, time.time()]
		return id

	def eliminar(self, id):
		del self.clientes[id]
		self.gID -= 1
		self.update()

	def pos(self, id):
		self.update()
		return self.clientes[id][0]

	def update(self):
		eph = time.time()-10
		tmp = [0, 0, 0] #ordenar, apartir de, restar
		for cliente in self.clientes:
			if self.clientes[cliente][1] <= eph: #quitar a los que su epoch sea mas antiguo a 10 seg
				self.gID -= 1
				tmp = [1, self.clientes[cliente][0], tmp[2]+1] if (self.clientes[cliente][0] < tmp[1]) else [1, tmp[1], tmp[2]+1]
				del self.clientes[cliente]
		if tmp[0]:
			for cliente in self.clientes:
				if self.clientes[cliente][0] >= tmp[1]:
					self.clientes[cliente][0] = self.clientes[cliente][0] - tmp[2]
		
fila = _fila()


@app.route('/xhr', methods = ['POST', 'GET'])
def index_login():
	if request.method == 'POST':
		if(request.headers.get("Content-Type") == "application/json"):
			data = request.json
		else:
			abort(500, description="Request invalido")
		#msg = {"err":0, "tipo":"txt","data":""} #err:1, mostrar reintantar
		if "id" in data:
			if not (data.get("id") in fila.clientes):
				abort(530, "Tiempo limite de espera alcanzado. Intentalo de nuevo.")
			match data.get("req"): ##PONER UN MATCH-CASE PARA VALIDAR CAPTCHA RECIBIDO
				case "alive":
					print("======1")
					lugar = fila.pos(data.get("id"))
					print(lugar)
					print("======2")
					if(lugar == 1):
						print("======3")
						nav = saes.saes()
						if nav.errorMsg:
							print("======4")
							fila.eliminar(data.get("id"))
							return jsonify({"err":1, "txt":nav.errorMsg}), 520
						imagen_captcha = nav.get_captcha()
						if nav.errorMsg:
							fila.eliminar(data.get("id"))
							return jsonify({"err":1, "txt":nav.errorMsg}), 520
						return jsonify({"img":"data:image/png;base64," + imagen_captcha}), 200
					else:
						return jsonify({"pos":lugar}), 530
				case "captcha":
					if( not (data.get("boleta") and data.get("password") and data.get("captcha")) ):
						fila.eliminar(data.get("id"))
						return jsonify({"error":"informacion de login incompleta"}), 505
					if(not (nav.login(boleta=data.get("boleta"), password=data.get("password"), captcha=data.get("captcha")))):
						fila.eliminar(data.get("id"))
						return jsonify({"error":nav.errorMsg}), 506
					#TODO: escribir en main.py la rutina para extraer la info necesaria
					r = make_response(render_template('editar.html'))
					return 
				case _ :
					print("default")
					return ""
		else:
			id = fila.agregar()
			return jsonify({"id":id}), 200
	else:
		abort(476)
	return ""

@app.route('/')
def pagina_principal():
	return app.send_static_file('login.html'), 200
	#r = make_response(render_template('login.html'))
	#return r, 200


@app.errorhandler(404)
def page_not_found(error):
	return "Not found :(", 404
	#return render_template("404.html"), 404


if __name__ == '__main__':
	#TODO: Implementar los argumentos debug y online
	# debug true/false : imprimir mensajes de error especificos
	# online true/false : el server sera visible en localhost o en una interfaz publica
	app.run(host="0.0.0.0", port=6969)