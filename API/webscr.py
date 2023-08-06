from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
#from selenium.common.exceptions import *



class main:
	def setError(self, msg, e):
		self.error = e
		self.errorMsg = msg
	def limpiarError(self):
		self.error = ""
		self.errorMsg = ""
	def cerrar(self):
			if self.error : print(self.error)
			self.navegador.close()
			self.navegador.quit()
	def __init__(self):
		self.limpiarError()
		try:
			##CAMBIAR EL DRIVER POR chromedriver (Chrome es el navegador mas comun)
			self.navegador = webdriver.Firefox()
			self.navegador.set_page_load_timeout(6) #si en 6 segundos no responde, morir
			self.navegador.get("https://www.saes.esfm.ipn.mx/")
		except Exception as e:
			self.setError("El SAES no responde, (offline?)", e)
			self.cerrar()
	def get_captcha(self):
		self.limpiarError()
		try:
			captcha = WebDriverWait(self.navegador, 10).until(EC.visibility_of(self.navegador.find_element(By.CLASS_NAME, 'LBD_CaptchaImage')))
			captchab64 = captcha.screenshot_as_base64
		except Exception as e:
			print("error captcha")
			self.setError("Hubo un error al obtener el captcha del SAES", e)
			self.cerrar()
			return
		return captchab64
	def login(self, boleta="", password="", captcha=""):
		self.limpiarError()
		if(boleta == "" or password == "" or captcha == ""):
			self.setError("Informacion incompleta", None) #regresar a la fila?
			self.cerrar()
			return
		try: #Intentar escribir datos de acceso
			self.navegador.find_element(By.ID, 'ctl00_leftColumn_LoginUser_UserName').send_keys(boleta)
			self.navegador.find_element(By.ID, 'ctl00_leftColumn_LoginUser_Password').send_keys(password)
			self.navegador.find_element(By.ID, 'ctl00_leftColumn_LoginUser_CaptchaCodeTextBox').send_keys(captcha)
			self.navegador.find_element(By.ID, "ctl00_leftColumn_LoginUser_LoginButton").click()
		except Exception as e:
			self.setError("Hubo un error al intentar usar tus credenciales.", e) #regresar a la fila?
			self.cerrar()
			return False
		try: #Verificar si el login fue exitoso, o no
			elem = WebDriverWait(self.navegador, 15).until(EC.any_of( #verificar si el inicio de sesion fue exitoso (o no)
				EC.presence_of_element_located((By.ID, "ctl00_mainCopy_FormView1")),
				EC.visibility_of_element_located((By.XPATH, "/html/body/form/div[3]/div[3]/div[1]/div[2]/div/div[2]/div/anonymoustemplate/table/tbody/tr/td/span"))
			))
			if(elem.tag_name == "span"): #no se pudo :(
				#leer el mensaje de error
				s = bs(elem.get_attribute("innerHTML"), features="html.parser")
				self.setError(s.get_text(" ", strip=True), None)
				self.cerrar()
				return False
			else: # we're in
				return True
		except Exception as e:
			self.setError("Hubo un error al determinar si el inicio de sesion fue correcto o no.", e)
			self.cerrar()
			return False
	def leer_datos(self):
		#ctl00_mainCopy_FormView1_nombrelabel    -> Nombre completo
		return None