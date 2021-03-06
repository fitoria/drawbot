#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ejercicio_5.py
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
angulo=3
for m in range(12):
    robot.bajar_lapiz()
    for a in range(1,36,3):
        robot.adelante(9+a)
        robot.derecha(360/angulo)
    robot.levantar_lapiz()
    robot.poner_a_cero()
    robot.derecha(30)
    robot.atras(a)
