#!./venv/bin/python

from __future__ import print_function
import requests
import sys
import signal
from sets import Set
from collections import OrderedDict

if __name__=="__main__":
    print('hammer.py running ...')
    ok = 0
    items = OrderedDict()
    while True:
        try:
            response = requests.get('http://localhost:8080/')
            if len(response.text) == 36:
                ok += 1
                if response.text not in items.keys():
                    items[response.text] = 0
                items[response.text] += 1
            else:
                print('incorrect response, was', response.text)
                raise ValueError('Incorrect response', response.text)
        except:
            raise
        finally:
            sys.stdout.write("\rOK: %d. %s" % (ok, ", ".join(["%s: %d" % (k, v) for (k, v) in items.items()])))
            sys.stdout.flush()
