#!/usr/bin/env python
import random
import time
from subprocess import call

score=0
idx=0
# while True:

def f(x,y):

    print(" "*9)
    row=""
    for i in range(1,y+1):
        row+=" "+str(i)

    print " "*9+row
    for i in range(1,x+1):
        print(" "*7+str(i).rjust(2," ")+" o"*y)

while idx<24:
    idx+=1
    a=range(2,12)
    b=range(5,7)
    x=random.choice(a)
    y=random.choice(b)
    call(["clear"])
    print(idx)
    print(" \n"*3)
    f(x,y)
    question="{0} {1} * {2} = {3}".format(" \n"*3+" "*9,x,y, "")
    print(question)
    time.sleep(2)
    # call(["say", question])
    call(["clear"])
    print(idx)
    print(" \n"*3)
    f(x,y)
    answer="{0} {1} * {2} = {3}".format(" \n"*3+" "*9,x,y, x*y)
    print(answer)
    time.sleep(1)
    # call(["say", answer])
