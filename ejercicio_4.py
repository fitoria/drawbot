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
drawbot.iniciar()
valor_viejo=0
drawbot.bajar_lapiz()

for a in range(100):
    drawbot.derecha(1)
    valor=drawbot.leer_analogico(1)
    valorfinal=((valor*20)/1023)
    if valorfinal>valor_viejo:
        drawbot.subir(valorfinal)
    if valorfinal<valor_viejo:
        drawbot.bajar(valorfinal)
    valor_viejo=valorfinal
drawbot.levantar_lapiz()

