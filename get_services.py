from swpag_client import Team
from pprint import pprint

t = Team("http://api.ictf2019.net/", "lVTU84h3IsWsv5Qa48Wv")
pprint(t.get_service_list())

with open('services.txt', 'w') as fout:
	pprint(t.get_service_list(), fout)
