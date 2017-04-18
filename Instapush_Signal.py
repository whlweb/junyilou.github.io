import os, signal
from time import sleep
pid = input("Input PID. ")
bint = bin(input("Input a number. ")).replace("0b",""); lbn = len(bint)
os.kill(pid,signal.SIGCONT)
print "Sending binary: " +  bint + " to PID " + str(pid); sleep(0.7)
for l in range (0, lbn):
	if bint[l] == "0": os.kill(pid,signal.SIGUSR1)
	if bint[l] == "1": os.kill(pid,signal.SIGUSR2)
	print "Sending letter No." + str(l+1) + ", " + str(lbn) + " in total."
	sleep(0.3)
os.kill(pid,signal.SIGTERM)
print "Sent."