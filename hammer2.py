#!/usr/bin/env python

from __future__ import print_function
import os

if __name__=="__main__":
    while True:
        ret = os.system('curl http://localhost:8080/')
        if ret == 0:
            pass
        else:
            print(ret)
            break
    print('exiting')