import requests
import json
import time
import matplotlib.pyplot as plt

os = {}
server = {}
protocols = {}
tls_version = {}

API_URL = "https://censys.io/api/v1/search/ipv4"
UID = "" #Get from Censys API
SECRET = "" #Get from Censys API


#Webserver, Protocols and Operating system - Run the program again for 152.7.0.0/16
PG = 1
while True:
    data = '{ "query": "ip: 152.1.0.0/16 ", "flatten": true, "fields": ["ip", "metadata.os","80.http.get.headers.server","443.https.get.headers.server", "protocols", "443.https.tls.version"], "page":'+str(PG)+'}'
    #time.sleep(5)
    res = requests.post(API_URL , headers = {"Content-Type": "application/json"}, auth=(UID, SECRET), data = data)

    if res.status_code == 200:
        for host_info in res.json()["results"]:
            if "metadata.os" in host_info:
                if host_info["metadata.os"] in os:
                    os[host_info["metadata.os"]] += 1
                else:
                    os[host_info["metadata.os"]] = 1
            if "80.http.get.headers.server" in host_info:
                if host_info["80.http.get.headers.server"] in server:
                    server[host_info["80.http.get.headers.server"]] += 1
                else:
                    server[host_info["80.http.get.headers.server"]] = 1
            if "443.https.get.headers.server" in host_info:
                if host_info["443.https.get.headers.server"] in server:
                    server[host_info["443.https.get.headers.server"]] += 1
                else:
                    server[host_info["443.https.get.headers.server"]] = 1
            if "protocols" in host_info:
                proc_list = host_info['protocols']
                for p in proc_list:
                    if p in protocols:
                        protocols[p] += 1
                    else:
                        protocols[p] = 1
            if "443.https.tls.version" in host_info:
                if host_info["443.https.tls.version"] in tls_version:
                    tls_version[host_info["443.https.tls.version"]] += 1
                else:
                    tls_version[host_info["443.https.tls.version"]] = 1
    else:
        break
    PG += 1

#Security Findings - Poodle Attack, Freak Attack, Logjam Attack

poodle_attacks = []
heartbleed_attacks = []
freak_atacks = []
logjam_attacks = []
PG = 1
while True:
    data = '{ "query": "ip: 152.1.0.0/16 ", "flatten": true, "fields": ["ip", "443.https.ssl_3","443.https.dhe_export", "443.https.rsa_export"], "page":'+str(PG)+'}'
    #time.sleep(5)
    res = requests.post(API_URL , headers = {"Content-Type": "application/json"}, auth=(UID, SECRET), data = data)
    if res.status_code == 200:
        for host_info in res.json()["results"]:
            if "443.https.ssl_3.support" in host_info:
                if host_info["443.https.ssl_3.support"]:
                    poodle_attacks.append(host_info["ip"])
            if "443.https.heartbleed.heartbleed_vulnerable" in host_info:
                if host_info["443.https.heartbleed.heartbleed_vulnerable"]:
                    heartbleed_attacks.append(host_info["ip"])
            if "443.https.dhe_export.support" in host_info:
                if host_info["443.https.dhe_export.support"]:
                    logjam_attacks.append(host_info["ip"])
            if "443.https.rsa_export.support" in host_info:
                if host_info["443.https.rsa_export.support"]:
                    freak_atacks.append(host_info["ip"])
    else:
        break
    PG += 1

"""
print(poodle_attacks)
print("\n\n")
print(heartbleed_attacks)
print("\n\n")
print(freak_atacks)
print("\n\n")
print(logjam_attacks)
"""
