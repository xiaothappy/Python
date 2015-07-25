#!/usr/bin/python
#Author xiaothappy
#Date 2015/07/25
import os
import time
import os.path
def listfile(df):
    try:
        if os.path.isdir(df):
            for i in os.listdir(df):
                ds=df+'/'+i
                if os.path.isdir(ds):
                    listfile(ds)
                else :
                    f=open(ds,'r')
                    print '%s have :'%(ds)
                    for j in f:
                        print j
                        time.sleep(0.5)
                    f.close()
        else:
            print '%s is not a dir!'%(df)
    except:
        pass
if __name__=='__main__':
    d=raw_input('Enter the dir:')
    listfile(d)
