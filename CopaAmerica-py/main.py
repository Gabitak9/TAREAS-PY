#!usr/bin/env python
# -*- coding: utf-8 -*-

import web
import os
import re
from funciones import *
from datetime import *
from definiciones import *
from web import form

#configuracion
web.config.debug = False

#direcciones utilizadas
urls = (
  '/', 'index',
  '/equipos/','equipos',
  '/partidos/','partidos',
  '/resultados/','resultados',
  '/marcador/','marcador',
  '/cuartos_de_final/','cuartos_de_final',
  '/semi_final/','semi_final',
  '/final/','final'

)

#ubicacion del sitio template
render = web.template.render('templates/')

#pagina home
class index:
    def GET(self):
        return str(render.header("index",nombre,iconos_header))+str(render.home(nombre,slogan))+str(render.footer())

#pagina de equipos
class equipos:
    def GET(self):
        data = {"equipo":"","grupo":""}
        return str(render.header("equipos",nombre,iconos_header))+str(render.equipos(grupos_copa_america,None,data))+str(render.footer())

    def POST(self):
        #se recibe la informacion del equipo y del grupo
        post_input = dict(web.input(_nethod='post'))
        del post_input["_nethod"]
        for llave, valor in post_input.items():
                post_input[llave] = str(valor)
        
        #Validamos si el equipo corresponde al grupo ingresado
        if self.validar(post_input):
            #Validamos si el equipo no estaba ingresado anteriormente
            if ingresar_equipos(post_input):
                return str(render.header("equipos",nombre,iconos_header))+str(render.postequipos(post_input))+str(render.footer())
            else:
                return str(render.header("equipos",nombre,iconos_header))+str(render.equipos(grupos_copa_america,"error",post_input))+str(render.footer())
        else:
            return str(render.header("equipos",nombre,iconos_header))+str(render.equipos(grupos_copa_america,"error",post_input))+str(render.footer())


    def validar(self,post):
        equipo = post["equipo"]!=""
        grupo = post["grupo"]!="Selecciona un grupo..."
        return equipo and grupo

#pagina partidos
class partidos:
    
    def GET(self):
        
        #obtenemos todos los equipos registrados en el sistema
        equipo = obtener_equipos()
        data = {"equipo1":"", "equipo2":""}
        return str(render.header("partidos",nombre,iconos_header))+str(render.partidos(equipo, None,data))+str(render.footer())

    def POST(self):
        #obtenemos todos los equipos registrados en el sistema
        equipo = obtener_equipos()
        #se recibe la informacion ingresada por el formulario
        post_input = dict(web.input(_nethod='post'))

        del post_input["_nethod"]
        for llave, valor in post_input.items():
                post_input[llave] = str(valor)
        

        #Validamos si es posible jugar un partido entre ambos equipos
        if self.validar(post_input):
            #Validamos si el partido no fue jugado anteriormente
            if (registrar_partidos(post_input)):
                return str(render.header("partidos",nombre,iconos_header))+str(render.postpartidos(post_input))+str(render.footer())
            else:
                return str(render.header("partidos",nombre,iconos_header))+str(render.partidos(equipo,"error",post_input))+str(render.footer())

        else:
            return str(render.header("partidos",nombre,iconos_header))+str(render.partidos(equipo,"error",post_input))+str(render.footer())


    def validar(self,post):
        
        if post["equipo1"] == "Selecciona un equipo...":
            return False

        if post["equipo2"] == "Selecciona un equipo...":
            return False

        if post["equipo1"] == post["equipo2"]:
            return False
        else:
            return True

#Pagina marcador
class marcador:

    def GET(self):
      
        data = {'equipo1':"",'equipo2':""}
        #Equipos ingresado al sistema que estan jugando un partido
        equipos = equipos_jugando()

        tupla1 = equipos["equipo1"]
        tupla2 = equipos["equipo2"]
        
        nombre1,_ = tupla1
        nombre2,_ = tupla2

        #nombre de los equipos
        nombres = nombre1,nombre2        

        #si no existen partidos en este momento
        if (nombre1 == "NULL" or nombre2 == "NULL"):
            return str(render.header("marcador",nombre,iconos_header))+str(render.sinpartidos())+str(render.footer())

        return str(render.header("marcador",nombre,iconos_header))+str(render.marcador(equipos,nombres,None,data))+str(render.footer())

    def POST(self):

        #Equipos ingresado al sistema que estan jugando un partido
        equipos = equipos_jugando() 

        tupla1 = equipos["equipo1"]
        tupla2 = equipos["equipo2"]

        nombre1,_ = tupla1
        nombre2,_ = tupla2

        #nombre de los equipos
        nombres = nombre1,nombre2        

        post_input = dict(web.input(_nethod='post'))
   
        del post_input["_nethod"]
        for llave, valor in post_input.items():
            post_input[llave] = equipos[llave][0],str(valor)
                
        if self.validar(post_input):
			#mostramos el tablero general con los resultados del partido
            actualizar_partidos(post_input)
            return str(render.header("marcador",nombre,iconos_header))+str(render.postmarcador(post_input))+str(render.footer())
        else:
            equipos = obtener_equipos()
            return str(render.header("marcador",nombre,iconos_header))+str(render.marcador(equipos,nombres,"error",post_input))+str(render.footer())


    def validar(self,post):
        if post["equipo1"] == "Goles actuales":
            return False
        if post["equipo2"] == "Goles actuales":
            return False

        if post["equipo1"][1] == "":
            return False
        if post["equipo2"][1] == "":
            return False

        return True


#pagina resultados
class resultados:

    def GET(self):
		#se actualiza la informacion de cada partido jugado
        actualizar_fecha()
		#obtenemos la informacion de los partidos para mostrar la tabla de posiciones
        tabla = tabla_de_posiciones()
        return str(render.header("index",nombre,iconos_header))+str(render.resultados(nombre,slogan,tabla))+str(render.footer())

class cuartos_de_final:

    def GET(self):
	    #obtencion de clasificados y registro de partidos de cuartos de final.
        cuarto_de_final()
		#enviamos fixture_final para mostrar la informacion en html
        return str(render.header("cuartos_de_final",nombre,iconos_header))+str(render.cuartos_de_final(nombre,slogan,fixture_final))+str(render.footer())


class semi_final:
    def GET(self):
	    #obtencion de clasificados y registro de partidos de cuartos de final.
        semi_finales()
        return str(render.header("semi_final",nombre,iconos_header))+str(render.semi_final(nombre,slogan,fixture_final))+str(render.footer())

class final:
    def GET(self):
	    #obtencion de clasificados y registro de partidos de cuartos de final.
        finales()
        return str(render.header("final",nombre,iconos_header))+str(render.final(nombre,slogan,fixture_final))+str(render.footer())


#pagina no encontrada
def notfound():
    return web.notfound(str(render.header("index",nombre,iconos_header))+str(render.notfound())+str(render.footer()))

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.notfound = notfound
    app.run()

