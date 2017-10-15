#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# prueba_mov_motor.py
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


#from libreria.vplot import ROBOT 
from libreria.pap import  MOTOR
from libreria.apicaro import puerto
import time
#from libreria.cinematica import VPLOTTER
#robot=VPLOTTER() # este es el "nombre" de nuestro robot.
#robot.iniciar() # iniciamos la conexion

# Con las 3 lineas de codigo anterior, logramos poner en marcha nuestro robot.
# a partir de ahora, las instrucciones moveran el cabezal para poder dibujar.

#robot.bajar_lapiz() # bajo el lapiz para que apoye sobre el papel
#robot.__motor1.girar(200)
icaro=puerto()
icaro.iniciar()
icaro.activar_servo(1,30)
time.sleep(1)
motor1=MOTOR([1,2,4,8])
for a in range(231):
    a=motor1.girar(-1)
    icaro.activar(a)
    time.sleep(0.01)
icaro.activar_servo(1,128)
icaro.activar(0)
#robot.levantar_lapiz()

