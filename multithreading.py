#Multithreading program for traffic signal
import threading
from threading import *
from time import sleep
lock=threading.Lock()

#Defining signal function
def green ():
    lock.acquire()
    print("Signal is green for 5 seconds, you can go now\n")
    for i in range (1,6):        
        print(i)
        sleep(1)
    lock.release()

def red():
    lock.acquire()
    print ("Red light for 10 seconds, please stop before the zebra crossing\n")
    for i in range (1,11):
        print(i)
        sleep(1)
    lock.release()

def yellow():
    lock.acquire()
    print("Alert: Signal is to be red within 2 seconds, please stop before zebra crossing\n")
    for i in range (1,3):
        print (i)
        sleep(1)
    lock.release()

#Threads creation
tg=Thread(target=green)
ty=Thread(target=yellow)
tr=Thread(target=red)

#Starting thread
tg.start()
ty.start()
tr.start()
