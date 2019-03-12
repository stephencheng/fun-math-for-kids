#!/usr/bin/env python
import random
import time
from subprocess import call

score=0
idx=0
while True:
    for x in range(1,12):
        idy=0
        idx+=1
        for y in range(1,12):
            idy+=1
            # print "{0}: {1} * {2} = {3}".format(idx,x,y, x*y)
            call(["clear"])
            print "{0} {1} * {2} = {3}".format("\n"*idx+"   "*idy,x,y, x*y)
            time.sleep(0.5)
    # call(["say", msg])
