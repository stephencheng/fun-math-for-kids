#!/usr/bin/env python
import random
from subprocess import call
import time
from datetime import datetime
import sys

idx=0
score=1870
wrong=0
#the sum
c=11

start_time = datetime.now()

while idx<100:

    start_problem = time.time()
    idx+=1
    a=range(0,10)
    x=random.choice(a)
    print "{0} => what's the answer of: {1} + ? == {2}".format(idx,x,c)
    print "_____________________________________________"

    raw_num=raw_input("your answer:")
    try:
        # print "input is: {0}".format(raw_num)

        if raw_num=='q':
            print 'quit, bye'
            quit()
        else:
            num=int(raw_num)

            if num==c-x:
                msg=random.choice(["you are good at it","you are clever","you are really good at it","you worked very hard","you did good job"])
                score+=10
            else:
                msg=random.choice(["try one more time please","you can think harder","ooops, you need to work harder"])
                score-=20
                wrong+=1
            print msg
            call(["say", msg])
            sdiff=time.time() - start_problem
            print "it took {0} seconds".format(sdiff)
            if sdiff > 10:
                slow_msg="too slow this time, penalty 5 points"
                call(["say", slow_msg])
                score-=5
            else:
                fast_msg=random.choice(["you are really fast","you are fast"])
                print fast_msg
                call(["say", fast_msg])

            print "wrong: {0}\ntotal play time: {1}".format(wrong,datetime.now() - start_time)
            print "your score ---------> {0}\n\n".format(score)

    except:
        print "input is not valid, try again"
        msg=random.choice(["try one more time please","you have to think harder","ooops, you need to work harder"])
        score-=20
        wrong+=1
        continue

