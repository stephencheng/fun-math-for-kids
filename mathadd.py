#!/usr/bin/env python
import random
from subprocess import call

idx=0
score=0
while True:
    idx+=1
    a=range(3,10)
    b=range(3,10)
    x=random.choice(a)
    y=random.choice(b)
    print "{0} => what's the answer of: {1} + {2}".format(idx,x,y)
    print "_____________________________________________"
    try:
        num=int(raw_input("your answer:"))
    except:
        next
    if num==x+y:
        msg=random.choice(["you are good at it","you are really good at it","you worked very hard","you did good job"])
        score+=10
    else:
        msg=random.choice(["try one more time please","you have to think harder","ooops, you need to work harder"])
        score-=5
    print msg
    print "your score ---------> {0} \n\n".format(score)
    call(["say", msg])
