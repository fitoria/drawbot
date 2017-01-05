#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  drawbot.py
#
#  Copyright 2016 valentin basel <valentinbasel@gmail.com>
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

import time
import apicaro
import pap

class ROBOT(apicaro.puerto):
    """
    La clase ROBOT, contiene las instrucciones para iniciar y mover
    el DRAWBOT.
    Hereda los atributos de la clase puerto de apicaro.
    """

    def __init__ (self):
        """
        Valores globales del robot, como su velocidad o los
        paso que puede dar cada motor PAP
        """
        self.velocidad=0.02
        self.motor1=pap.MOTOR([1,2,4,8])
        self.motor2=pap.MOTOR([16,32,64,128])

    def apagar(self):
        """
        Pone los bits del puerto UNL2803 a 0.
        """
        self.activar(0)
        return 0

    def subir(self,pasos):
        """
        Mueve los motores 1 y 2 N-pasos para subir/bajar el
        cabezal.
        motor_1 = 1
        motor_2 = 1
        """
        if pasos>0:
            print "subir: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor1.girar(1)
                b=self.motor2.girar(1)
                self.activar(a+b)
                time.sleep(self.velocidad)
        else:
            print "bajar: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor1.girar(-1)
                b=self.motor2.girar(-1)
                self.activar(a+b)
                time.sleep(self.velocidad)
        self.activar(0)
        return 0

    def bajar(self,pasos):
        """
        Mueve los motores 1 y 2 N-pasos para subir/bajar el
        cabezal.
        motor_1 = -1
        motor_2 = -1
        """
        if pasos>0:
            print "bajar: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor1.girar(-1)
                b=self.motor2.girar(-1)
                self.activar(a+b)
                time.sleep(self.velocidad)
        else:
            print "subir: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor1.girar(1)
                b=self.motor2.girar(1)
                self.activar(a+b)
                time.sleep(self.velocidad)
        self.activar(0)
        return 0

    def derecha (self,pasos):
        """
        Mueve el cabezal a la derecha
        motor1 = -1
        motor2 = 1
        """
        if pasos>0:
            print "derecha: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor1.girar(-1)
                b=self.motor2.girar(1)
                self.activar(a+b)
                time.sleep(self.velocidad)
        else:
            print "izquierda: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor1.girar(1)
                b=self.motor2.girar(-1)
                self.activar(a+b)
                time.sleep(self.velocidad)
        self.activar(0)
        return 0

    def izquierda (self,pasos):
        """
        Mueve el cabezal a la izquierda
        motor1 = 1
        motor2 = -1
        """
        if pasos>0:
            print "izquierda: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor1.girar(1)
                b=self.motor2.girar(-1)
                self.activar(a+b)
                time.sleep(self.velocidad)
        else:
            print "derecha: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor1.girar(-1)
                b=self.motor2.girar(1)
                self.activar(a+b)
                time.sleep(self.velocidad)
        self.activar(0)
        return 0

    def bajar_lapiz(self):
        """
        Baja el servo
        servo1 = 30
        """
        self.activar_servo(1, 30)
        time.sleep(1)
        return 0

    def levantar_lapiz(self):
        """
        Levanta el servo
        servo1 = 128
        """
        self.activar_servo(1,128)
        time.sleep(1)
        return 0

    def girar_m1 (self,pasos):
        """
        mueve el motor 1
        """
        if pasos>0:
            print "motor 1 girar: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor1.girar(1)
                self.activar(a)
                time.sleep(self.velocidad)
        else:
            print "motor 1 girar: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor1.girar(-1)
                self.activar(a)
                time.sleep(self.velocidad)
        self.activar(0)
        return 0

    def girar_m2 (self,pasos):
        """
        mueve el motor 2
        """
        if pasos>0:
            print "motor 1 girar: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor2.girar(1)
                self.activar(a)
                time.sleep(self.velocidad)
        else:
            print "motor 1 girar: ", pasos, " pasos"
            for a in range(abs(pasos)):
                a=self.motor2.girar(-1)
                self.activar(a)
                time.sleep(self.velocidad)
        self.activar(0)
        return 0

