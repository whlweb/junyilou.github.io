import os, signal, sys
from time import sleep
pRead = open(os.path.expanduser('~') + "/pid.txt"); pid = pRead.read()
bint = bin(int(sys.argv[1])).replace("0b",""); lbn = len(bint)
try: os.kill(int(pid),signal.SIGCONT)
except OSError:
	print "No such progress featureing PID " + pid; sleep(0.7)
	os.system('screen -S jdk -X stuff "exit\n"'); os.system("screen -dmS jdk")
	os.system('screen -S jdk -X stuff "python ~/junyilou.github.io/Kuaidi_IFTTT.py ' + sys.argv[1] + '\n"')
	print "Daemon started screen session, run screen -r to check it."
else:
	print "\nGet Integer: " + sys.argv[1] + "\nSending binary: " +  bint + " to PID " + pid; sleep(0.7)
	for l in range (0, lbn):
		if bint[l] == "0": os.kill(int(pid),signal.SIGUSR1)
		if bint[l] == "1": os.kill(int(pid),signal.SIGUSR2)
		print "Sending letter No." + str(l+1) + ", " + str(lbn) + " in total."
		sleep(0.3)
	os.kill(int(pid),signal.SIGTERM)
	print "Sent. Run screen -r to check it."
os.system("screen -r jdk")
