__author__ = 'Tarnasa'

import PIL.Image

filename = 'oxygen.png'

#import urllib.request
#
#url = r'http://www.pythonchallenge.com/pc/def/oxygen.png'
#
#with open(filename, 'wb') as f:
#    f.write(urllib.request.urlopen(url).read())

xs, ys = 2, 47
xd = 7
xe = 608

im = PIL.Image.open(filename)
px = im.load()

values = ''.join(chr(px[x, ys][0]) for x in range(xs, xe, xd))

print(values)
