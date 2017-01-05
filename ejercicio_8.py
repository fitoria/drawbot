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

from drawbot import ROBOT
drawbot=ROBOT()
drawbot.iniciar()
drawbot.bajar_lapiz()
#~ drawbot.bajar(1)
#~ drawbot.levantar_lapiz()
#~ exit()
for a in range(10):
    drawbot.bajar(200)
    drawbot.izquierda(10)
    drawbot.subir(200)
    drawbot.izquierda(10)

drawbot.levantar_lapiz()
