
-----main.py
si main.py se ejecuta sin ningun argumento:
	preguntar si ejecutar en modo privado [solo esta compu puede acceder al servidor web/ 127.0.0.1]
	o en modo publico [todas las maquinas de la red pueden ver el server web/ 0.0.0.0]
siNo:
	leer los argumentos pasados desla la CLI

----WEB/main.py
interfaz web para la API y el generador de pdf
1. index.html: mostrar deslinde de responsabilidad y pasos a seguir (iniciar sesion, corregir datos, generar y descargar)
2. el usuario mete sus datos y da click en comenzar
3. web/main manda la informacion a api/main. api/main carga una instancia de chrome para entrar al saes.
4. api/main le regresa a web/main -> usuario el captcha (mostar cuenta regresiva de 20 seg)
5 web/main manda el captcha del usuario a api/main


----API/main.py
acceder al saes con selenium y extraer la info con bs4