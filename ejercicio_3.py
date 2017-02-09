#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ejercicio_3.py
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
aa=15
ll=5
drawbot.bajar_lapiz()
for n in range(4):
    for a in range(ll):
        for b in range(1,aa):
            drawbot.subir(b)
            drawbot.izquierda(b)
            drawbot.bajar(b)
            drawbot.derecha(b)
        drawbot.derecha(aa)
    drawbot.bajar(aa)
    for a in range(ll):
        for b in range(1,aa):
            drawbot.subir(b)
            drawbot.izquierda(b)
            drawbot.bajar(b)
            drawbot.derecha(b)
        drawbot.izquierda(aa)
    drawbot.bajar(aa)
drawbot.levantar_lapiz()
