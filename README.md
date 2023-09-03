# API-SAES
API para simplificar el llenado de la hoja de inscripcion para alumnos de la ESFM

# Server

[TODO: Documentar el uso del server de python, dependencias vm etc,]

### Requerimientos
[TODO: Implementar compatibilidad con navegadores basados en Chromium]
 - Python >= 3.11
 - Firefox >= 100.0
 - geckodriver

### Intalacion
[TODO]
Descarga o clona este repositorio :)

### Instalar dependencias
```bash
$ pip3 install -r requirements.txt
```

# UI

Para poder ejecutar una vista previa de la UI es necesario tener instalado flutter y ejecutar el siguiente comando:

```bash
$ cd apiui
$ flutter create .
$ flutter run 
```

# TODO:

Entre las tareas pendientes tenemos:

- [ ] Crear calendario o lineamientos para contribucion (contribute.md)
- [ ] https://github.com/cpesfm/API-SAES/issues/1
- [ ] https://github.com/cpesfm/API-SAES/issues/2
- [ ] https://github.com/cpesfm/API-SAES/issues/3
- [ ] Crear contenedores docker para cada version estable del proyecto
- [ ] Generar `releases` de cada version estable
- [ ] Alojar el servicio en la nube 

# Tecnologias propuestas

- web scrapping con python
- Generacion del pdf con python
- Firebase para alojar web app
- Flutter para cross platform app
