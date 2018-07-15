Step 1: Run the client.py program as:

python2.7 client.py 6002 6003 6004 6005 6006 in on window
python2.7 client.py 6003 6002 6004 6005 6006 in on window
python2.7 client.py 6004 6003 6002 6005 6006 in on window
python2.7 client.py 6005 6003 6002 6004 6006 in on window
python2.7 client.py 6006 6003 6002 6005 6004 in on window




On the client input number:
6 pop 
7 create 
8 add
9 print
10 show id
11 top
12 size



To kill a node simply "cmd c" or grep kill -p on a window.  This terminates a node.


syncobj_admin -conn 127.0.0.1:6002 -status shows the status and leader of the cluster.

syncobj_admin -conn 127.0.0.1:6002 -add 127.0.0.1:6010 adds a cluster.


The program does:
Leader election
Dynamic membership change
Log replication
Encryption
Tolerates 2 terminations
Log compactions

Doesn't do:

Does no detect the least amount of nodes for the raft consensus to work.
No unified client



