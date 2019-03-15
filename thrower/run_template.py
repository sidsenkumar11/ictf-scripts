import sys
from pwn import *

def usage():
    print "python <service_name>.py <hostname> <port> <flag_id>"
    sys.exit(1)

usage()

r = remote(sys.argv[1], sys.argv[2])
# ....
