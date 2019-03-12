#!/usr/bin/env python
import random
import time
from subprocess import call

score=0
idx=0
# while True:
while idx<24:
    idx+=1
    a=range(2,12)
    b=range(6,7)
    x=random.choice(a)
    y=random.choice(b)
    call(["clear"])
    print(idx)
    question="{0} {1} * {2} = {3}".format(" \n"*x+" "*y,x,y, "")
    answer="{0}".format(x*y)
    print(question)
    time.sleep(0.75)
    call(["say", question])
    time.sleep(0.75)
    call(["say", answer])
