#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    controla atraves de dbus
"""

import os
import dbus
import time
import pygame
from pygame.locals import *

from joystick.joystick import *
from joystick.constantes import *
from metha import extrae_methadatos as get_metha


INC = 0.1

def get_info(pl):
    f_name = pl.getPlayingUri()[7:].replace("%20", " ")
    dic = get_metha(f_name)
    try:
        print dic['nombre'],'-', dic['artista']
    except:
        print 'INFO NOT AVAIBLE'


def main():
    obj_bus = dbus.SessionBus()
    proxy = obj_bus.get_object('org.gnome.Rhythmbox', '/org/gnome/Rhythmbox/Player')
    player = dbus.Interface(proxy, 'org.gnome.Rhythmbox.Player')
    pygame.display.init()
    pygame.joystick.init()

    #controla que haya un joistic conectado
    try:
        joyst = pygame.joystick.Joystick(0)
        joyst.init()
    except pygame.error:
        print "Error no existe un Joistick conectado"
        sys.exit(-1)

    vol = 0.5
    play = player.getPlaying()

    #bucle principal
    loop = True
    while loop:
        time.sleep(0.05)
        joykeys = get_joy_keys(joyst)

        #izquierda
        if joykeys[AXIS_0_M]:
            player.previous()
            get_info(player)

        #derecha
        elif joykeys[AXIS_0_P]:
            player.next()
            get_info(player)

        #arriba
        elif joykeys[AXIS_1_M]:
            if vol <= 1.0:
                vol += INC
            player.setVolume(vol)
            #print "volumen \%%s" %int(vol * 100)


        #abajo
        elif joykeys[AXIS_1_P]:
            if vol >= 0.0:
                vol -= INC
            player.setVolume(vol)
            #print "volumen \%%s" %int(vol * 100)

        #start
        elif joykeys[BTN_9]:
            play = not(play)
            player.playPause(play)

        #select
        elif joykeys[BTN_8]:
            player.playPause(False)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                loop =False


if __name__ == '__main__':
    main()








