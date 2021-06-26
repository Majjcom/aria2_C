import psutil
import time
import os

name = 'died'

run = True
while run:
    pids = psutil.pids()
    run = False
    try:
        for pid in pids:
            p = psutil.Process(pid)
            process_name = p.name()
            if process_name == 'aria2c.exe':
                name = 'got'
    except:
        run = True
        pass

path_real = str(__file__)
print(path_real)
path_name = os.path.basename(path_real)
f = open(path_real[:path_real.find(path_name)] + name, 'w')
f.close()
