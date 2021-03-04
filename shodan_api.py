from shodan import Shodan
import json

api = Shodan('5mgBBI2nLPHq07vTdEh5YGgio8mKTgNW')

# Lookup an IP
verified_cve = {}
hosts = ['152.1.109.5', '152.1.220.152', '152.1.52.127', '152.7.99.62']

for host in hosts:
    ipinfo = api.host(host)
    print(host)
    print(ipinfo['vulns'])
    for data in ipinfo['data']:
        if 'vulns' in data:
            for cve, ele in data['vulns'].items():
                if ele['verified']:
                    verified_cve[cve] = ele['summary']
    #printing only summary of the CVE whose verified flag is set to True
    print(verified_cve)
    print("\n")
