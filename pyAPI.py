def check():
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

def update():
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

def trans(source, target):
    from os import remove
    from os import path
    f_s = open(source, 'rb')
    f_t = open(target, 'w', encoding='utf-8')
    content = ''
    tmp = f_s.read().decode()
    for i in tmp:
        if i == '\r':
            content += '\n'
        else:
            content += i
    f_t.write(content)
    f_s.close()
    f_t.close()
    remove(source)

def main():
    import sys
    if sys.argv[1] == 'check':
        check()
    elif sys.argv[1] == 'update':
        update()
    elif sys.argv[1] == 'trans':
        trans(sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()
