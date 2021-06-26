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