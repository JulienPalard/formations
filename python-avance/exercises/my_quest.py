import sys
import pexpect

child = pexpect.spawn("netcat mdk.fr 1975")
child.logfile = sys.stdout.buffer
child.expect("What is your quest?")
child.sendline("To seek the Holy Grail.")
child.expect("What is your name?")
child.sendline("My name is Sir Lancelot of Camelot.")
child.expect("What is your favorite color?")
child.sendline("Blue")
child.expect("Find the exit.")
