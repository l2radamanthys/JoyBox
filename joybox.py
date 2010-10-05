#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
joybox.py
==========
    Version: 0.0.3(Beta)

    Autor: Ricardo D. Quiroga->L2Radamanthys

    Fecha: 13 de Junio de 2010

    E-mail:
        l2radamanthys@gmail.com
        l2radamanthys@saltalug.org.ar
        ricardoquiroga.dev@gmail.com

    SitioWeb:
        http://www.l2radamanthys.com.ar
        http://l2radamanthys.blogspot.com

    Descripcion:
        Pequeño Script que permite controlar rhythmbox mediante un Joystic

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

__version__ = "0.0.2"
__autor__ = "Ricardo D. Quiroga - L2Radamanthys  l2radamanthys@gmailcom"
__date__ = "13 de Junio de 2010"
__copyright__ = "Copyright (c) 2010 Ricardo D. Quiroga"
__license__ = "GPL2"


import sys
import time
from os import system
import pygame
from pygame.locals import *

from joystick.joystick import *
from joystick.constantes import *


#CONSTANTES DE COMANDOS
cmd = 'rhythmbox-client '
play = '--play-pause'
sig = '--next'
ant = '--previous'
up = '--volume-up'
down = '--volume-down'
quit='--quit'
pformat='--print-playing-format="%tt %ta %td"'


def status(buffer, mensaje=''):
    buffer = [mensaje] + buffer[:-1]
    system('clear')
    print """
        ------------------------------------
            JOYBOX v(0.0.2) Beta
        Ricardo D. Quiroga -> L2Radamanthys
            l2radamanthys@gmail.com
          http://www.l2radamanthys.com.ar
        ------------------------------------
    """
    print '-------------------------------------------------'
    system(cmd + pformat)
    print '-------------------------------------------------'
    print buffer[0]
    print '-------------------------------------------------'
    #buffer.append(msj)
    for msj in buffer[1:]:
        print msj
    print '-------------------------------------------------'
    return buffer


def main():
    pygame.display.init()
    pygame.joystick.init()
    #screen = pygame.display.set_mode((100,100))
    reloj = pygame.time.Clock()

    #controla que haya un joistic conectado
    try:
        joyst = pygame.joystick.Joystick(0)
        joyst.init()
    except pygame.error:
        print "Error no existe un Joistick conectado"
        sys.exit(-1)


    evt_buffer = [
        '- -----------',
        '- -----------',
        '- -----------',
        '- -----------',
        '- -----------',
        '- -----------',
        '- -----------',
        '- -----------',
    ]
    evt_buffer = status(evt_buffer, '- JOYBOX INIT')

    loop = True
    while loop:
        time.sleep(0.05)
        joykeys = get_joy_keys(joyst)

        #izquierda
        if joykeys[AXIS_0_M]:
            system(cmd + ant)
            evt_buffer = status(evt_buffer, '- PISTA ANT <-')

        #derecha
        elif joykeys[AXIS_0_P]:
            system(cmd + sig)
            evt_buffer = status(evt_buffer, '- PISTA SIG->')

        #arriba
        elif joykeys[AXIS_1_M]:
            system(cmd + up)
            evt_buffer = status(evt_buffer, '- VOLUMEN ++')

        #abajo
        elif joykeys[AXIS_1_P]:
            system(cmd + down)
            evt_buffer = status(evt_buffer, '- VOLUMEN --')

        #start
        elif joykeys[BTN_9]:
            system(cmd + play)
            evt_buffer = status(evt_buffer, '- PLAY/PAUSE')

        #select
        elif joykeys[BTN_8]:
            system(cmd + quit)
            evt_buffer = status(evt_buffer, '- STOP')

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                loop =False


if __name__ == '__main__':
    main()
