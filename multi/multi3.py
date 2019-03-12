#!/usr/bin/env python
import random
import time
from subprocess import call

score=0
while True:
    a=range(1,12)
    b=range(1,12)
    x=random.choice(a)
    y=random.choice(b)
    msg="{0} {1} * {2} = {3}".format("\n"*x+"   "*y,x,y, x*y)
    print msg
    time.sleep(1)
    call(["clear"])
    call(["say", msg])
