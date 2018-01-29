import threading

dict={}
class mythread(threading.Thread):
    def __init__(self, filename,string):
        threading.Thread.__init__(self)
        self.filename = filename
        self.string = string
    def run(self):
        f1=open(self.filename,'w')
        f1.write(self.string)
        f1.close()
        f1 = open(self.filename, 'r')
        str=f1.read()
        f1.close()
        l=str.split(" ")
        for i in l:
            if(dict.__contains__(i)):
                dict[i]=dict[i]+1
            else:
                dict[i]=1

t1 = mythread('thread1','hi my name is rajat')
t2 = mythread('thread2','rajat works at quantiphi')
t1.start()
t2.start()
t1.join()
t2.join()
print(dict)


