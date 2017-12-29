#INTEGRANTES
#
#
#

from definiciones import *

#Funcion que devuelve un diccionario con la informacion de los equipos que estan actualmente jugando un partido
#Si no existen equipos jugando, devuelve un diccionario con valores NULL
def equipos_jugando ():

    #leemos el archivo partidos.dat
    jugando = open("partidos.dat","r")
    
    partido = dict()

    for linea in jugando:
        linea = linea.strip().split(";")
        #si mi archivo no tiene partidos registrados
        if linea[0] == "NULL" :
            partido["equipo1"] = ("NULL","NULL")
            partido["equipo2"] = ("NULL","NULL")
            return partido
        
        else:  
            #obtenemos la informacion de los equipos
            equipo1 = linea[0]
            equipo2 = linea[1]
            goles1 = linea[2]
            goles2 = linea[3]

            partido["equipo1"] = (equipo1,goles1)
            partido["equipo2"] = (equipo2,goles2)

    jugando.close()
    return partido

#Funcion que actualiza la tabla de posiciones. Para ello, obtiene la infomacion registrada en detalle_partidos.dat
#y guarda el contenido en un diccionario que es tomado por main.py para mostrar la informacion en resultados.html

def tabla_de_posiciones ():

    tabla_de_posiciones = dict()

    #resultados del grupo1
    tabla_de_posiciones["Grupo A"] = []

    #resultados del grupo2
    tabla_de_posiciones["Grupo B"] = []

    #resultados del grupo3
    tabla_de_posiciones["Grupo C"] = []
    
    detalle_partidos = open("detalle_partidos.dat","r")
    grupos = open("grupos.dat","r")

    grupo = -1

    #leemos toda la informacion registrada en el detalle de los partidos.
    for linea in detalle_partidos:
        linea = linea.strip().split(";")
        grupos = open("grupos.dat","r")
        pais = linea[0]
        info = (linea[0],linea[1],linea[2],linea[3],linea[4],linea[5],linea[6],linea[7],linea[8])
        #obtenemos el grupo de pais que estamos obteniendo los datos
        for linea2 in grupos:
            linea2 = linea2.strip().split(";")
            if (linea2[0] == pais):
                grupo = linea2[1]
                tabla_de_posiciones[grupo].append(info)
        grupos.close()    
        grupo = str(grupo)

    detalle_partidos.close()
    grupos.close()
    return tabla_de_posiciones


def registrar_partidos (partido):
    #Se valida que ambos equipos pertenezcan al mismo grupo.
    if paises_por_grupo[partido['equipo1']] == paises_por_grupo[partido['equipo2']]:
        #Se valida que el equipo no juegue contra si mismo.
        if partido['equipo1'] != partido['equipo2']:
            #Se valida que el partido no haya sido jugado anteriormente.
            partido_actual = {partido['equipo1'], partido['equipo2']}
            archivo2 = open('resultados.dat', 'r')
            se_puede = True
            for linea in archivo2:
                c = linea.strip().split(';')
                partido_a_comparar = {c[0], c[1]}
                if partido_actual == partido_a_comparar:
                    se_puede = False
            archivo2.close()
            if se_puede == True:                    
                #Ya validada las 3 condiciones procedemos a ingresar el partido en el archivo partidos.dat.
                archivo = open('partidos.dat', 'w')
                partido_ingresado = [partido['equipo1'], partido['equipo2'], '0', '0']
                linea = ';'.join(map(str,partido_ingresado))+'\n'
                archivo.write(linea)
                archivo.close()
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def obtener_equipos ():
    #Del archivo grupos.dat procedemos a obtener el listado de equipos.
    archivo = open('grupos.dat', 'r')
    lista_de_equipos = []
    for linea in archivo:
        c = linea.strip().split(';')
        e = c[0]
        lista_de_equipos.append(e)
    return lista_de_equipos

def ingresar_equipos (equipo):
    archivo = open('grupos.dat', 'r')
    #Se crea una lista auxiliar con el fin de ver si un equipo ya fue ingresado anteriormente.
    lista_auxiliar=[]
    for linea in archivo:
        c = linea.strip().split(';')
        e = c[0]
        lista_auxiliar.append(e)
    archivo.close()
    if equipo['equipo'] not in lista_auxiliar:
        #Ahora se verifica que el equipo ingresado pertenezca a los equipos que disputan la Copa America.
        #Y que pertenezca al grupo correspondiente (De acuerdo al diccionario paises_por_grupo)
        if equipo['equipo'] in paises_por_grupo and equipo['grupo'] == paises_por_grupo[equipo['equipo']]:
            archivo = open('grupos.dat', 'a')
            archivo2 = open('detalle_partidos.dat', 'a')
            equipo_ingresado = (equipo['equipo'],equipo['grupo'])
            linea1 = ';'.join(map(str,equipo_ingresado))+'\n'
            archivo.write(linea1)
            archivo.close()
            equipo_ingresado2 = (equipo['equipo'], '0', '0', '0', '0', '0', '0', '0', '0',)
            linea2 = ';'.join(map(str,equipo_ingresado2))+'\n'
            archivo2.write(linea2)
            archivo2.close()
            return True
        else:
            return False

def actualizar_fecha ():
    #Se crea este diccionario con el fin de ir sumando y almacenando los resultados.
    diccionario_detalle_partidos = { 'Chile':[0,0,0,0,0,0,0,0],
    'Bolivia':[0,0,0,0,0,0,0,0],
    'Mexico':[0,0,0,0,0,0,0,0],
    'Ecuador':[0,0,0,0,0,0,0,0],
    'Uruguay':[0,0,0,0,0,0,0,0],
    'Paraguay':[0,0,0,0,0,0,0,0],
    'Argentina':[0,0,0,0,0,0,0,0],
    'Jamaica':[0,0,0,0,0,0,0,0],
    'Brasil':[0,0,0,0,0,0,0,0],
    'Colombia':[0,0,0,0,0,0,0,0],
    'Venezuela':[0,0,0,0,0,0,0,0],
    'Peru':[0,0,0,0,0,0,0,0]}
    archivo = open('resultados.dat', 'r')
    #Se procede a leer linea por linea el archivo resultados.dat y se van almacenando los resultados
    #en variables locales.
    for linea in archivo:
        resultado_obtenido = linea.strip().split(';')
        equipo1, equipo2, goles_equipo1, goles_equipo2 = resultado_obtenido
        puntaje_equipo1 = [0,0,0,0,0,0,0,0]
        puntaje_equipo2 = [0,0,0,0,0,0,0,0]
        if goles_equipo1 > goles_equipo2:
            puntaje_equipo1 = [1,1,0,0,int(goles_equipo1),int(goles_equipo2),int(goles_equipo1)-int(goles_equipo2),3]
            puntaje_equipo2 = [1,0,1,0,int(goles_equipo2),int(goles_equipo1),int(goles_equipo2)-int(goles_equipo1),0]
        elif goles_equipo1 < goles_equipo2:
            puntaje_equipo2 = [1,1,0,0,int(goles_equipo2),int(goles_equipo1),int(goles_equipo2)-int(goles_equipo1),3]
            puntaje_equipo1 = [1,0,1,0,int(goles_equipo1),int(goles_equipo2),int(goles_equipo1)-int(goles_equipo2),0]
        else:
            puntaje_equipo1 = [1,0,0,1,int(goles_equipo1),int(goles_equipo2),0,1]
            puntaje_equipo2 = [1,0,0,1,int(goles_equipo2),int(goles_equipo1),0,1]
        PJ_1, PG_1, PP_1, PE_1, GF_1, GC_1, DI_1, PTS_1 = puntaje_equipo1
        PJ_2, PG_2, PP_2, PE_2, GF_2, GC_2, DI_2, PTS_2 = puntaje_equipo2
        PJ_1_d, PG_1_d, PP_1_d, PE_1_d, GF_1_d, GC_1_d, DI_1_d, PTS_1_d = diccionario_detalle_partidos[equipo1]
        PJ_2_d, PG_2_d, PP_2_d, PE_2_d, GF_2_d, GC_2_d, DI_2_d, PTS_2_d = diccionario_detalle_partidos[equipo2]
        #Una vez obtenido los goles, puntajes, etc se procede a actualizar la informacion en el diccionario.
        diccionario_detalle_partidos[equipo1][0] = PJ_1 + PJ_1_d
        diccionario_detalle_partidos[equipo1][1] = PG_1 + PG_1_d
        diccionario_detalle_partidos[equipo1][2] = PP_1 + PP_1_d
        diccionario_detalle_partidos[equipo1][3] = PE_1 + PE_1_d
        diccionario_detalle_partidos[equipo1][4] = GF_1 + GF_1_d
        diccionario_detalle_partidos[equipo1][5] = GC_1 + GC_1_d
        diccionario_detalle_partidos[equipo1][6] = DI_1 + DI_1_d
        diccionario_detalle_partidos[equipo1][7] = PTS_1 + PTS_1_d
        diccionario_detalle_partidos[equipo2][0] = PJ_2 + PJ_2_d
        diccionario_detalle_partidos[equipo2][1] = PG_2 + PG_2_d
        diccionario_detalle_partidos[equipo2][2] = PP_2 + PP_2_d
        diccionario_detalle_partidos[equipo2][3] = PE_2 + PE_2_d
        diccionario_detalle_partidos[equipo2][4] = GF_2 + GF_2_d
        diccionario_detalle_partidos[equipo2][5] = GC_2 + GC_2_d
        diccionario_detalle_partidos[equipo2][6] = DI_2 + DI_2_d
        diccionario_detalle_partidos[equipo2][7] = PTS_2 + PTS_2_d
    archivo.close()
    archivo2 = open('detalle_partidos.dat', 'w')
    #Ahora se escribe la informacion del diccionario en el archivo detalle_partidos.dat tal como se solicita.
    for i, j in diccionario_detalle_partidos.items():
        pais = [i]
        puntos = j
        pais.append(';'.join(map(str,puntos)))
        linea_final = ';'.join(map(str,pais))+'\n'
        archivo2.write(linea_final)
    archivo2.close()
    return None

def actualizar_partidos (partido):
    #Se abre el archivo resultados.dat y se agrega el ultimo partido ingresado con su respectivo resultado
    archivo = open('resultados.dat', 'a')
    partido_final = (partido['equipo1'][0], partido['equipo2'][0], partido['equipo1'][1], partido['equipo2'][1])
    linea = ';'.join(map(str,partido_final))+'\n'
    archivo.write(linea)
    archivo.close()
    #Se reinicia la informacion de partidos.dat
    archivo2 = open('partidos.dat', 'w')
    archivo2.write('NULL')
    archivo2.close()
    return None

def cuarto_de_final ():
    detalle_partidos = open('detalle_partidos.dat', 'r')
    cuartos_final = open('cuarto_de_final.dat', 'w')
    A1, A2, B1, B2, C1, C2, ter1, ter2 = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', '3ero1', '3ero2']
    dicA = {}
    dicB = {}
    dicC = {}
    for linea in detalle_partidos:
        resultados = linea.strip().split(';')
        equipo,_,_,_,_,GF,_,DI,PTS  = resultados
        resultados_ocupar = PTS, DI, GF
        map(int,resultados_ocupar)
        grupo_equipo = paises_por_grupo[equipo]
        if grupo_equipo == 'Grupo A':
            dicA[equipo] = resultados_ocupar
        elif grupo_equipo == 'Grupo B':
            dicB[equipo] = resultados_ocupar
        elif grupo_equipo == 'Grupo C':
            dicC[equipo] = resultados_ocupar
    for a, b in dicA.items():
        equipo = a
        PTS, DI, GF = b
        A1, A2, terA, pts, di, gf = ['','','',0,0,0]
        if PTS > pts:
            A1 = equipo
            pts = PTS
        elif PTS == pts:
            if DI > di:
                A1 = equipo
                di = DI
            elif DI == di:
                if GF > gf:
                    A1 = equipo
                    gf = GF
        pts, di, gf = [0,0,0]
        if equipo != A1:
            if PTS > pts:
                A2 = equipo
                pts = PTS
            elif PTS == pts:
                if DI > di:
                    A2 = equipo
                    di = DI
                elif DI == di:
                    if GF > gf:
                        A2 = equipo
                        gf = GF
        pts, di, gf = [0,0,0]
        if equipo != A1 and equipo != A2:
            if PTS > pts:
                terA = equipo
                pts = PTS
            elif PTS == pts:
                if DI > di:
                    terA = equipo
                    di = DI
                elif DI == di:
                    if GF > gf:
                        terA = equipo
                        gf = GF
    for a, b in dicB.items():
        equipo = a
        PTS, DI, GF = b
        B1, B2, terB, pts, di, gf = ['','','',0,0,0]
        if PTS > pts:
            B1 = equipo
            pts = PTS
        elif PTS == pts:
            if DI > di:
                B1 = equipo
                di = DI
            elif DI == di:
                if GF > gf:
                    B1 = equipo
                    gf = GF
        pts, di, gf = [0,0,0]
        if equipo != B1:
            if PTS > pts:
                B2 = equipo
                pts = PTS
            elif PTS == pts:
                if DI > di:
                    B2 = equipo
                    di = DI
                elif DI == di:
                    if GF > gf:
                        B2 = equipo
                        gf = GF
        pts, di, gf = [0,0,0]
        if equipo != B1 and equipo != B2:
            if PTS > pts:
                terB = equipo
                pts = PTS
            elif PTS == pts:
                if DI > di:
                    terB = equipo
                    di = DI
                elif DI == di:
                    if GF > gf:
                        terB = equipo
                        gf = GF
    for a, b in dicC.items():
        equipo = a
        PTS, DI, GF = b
        C1, C2, terC, pts, di, gf = ['','','',0,0,0]
        if PTS > pts:
            C1 = equipo
            pts = PTS
        elif PTS == pts:
            if DI > di:
                C1 = equipo
                di = DI
            elif DI == di:
                if GF > gf:
                    C1 = equipo
                    gf = GF
        pts, di, gf = [0,0,0]
        if equipo != A1:
            if PTS > pts:
                C2 = equipo
                pts = PTS
            elif PTS == pts:
                if DI > di:
                    C2 = equipo
                    di = DI
                elif DI == di:
                    if GF > gf:
                        C2 = equipo
                        gf = GF
        pts, di, gf = [0,0,0]
        if equipo != C1 and equipo != C2:
            if PTS > pts:
                terC = equipo
                pts = PTS
            elif PTS == pts:
                if DI > di:
                    terC = equipo
                    di = DI
                elif DI == di:
                    if GF > gf:
                        terC = equipo
                        gf = GF
    fixture_final['P1'][0] = A1
    fixture_final['P2'][0] = A2
    fixture_final['P3'][0] = B1
    fixture_final['P4'][1] = B2
    fixture_final['P4'][0] = C1
    fixture_final['P2'][1] = C2
    for a, b in fixture_final.items():
        if a != 'P5' and a != 'P6' and a != 'P7' and a != 'P8':
            partido = [a]
            resultado = b
            partido.append(';'.join(map(str,resultado)))
            linea_final = ';'.join(map(str,partido))+'\n'
            cuartos_final.write(linea_final)
    detalle_partidos.close()
    cuartos_final.close()
    return None

def semi_finales (): 
    archivo1 = open('cuarto_de_final.dat', 'r')
    archivo2 = open('semi_finales.dat', 'w')
    for linea in archivo1:
        cuarto_final = linea.strip().split(';')
        partido, equipo1, equipo2, goles_equipo1, goles_equipo2 = cuarto_final
        #Determinamos los ganadores/perdedores de cada partido y almacenamos en variables locales los resultados
        if goles_equipo1 > goles_equipo2:
            ganador = equipo1
        else:
            ganador = equipo2
        if partido =='P1':
            P1= ganador
        if partido =='P2':
            P2 = ganador
        if partido =='P3':
            P3=ganador
        if partido =='P4':
            P4=ganador
    #Los agregamos al diccionario fixture_final
    fixture_final['P5'][0] = P1
    fixture_final['P5'][1] = P2
    fixture_final['P6'][0] = P3
    fixture_final['P6'][1] = P4
    #Lo escribimos en el archivo semi_finales.dat
    archivo2.write('P5;'+P1+';'+P2+';0;0'+'\n'+'P6;'+P3+';'+P4+';0;0')
    archivo2.close()
    archivo1.close()
    return None


def finales ():
    archivo = open('semi_finales.dat', 'r')
    archivo2 = open('finales.dat', 'w')
    for linea in archivo:
        semi_finales = linea.strip().split(';')
        partido, equipo1, equipo2, goles_equipo1, goles_equipo2 = semi_finales
        #Determinamos los ganadores/perdedores de cada partido y almacenamos en variables locales los resultados
        if goles_equipo1 > goles_equipo2:
            ganador = equipo1
            perdedor = equipo2
        else:
            ganador = equipo2
            perdedor = equipo1
        if partido =='P5':
            G5= ganador
            P5= perdedor
        if partido =='P6':
            G6= ganador
            P6= perdedor
    #Los agregamos al diccionario fixture_final
    fixture_final['P7'][0] = P5
    fixture_final['P7'][1] = P6
    fixture_final['P8'][0] = G5
    fixture_final['P8'][1] = G6
    #Lo escribimos en el archivo finales.dat
    archivo2.write('P7;'+P5+';'+P6+';0;0'+'\n'+'P8;'+G5+';'+G6+';0;0')
    archivo2.close()
    archivo.close()
    return None

#Funcion auxiliar creada para obtener el primero, segundo y tercero de un grupo.
def mejores_grupo(diccionario):
    primero = ''
    segundo = ''
    tercero = ''
    PTS_d = 0
    DI_d = 0
    GF_d = 0
    for i,j in diccionario.items():
        if diccionario[i][0] > PTS_d:
            primero = i
            PTS_d = diccionario[i][0]
        elif diccionario[i][0] == PTS_d:
            if diccionario[i][1] > DI_d:
                primero = i
                DI_d = diccionario[i][1]
            elif diccionario[i][1] == DI_d:
                if diccionario[i][2] > GF_d:
                    primero = i
                    GF_d = diccionario[i][2]
    PTS_d = 0
    DI_d = 0
    GF_d = 0
    for i, j in diccionario.items():
        if i != primero:
            if diccionario[i][0] > PTS_d:
                segundo = i
                PTS_d = diccionario[i][0]
            elif diccionario[i][0] == PTS_d:
                if diccionario[i][1] > DI_d:
                    segundo = i
                    DI_d = diccionario[i][1]
                elif diccionario[i][1] == DI_d:
                    if diccionario[i][2] > GF_d:
                        segundo = i
                        GF_d = diccionario[i][2]
    PTS_d = 0
    DI_d = 0
    GF_d = 0
    for i, j in diccionario.items():
        if i != primero:
            if i!= segundo:
                if diccionario[i][0] > PTS_d:
                    tercero = i
                    PTS_d = diccionario[i][0]
                elif diccionario[i][0] == PTS_d:
                    if diccionario[i][1] > DI_d:
                        tercero = i
                        DI_d = diccionario[i][1]
                    elif diccionario[i][1] == DI_d:
                        if diccionario[i][2] > GF_d:
                            tercero = i
                            GF_d = diccionario[i][2]
    return [primero,segundo,tercero]

#Funcion auxiliar para escoger los dos mejores terceros.
def mejores_tercero(diccionario):
    tercero1 = ''
    tercero2 = ''
    PTS_d = 0
    DI_d = 0
    GF_d = 0
    for i,j in diccionario.items():
        if diccionario[i][0] > PTS_d:
            tercero1 = i
            PTS_d = diccionario[i][0]
        elif diccionario[i][0] == PTS_d:
            if diccionario[i][1] > DI_d:
                tercero1 = i
                DI_d = diccionario[i][1]
            elif diccionario[i][1] == DI_d:
                if diccionario[i][2] > GF_d:
                    tercero1 = i
                    GF_d = diccionario[i][2]
    PTS_d = 0
    DI_d = 0
    GF_d = 0
    for i, j in diccionario.items():
        if i != tercero1:
            if diccionario[i][0] > PTS_d:
                tercero2 = i
                PTS_d = diccionario[i][0]
            elif diccionario[i][0] == PTS_d:
                if diccionario[i][1] > DI_d:
                    tercero2 = i
                    DI_d = diccionario[i][1]
                elif diccionario[i][1] == DI_d:
                    if diccionario[i][2] > GF_d:
                        tercero2 = i
                        GF_d = diccionario[i][2]
    return [tercero1, tercero2]