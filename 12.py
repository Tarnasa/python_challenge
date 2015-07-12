__author__ = 'Tarnasa'

import urllib.request
from io import BytesIO
from PIL import Image

url = 'http://www.pythonchallenge.com/pc/return/evil2.gfx'

username = 'huge'
password = 'file'

password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, url, username, password)
urllib.request.install_opener(urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(password_manager)))

filenames = "1.jpg,2.png,3.gif,4.png,5.jpg".split(',')
files = [open(filename, 'wb') for filename in filenames]

for index, byte in enumerate(urllib.request.urlopen(url).read()):
    files[index % len(files)].write(bytes([byte]))

for filename in filenames:
    im = Image.open(filename)
    im.show()