#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    moyenne = (a+b+c)/3
    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    return (angle_degs + (angle_mins + angle_secs/60)/60)*math.pi/180


def to_degrees(angle_rads: float) -> tuple:
    AngleEndegree = (angle_rads*360)/(2*math.pi)
    degrees, minutes, seconds = AngleEndegree, AngleEndegree/60, AngleEndegree/3600
    return  degrees, minutes, seconds


def to_celsius(temperature: float) -> float:
    TCelsius = (temperature -32) /1.8
    return TCelsius


def to_farenheit(temperature: float) -> float:
    Tfarenheit = temperature*1.8 + 32
    return Tfarenheit


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
