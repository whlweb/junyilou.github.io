import os, signal, sys
from time import sleep
pRead = open(os.path.expanduser('~') + "/pid.txt"); pid = pRead.read()
bint = bin(int(sys.argv[1])).replace("0b",""); lbn = len(bint)
print "\nGet Integer: " + sys.argv[1] + "\nSending binary: " +  bint + " to PID " + pid; sleep(0.7)
for l in range (0, lbn):
	if bint[l] == "0": os.kill(int(pid),signal.SIGUSR1)
	if bint[l] == "1": os.kill(int(pid),signal.SIGUSR2)
	print "Sending letter No." + str(l+1) + ", " + str(lbn) + " in total."
	sleep(0.3)
os.kill(int(pid),signal.SIGTERM)
print "Sent."