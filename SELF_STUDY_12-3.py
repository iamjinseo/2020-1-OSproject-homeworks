import threading
import time

class NUM :
    obj_name=''
    Sum=0
    limitNum=0
    def __init__(self, name, limitnum):
        self.obj_name=name
        self.limitNum=limitnum
    def Sum_nums(self) :
        print(self.obj_name, end=' : ')
        for i in range (1, (self.limitNum)+1) :
            self.Sum+=i
            print(i, "+ ", end='')
            time.sleep((0))
        print("=", self.Sum)

To1000=NUM('천까지', 1000)
To100000=NUM('십만까지', 100000)
To10000000=NUM('천만까지', 10000000)

th1=threading.Thread(target=To1000.Sum_nums())
th2=threading.Thread(target=To100000.Sum_nums())
th3=threading.Thread(target=To10000000.Sum_nums())

th1.start(); th2.start(); th3.start()