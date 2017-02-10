#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ejercicio_2.py
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

from libreria.vplot import ROBOT 

robot=ROBOT() # este es el "nombre" de nuestro robot.
robot.iniciar() # iniciamos la conexion

robot.bajar_lapiz() # bajo el lapiz para que apoye sobre el papel

# En este ejercicio, usamos 2 bucles, uno adentro del otro, lo que se denomina
# un "bucle anidado", en cada interación del bucle A, se haran 3 repeticiones 
# del codigo fuente del bucle B (dibujando un triangulo).

for a in range(4): # bucle A
    for b in range(3): # bucle B
        robot.adelante(100)
        robot.derecha(120)
    robot.derecha(90)   # gira para que el robot no dibuje el mismo triangulo 
                        # sobre la misma superficie

#  Una ves terminado el dibujo, levanta el lapiz y cierra el programa
robot.levantar_lapiz()
robot.cerrar()


