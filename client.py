import stack
import sys
import time
from functools import partial
from stack import TestObj
sys.path.append("../")
from pysyncobj import SyncObj, replicated,SyncObjConf

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
        # if n % 200 == 0:
        # if True:
        #    print('Counter value:', o.getCounter(), o._getLeader(), o._getRaftLogSize(), o._getLastCommitIndex())
'''
python27. client.py 6002 6003 6004 6005 6006

'''
