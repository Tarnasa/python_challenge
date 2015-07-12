__author__ = 'Tarnasa'

import urllib.request
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

n = '8022' # '12345'

for i in range(500):
    s = urllib.request.urlopen(url + n).read().decode('utf-8')
    n = re.search(r'([0-9]+$)', s).group(1)
    print(n)

