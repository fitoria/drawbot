#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ejercicio_1.py
#
#  Copyright 2016 valentin basel <vbasel@valentin.basel>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from PIL import Image
from libreria.vplot import ROBOT
drawbot = ROBOT()
drawbot.cerrar()
drawbot.iniciar()
caracter = 3
def blanco():
    """TODO: Docstring for blanco.
    :returns: TODO

    """
    drawbot.adelante(caracter)
def negro():
    """TODO: Docstring for negro.
    :returns: TODO

    """
    for b in range(caracter):
        drawbot.izquierda(90)
        drawbot.adelante(caracter)
        drawbot.derecha(90)
        drawbot.adelante(1)
        drawbot.derecha(90)
        drawbot.adelante(caracter)
        drawbot.izquierda(90)

def nueva_linea(p):
    """TODO: Docstring for nueva_linea.
    :returns: TODO

    """
    drawbot.levantar_lapiz()
    drawbot.derecha(180)
    drawbot.adelante(p*caracter)
    drawbot.izquierda(90)
    drawbot.adelante(caracter)
    drawbot.izquierda(90)
    drawbot.bajar_lapiz()

drawbot.bajar_lapiz()
#~ arc=open("imagen_icaro.txt","r")
#~ for linea in arc:
    #~ pa=0
    #~ for b in linea:
        #~ if b==' ' or b=='\n' or b=='\r':
            #~ blanco()
        #~ else:
            #~ negro()
        #~ pa=pa+1
    #~ nueva_linea(pa)
#~ arc.close()


i = Image.open("/home/vbasel/python.png")
pix = i.load()
xx,yy=i.size
for y in range(yy):
    linea=""
    pa=0
    for x in range(xx):
        pixel = pix[x,y]
        if pixel[0]==255 and pixel[1]==255 and pixel[2]==255:
            linea= linea + "_"
            blanco()
        else:
            linea= linea + "#"
            negro()
        pa=pa+1
    print linea
    nueva_linea(pa)
drawbot.levantar_lapiz()


