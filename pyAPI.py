def main():
    import sys
    if sys.argv[1] == 'check':
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
    elif sys.argv[1] == 'update':
        from http import client as C
        from os import path

        serv = C.HTTPConnection('space.majjcom.site:8898')
        serv.request('GET', '/api/v3/file/get/205/ver.txt?sign=Kz70hR7KWpmOZrvEQTCXKY4rkkABKU-9De4SISfUXcM%3D%3A0')
        req = serv.getresponse()
        ver = req.read().decode()
        print(ver)
        serv.close()
        path_real = str(__file__)
        print(path_real)
        path_name = path.basename(path_real)
        f = open(path_real[:path_real.find(path_name)] + 'ver', 'w')
        f.write(ver)
        f.close()

if __name__ == '__main__':
    main()
