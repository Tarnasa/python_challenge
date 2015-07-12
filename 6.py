__author__ = 'Tarnasa'

import zipfile
import re

comments = []
n = '90052'

with zipfile.ZipFile('channel.zip') as z:
    name_list = set(z.namelist())
    while True:
        filename = '{}.txt'.format(n)
        if filename not in name_list:
            break
        comments.append(z.getinfo(filename).comment)
        with z.open(filename) as f:
            n = re.search(r'([0-9]*$)', f.readline().decode('utf-8')).group(1)
        print(n)

print(''.join(comment.decode('utf-8') for comment in comments))



