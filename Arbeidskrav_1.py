# -*- coding: utf-8 -*-
"""
I denne koden finner vi ut av hva som blir den billigste, årlige kostnadene 
av el-bil og bensinbil. 

Created on Sun Nov  3 21:34:16 2024

@author: Marianne Gulliksen ma_gulliksen@hotmail.com
"""

""" Antall km. og dager i året """
km = 12000
år = 365

""" Prisen på årlig forsikring for hhv. el-bil og bensinbil"""
fe = 5000
fb = 7500

""" Trafikkforsikringsavgift"""
tfa = 8.38

""" Drivstoffforbruk"""
kwhkm = 0.2
kwhkr = 2.00
bensin = 1.0

""" Bomavgift"""
bae = 0.1
bab = 0.3

""" Årlig avgift el-bil"""
Elbil = fe + (tfa*år) + (km*kwhkm*kwhkr) + (km*bae)

print(Elbil)

""" Årlig avgift bensinbil"""
Bensinbil = fb + (tfa*år) + (bensin*km) + (km*bab)

print(Bensinbil)

""" Differanse mellom kostnadene """
Diff = Bensinbil - Elbil

print(Diff)

""" Konklusjonen er at i dette tilfellet er det mye billigere med El-bil, 
med en differanse på 12 100,-"""