from swpag_client import Team
t = Team("http://api.ictf2019.net/", "lVTU84h3IsWsv5Qa48Wv")
vm_info = t.get_vm()
print(vm_info.keys())
print(vm_info['ctf_key'])
print(vm_info['ip'])
print(vm_info['team_id'])
