#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Script para leer los methadatos des un archivo de musica
    por ahora solo soporta MP3
"""


def extrae_methadatos(file_name):
    """
    """
    dic = {}
    try:
        file = open(file_name, 'r+b')
    except IOError:
        print "IO Error"
        return dic

    file.seek(-128, 2)
    file.read(3)
    dic['nombre'] = file.read(30)
    dic['artista'] = file.read(30)
    dic['albun'] = file.read(30)
    dic['anio'] = file.read(4)
    dic['comentario'] = file.read(30)
    dic['genero'] = file.read(1)
    file.close()
    return dic


#test
#dic = extrae_methadatos("23 infinity.mp3")
#for k in dic:
#    print "%s \t\t %s" %(k, dic[k])
