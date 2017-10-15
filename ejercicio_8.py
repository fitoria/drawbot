#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ejercicio_1.py
#
# Copyright © 2017 Valentin Basel <valentinbasel@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#########################5######################################################
#
# En el ejercicio anterior dibujamos un cuadrado con los comandos para mover
# el cabezal del robot.
# Sin embargo, repetimos 4 veces la mismas lineas - adelante(100), derecha(90)-
# En este ejercicio vamos a usar un bucle de repeticion "for" que nos permite 
# repetir muchas veces la misma porcion de codigo fuente.
# los bucles o repeticiones, son una de las partes mas importante de programar.

from libreria.vplot import ROBOT 

robot=ROBOT() # este es el "nombre" de nuestro robot.
#robot.PUERTO="/dev/ttyACM1"

robot.iniciar() # iniciamos la conexion
#~ robot.subir_lapiz()
robot.bajar_lapiz() # bajo el lapiz para que apoye sobre el papel
b=15
lados=5

for a in range(100):
    robot.adelante(b)
    robot.derecha((360/lados)-1)
    b=b+5

#  Una ves terminado el dibujo, levanta el lapiz y cierra el programa
robot.levantar_lapiz()
robot.cerrar()



