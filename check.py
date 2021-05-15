import psutil
import time
import os

run = True
while run:
    pids = psutil.pids()
    run = False
    try:
        for pid in pids:
            p = psutil.Process(pid)
            process_name = p.name()
            #print(process_name)
            if process_name == 'aria2c.exe':
                run = True
        time.sleep(1)
    except:
        run = True
        time.sleep(1)
        pass

path_real = str(__file__)
print(path_real)
path_name = os.path.basename(path_real)
f = open(path_real[:path_real.find(path_name)] + 'died', 'w')
f.write('aria2 is dead...')
f.close()
