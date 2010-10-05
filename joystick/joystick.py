#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
joystick.py
========
    Version: 0.0.3

    Autor: Ricardo D. Quiroga -> L2Radamanthys

    Fecha: 18 de Febrero de 2010

    E-mail:
        l2radamanthys@gmail.com
        l2radamanthys@saltalug.org.ar
        ricardoquiroga.dev@gmail.com

    SitioWeb:
        http://www.l2radamanthys.tk
        http://l2radamanthys.unlugar.com
        http://l2radamanthys.blogspot.com

    Descripcion:
        Script para poder leer los eventos del Joystick como si se leyeran
        mediante el teclado, esta libreria requiere PyGame

    Terminos y Condiciones:
        Este Script es Software Libre y esta bajo terminos de la GNU General
        Public Licence publicada por la Free Software Foundation
        (http://www.fsf.org) version 2 de la licencia u/o (opcionalmente)
        otras versiones de la licencia.

        Usted puede redistribuir y/o modificar este Script
        siguiendo los terminos de la GNU General Public Licence
        para mayor informacion vease la copia de la licencia que
        se adjunta con estos Script.
"""


def status_axes(joyst, axes=[]):
    #axes = []
    num_axes = joyst.get_numaxes()
    for i in xrange(num_axes):
        axis = joyst.get_axis(i)
        #print 'axis %d V: %f ' %(i, axis),
        axis_m = False
        axis_p = False
        if int(round(axis)) < 0:
            axis_m = True
        if int(round(axis)) > 0:
            axis_p = True
        axes.append(axis_m)
        axes.append(axis_p)
    return axes


def get_axes(joyst):
    """
        retorna un array con el estado de todos los Axis
    """
    axes = []
    num_axes = joyst.get_numaxes()
    for i in xrange(num_axes):
        axes.append(joyst.get_axis(i))
    return axes


def get_buttons(joyst):
    """
        Retorna un array con el estado de todos los botones, retorna true
        si el boton esta pulsado, caso contrario retorna False
    """
    btns = []
    num_btn = joyst.get_numbuttons()
    for i in xrange(num_btn):
        btns.append(joyst.get_button(i))
    return btns


def get_joy_keys(joyst):
    """
        retorna las botones y axis precionados en un control.

        IMPORTANTE: ESTE METODO SOLO FUNCIONA CON CONTROLES QUE POSEAN
        12 BOTONES Y A LO SUMO 3 AXES, POR LO QUE NO ES UN METODO GENERICO
        QUE SE PUEDA USAR CON CUALQUIER CONTROL, TRATARE DE SUBSANAR ESTE
        PROBLEMA PARA VERSIONES FUTURAS.
    """
    btns = get_buttons(joyst)
    axes = status_axes(joyst, btns)
    return axes
