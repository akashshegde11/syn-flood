import sys
from scapy.all import *

print("Field Values of packet sent")

p=IP(dst="192.168.1.100",id=1111,ttl=150)/TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S")/"Testing"

ls(p)

print("Sending Packets in 0.3 second intervals for timeout of 4 sec")

ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)

print("Summary of answered & unanswered packets")

ans.summary()
unans.summary()

#print("source port flags in response")

#ans.make_table(lambda(s,r): (s.dst, s.dport, r.sprintf("%IP.id% \t %IP.ttl% \t %TCP.flags%")))