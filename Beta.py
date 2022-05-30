import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from F711 import buynow
    buynow()
elif bit == '32bit':
    from F32 import buynow
    buynow()
