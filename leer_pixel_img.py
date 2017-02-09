#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  leer_pixel_img.py
#  
#  Copyright 2017 valentin basel <vbasel@notebookvalen>
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
from PIL import Image
i = Image.open("/home/vbasel/python.png")
pix = i.load()
xx,yy=i.size
for y in range(yy):
    linea=""
    for x in range(xx):
        pixel = pix[x,y]
        #~ print pixel
        if pixel[0]==255 and pixel[1]==255 and pixel[2]==255:
            linea= linea + "_"
        else:
            linea= linea + "#"
    print linea

