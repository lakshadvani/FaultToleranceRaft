#!/usr/bin/env python
from __future__ import print_function

import sys
import time
from functools import partial

sys.path.append("../")
from pysyncobj import SyncObj, replicated,SyncObjConf


class TestObj(SyncObj):
    def __init__(self, selfNodeAddr, otherNodeAddrs):
        super(TestObj, self).__init__(selfNodeAddr, otherNodeAddrs)
        self.__counter = 0
        self.__list_of_queues = []
        self.__labelDict = {}
        self.t = []
        self.d = {}
        self.id = 0
        self.labs = {}

    @replicated
    def incCounter(self):
        self.__list_of_queues.append([])
        return self.__counter

    @replicated
    def qCreate(self,label):
        self.__list_of_queues.append([])
        self.__labelDict[label] = len(self.__list_of_queues)-1
        return self.__labelDict[label]

    @replicated
    def qID(self,label):
        return self.__labelDict[label]

    @replicated
    def qer(self):
        return self.t

    @replicated
    def creator(self,label):
        self.d[label] = []
        self.id = self.id+1
        self.labs[label] = self.id

    def checker(self,label):
        if(self.d[label]):
            return True
        else:
            return False


    @replicated
    def addor(self,label,val):
        if label in self.d.keys():
            self.d[label].append(val)
        else:
            print("no such stack")


    def show(self):
        print(self.d)

    def top(self,label):
        print(self.d[label][-1])

    def siz(self):
        print(len(self.d))
    def show_id(self,label):
        print(self.labs[label])
    # @replicated
    # def addValue(self, value, cn):
    #     self.__list_of_queues.append([])
    #     return len(self.__list_of_queues)

    @replicated
    def qPush(self, val):
        self.t.append(val)
        # return self.__list_of_queues[0]

    @replicated
    def qPop(self,label):
        return self.__list_of_queues[label].pop()

    def getCounter(self):
        return self.__counter

    def getQueue(self):
        if (len(self.__list_of_queues) >= 1):

            return self.__list_of_queues[0]
        else:
            return []

    def getQ(self):
        print((self.t))
        return self.t

    @replicated
    def popp(self,label):
        self.d[label].pop()

    def getListofQObjects(self):
        if(len(self.__list_of_queues) >= 1):
            return self.__list_of_queues
        else:
            return []


def onAdd(res, err, cnt):
    print("on add called %d" % cnt, res, err)

def onCreate(res,err,cnt):
    print("Queue created for %d" % cnt,res,err)


if __name__ == '__main__':
    SyncObjConf(dynamicMembershipChange = True)
    if len(sys.argv) < 3:
        print('Usage: %s self_port partner1_port partner2_port ...' % sys.argv[0])
        sys.exit(-1)

    port = int(sys.argv[1])
    partners = ['localhost:%d' % int(p) for p in sys.argv[2:]]
    print("Before o")
    o = TestObj('localhost:%d' % port, partners)
    n = 0
    old_value = -1
    print("Before while")
    print("")
    while True:
        time.sleep(2.5)
        #time.sleep(5)
        # nt ("before if value")
        nb = raw_input('Choose a number: ')
        if int(nb) == 1:
            print(o.getQueue())
        for item in o.getListofQObjects():
            print(item)

        if o._getLeader() is None:
            print("lol")
            continue
        # if n < 2000:
        if int(nb)==3:
            o.qCreate(n,callback=partial(onCreate,cnt=n))
            # o.addValue(1, n, callback=partial(onAdd, cnt=n))
        if int(nb)==2:
            o.qPush(10)
        if int(nb)==4:
            o.qer(n)
        if int(nb)==5:
            o.getQ()
        if int(nb)==6:
            jk = int(raw_input('label'))
            o.popp(jk)
        if int(nb)==7:
            v = int(raw_input('label'))
            o.creator(v)
        if int(nb)==8:
            qx = int(raw_input('label'))
            hg = int(raw_input('val'))
            o.addor(qx,int(hg))
            # print(len(list_of_queues))
        if int(nb)==9:
            o.show()
        if int(nb)==10:
            hg = int(raw_input('label'))
            o.show_id(hg)
        if int(nb) == 11:
            hg = int(raw_input('label'))
            o.top(hg)
        if int(nb) == 12:
            o.siz()
        n += 1
         #if n % 200 == 0:
         #if True:
         #   print('Counter value:', o.getCounter(), o._getLeader(), o._getRaftLogSize(), o._getLastCommitIndex())
