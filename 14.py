__author__ = 'Tarnasa'

import urllib.request
from io import BytesIO
from PIL import Image

url = 'http://www.pythonchallenge.com/pc/return/wire.png'

username = 'huge'
password = 'file'

password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, url, username, password)
urllib.request.install_opener(urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(password_manager)))

im = Image.open(BytesIO(urllib.request.urlopen(url).read()))
generated = Image.new('RGB', (100, 100), (0, 0, 0))

im_pixels = im.load()
gen_pixels = generated.load()

x, y = 0, 0
xd, yd = 1, 0
length = 100
n = 0
for index in range(100*100):
    gen_pixels[x, y] = im_pixels[index, 0]
    n += 1
    if n == length:
        n = 0
        if xd != 0:
            length -= 1
        xd, yd = -yd, xd
    x += xd
    y += yd

generated.show()