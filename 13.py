__author__ = 'Tarnasa'

import xmlrpc.client
import xmlrpc.server

url = 'http://www.pythonchallenge.com/pc/phonebook.php'

proxy = xmlrpc.client.ServerProxy(url)

print(proxy.system.listMethods())

print(proxy.phone('Bert'))