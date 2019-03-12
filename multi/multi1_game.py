#!/usr/bin/env python
import random
import time
from subprocess import call

idx=0
score=0
while True:
    for x in range(2,5):
        idy=0
        for y in range(1,12):
            idx+=1
            idy+=1
            # print "{0}: {1} * {2} = {3}".format(idx,x,y, x*y)
            call(["clear"])
            question="{0} {1} * {2} = {3}".format(" "*idy,x,y, "")
            answer="{0}".format(x*y)
            print(question)
            time.sleep(0.5)
            call(["say", question])
            time.sleep(0.5)
            call(["say", answer])
