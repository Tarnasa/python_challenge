__author__ = 'Tarnasa'

import urllib.request
from io import BytesIO
from PIL import Image

url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'

username = 'huge'
password = 'file'

password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, url, username, password)
urllib.request.install_opener(urllib.request.build_opener(urllib.request.HTTPBasicAuthHandler(password_manager)))

im = Image.open(BytesIO(urllib.request.urlopen(url).read()))
px = im.load()
for y in range(0, im.size[1]):
    for x in range(y % 2, im.size[0] - 1, 2):
        px[x + 1, y] = px[x, y]

im.show()