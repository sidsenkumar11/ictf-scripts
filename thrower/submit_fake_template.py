from swpag_client import Team
import subprocess
import sys
import datetime

def log(x):
    print '[' + str(datetime.datetime.now().time()) + ']: ' + x

def usage():
    print "TODO: Enter our own host IP in this script!"
    print "python exploit_and_submit_service.py <http://team_interface> <flag_token> <service_name>"
    print "The actual exploit script should take parameters like as follows: "
    print "python <service_name>.py <hostname> <port> <flag_id>"
    sys.exit(1)

usage()
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

    command = 'python run_fake_' + service_name + '.py '
    command += '172.31.129.' + target['hostname'][-1] + ' ' + target['port'] + ' ' + target['flag_id']
    flag = subprocess.check_output(command, shell=True)
    log(target['host'] + ':' + target['port'] + ' - ' + flag)
    if 'FLG' in flag:
        flags.append(flag.strip())
    else:
        fails.append((target, flag.strip()))
