from swpag_client import Team
import subprocess
import sys
import datetime
from subprocess import CalledProcessError

def log(x):
    print '[' + str(datetime.datetime.now().time()) + ']: ' + x

def usage():
    print "TODO: Enter our own host IP in this script!"
    print "python submit_real_service.py <http://team_interface> <flag_token> <service_name>"
    print "The actual exploit script should take parameters like as follows: "
    print "python <service_name>.py <hostname> <port> <flag_id>"
    sys.exit(1)

if len(sys.argv) < 4:
    usage()

# Create connection
t = Team(sys.argv[1], sys.argv[2])

# Get service ID and ports
services = t.get_service_list()
service_id, service_port = 0, 0
for service in services:
    if service['service_name'] == sys.argv[3]:
        service_id = service['service_id']
        service_port = service['port']
        break

log("Service ID  : " + str(service_id))
log("Service Port: " + str(service_port))

# Sanity check the target ports
targets = t.get_targets(service_id)
for target in targets:
    assert(target['port'] == service_port)

# Send exploit to each target
flags, fails = [], []
for target in targets:

    # TODO: Make sure we don't exploit ourselves
    if target['team_name'] == 'gamma':
        continue

    command = 'timeout 5 python run_real_' + sys.argv[3] + '.py '
    command += '172.31.129.' + target['hostname'][-1] + ' ' + str(target['port']) + ' ' + str(target['flag_id'])
    try:
        flag = subprocess.check_output(command, shell=True)
    except CalledProcessError:
        log("Failed on: " + str(target['team_name']))
        continue
    log(target['hostname'] + ':' + str(target['port']) + ' - ' + flag)
    if 'FLG' in flag:
        flags.append(flag.strip())
    else:
        fails.append((target, flag.strip()))

# Submit flags
results = t.submit_flag(flags)
for result in results:
    log(result)
    # assert(result == 'correct')

if fails:
    for fail in fails:
        print "----------------------"
        print "Failed exploits"
        print "----------------------"
        print fail[0]
        print fail[1]
        print "----------------------"
