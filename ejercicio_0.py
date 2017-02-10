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

###############################################################################
#
# Este es un primer ejercicio de prueba para nuestro robot dibujante.
# todo lo que este despues del simbolo # no es tenido en cuenta por el
# interprete PYTHON, se usa para dejar comentarios para las personas que 
# tengan que leer el codigo fuente.
#
###############################################################################

# La siguiente linea de codigo, importa la libreria necesaria para poder 
# controlar nuestro robot, para poder darle ordenes de forma sencilla.
# Las librerias nos permiten re utilizar codigo fuente, para no tener que
# escribir de vuelta lo mismo una y otra ves.

from libreria.vplot import ROBOT 

robot=ROBOT() # este es el "nombre" de nuestro robot.
robot.iniciar() # iniciamos la conexion

# Con las 3 lineas de codigo anterior, logramos poner en marcha nuestro robot.
# a partir de ahora, las instrucciones moveran el cabezal para poder dibujar.

robot.bajar_lapiz() # bajo el lapiz para que apoye sobre el papel

# el cabezal de dibujo de nuestro robot puede moverse para adelante, atras y
# girar a la derecha o a la izquierda (en grados).

#con el siguiente codigo el robot dibujara un cuadrado de 100 puntos de lado
robot.adelante(100)
robot.derecha(90)
robot.adelante(100)
robot.derecha(90)
robot.adelante(100)
robot.derecha(90)
robot.adelante(100)

#  Una ves terminado el dibujo, levanta el lapiz y cierra el programa
robot.levantar_lapiz()
robot.cerrar()



