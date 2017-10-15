#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ejercicio_7.py
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
lados=20
largo=50
for a in range(360/((360/lados)/2) ):
    for b in range(lados):
        robot.adelante(largo)
        robot.derecha(360/lados)
    robot.derecha((360/lados)/2)

#  Una ves terminado el dibujo, levanta el lapiz y cierra el programa

robot.levantar_lapiz()
robot.cerrar()
