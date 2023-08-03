from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import *



class saes:
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
			wait = WebDriverWait(self.navegador, 4)
			captcha = wait.until(EC.visibility_of(self.navegador.find_element(By.CLASS_NAME, 'LBD_CaptchaImage')))
			#captcha = self.navegador.find_element(By.CLASS_NAME, 'LBD_CaptchaImage')
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
			self.setError("Informacion incompleta", "---") #regresar a la fila?
			self.cerrar()
			return
			try:
				self.navegador.find_element(By.ID, 'ctl00_leftColumn_LoginUser_UserName').send_keys(boleta)
				self.navegador.find_element(By.ID, 'ctl00_leftColumn_LoginUser_Password').send_keys(password)
				self.navegador.find_element(By.ID, 'ctl00_leftColumn_LoginUser_CaptchaCodeTextBox').send_keys(captcha)
				#self.navegador.find_element(By.ID, "ctl00_leftColumn_LoginUser_LoginButton").click()
			except Exception as e:
				self.setError("Hubo un error al intentar enviar tus credenciales.", e) #regresar a la fila?
				self.cerrar()
				return
			elem = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.ID, "Element_to_be_found")) #This is a dummy element
)


#r = {"type":0,"msg":""} #0:error  1:imagen/base64 

def conectar_saes():
	#esperar a que la pagina del saes rederize
	#hacer screenshot del captcha
	#mandarlo al cliente
	driver = webdriver.Firefox(timeout=10) #iniciar navegador con timeout de 10s
	driver.get("https://www.saes.esfm.ipn.mx/")
	captcha = driver.find_element(By.CLASS_NAME, 'LBD_CaptchaImage')
	print(captcha.screenshot_as_base64)

	driver.quit()

	saes_form = driver.find_element(By.ID, 'ctl00_leftColumn_LoginUser_UserName')
	saes_form.send_keys("boleta")
	saes_form = driver.find_element(By.ID, '')
	saes_form.send_keys("password")
	saes_form.send_keys("captcha")
#except NoSuchElementException as e:
#	print("error")
#finally:
#	if(r["error"]>0):
#		print(r["msg"])
#		driver.quit()
	#return r

#saes = API.saes()
#saes = saes()
#print(saes.error)
