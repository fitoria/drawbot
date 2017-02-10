#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# ejercicio_3.py
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

# Las varaibles son "cajas" donde se puede almacenar un valor y cambiarlo a 
# medida que nuestro programa se va ejecutando, permiten almacenar cualquier 
# valor, numeros, cadenas de caracteres y muchas cosas mas.
# en este ejemplo, la variable "Lados" determina la cantidad de lados que va a 
# tener el poligono que vamos a dibujar con nuestro robot.
lados=5
for a in range(lados):
    robot.adelante(100)
    robot.derecha(360/lados) # la suma de los angulos de un poligono regular 
                             # es igual a 360, por lo tanto si tenemos 5 angulos
                             # cada uno de ellos tiene que ser de 360/5= 72°
# Cambiando el valor de "lados" podemos dibujar cualquier poligono regular
#  Una ves terminado el dibujo, levanta el lapiz y cierra el programa
robot.levantar_lapiz()
robot.cerrar()


