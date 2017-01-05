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

from libreria.drawbot import ROBOT
drawbot=ROBOT()
drawbot.cerrar()
drawbot.iniciar()
caracter=4
def blanco():
    """TODO: Docstring for blanco.
    :returns: TODO

    """
    drawbot.derecha(caracter)
def negro():
    """TODO: Docstring for negro.
    :returns: TODO

    """
    for b in range(caracter):
        drawbot.subir(caracter)
        drawbot.derecha(1)
        drawbot.bajar(caracter)

def nueva_linea(p):
    """TODO: Docstring for nueva_linea.
    :returns: TODO

    """
    drawbot.levantar_lapiz()
    drawbot.izquierda(p*caracter)
    drawbot.bajar(caracter)
    drawbot.bajar_lapiz()

drawbot.bajar_lapiz()
arc=open("imagen_icaro.txt","r")
for linea in arc:
    pa=0
    for b in linea:
        if b==' ' or b=='\n' or b=='\r':
            blanco()
        else:
            negro()
        pa=pa+1
    nueva_linea(pa)
arc.close()
drawbot.levantar_lapiz()


