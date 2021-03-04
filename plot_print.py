import matplotlib.pyplot as plt
import pandas as pd

#TLS version data obtained from censys_query_api.py 
tls1 = {'TLSv1.0': 83, 'TLSv1.2': 442}
tls7 = {'TLSv1.2': 160, 'TLSv1.0': 11}

#Operating system data obtained from censys_query_api.py
os1 = {'Windows': 142, 'Ubuntu': 69, 'Unix': 12, 'Raspbian': 3, 'Fedora': 4, 'CentOS': 8, 'Debian': 4, 'Win64': 1}
os7 = {'Windows': 60, 'CentOS': 51, 'Ubuntu': 8, 'RedHat': 1, 'Unix': 1}

#Server data obtained from censys_query_api.py
server1 = {'Microsoft-IIS/10.0': 119, 'Virata-EmWeb/R6_2_1': 152, 'Web-Server/3.0': 14, 'Apache': 230, 'HP_Compact_Server': 30, 'EPSON_Linux UPnP/1.0 Epson UPnP SDK/1.0': 4, 'Microsoft-IIS/8.5': 8, 'Apache/2.4.41 (Unix)': 3, 'Allegro-Software-RomPager/4.01': 5, 'nginx': 43, 'Jetty(9.4.31.v20200723)': 33, 'Boa/0.94.13': 2, 'Microsoft-WinCE/7.00': 4, 'Apache/2.4.7 (Ubuntu)': 9, 'Apache/2.4.6 (Red Hat Enterprise Linux)': 50, 'Apache/2.4.18 (Ubuntu)': 13, 'debut/1.20': 19,  'nginx/1.7.10': 4, 'Apache/2.4.29 (Ubuntu)': 15, 'Apache/2.2.15': 2, 'lighttpd': 16, 'Mbedthis-Appweb/2.4.0': 1, 'Apache/2.2.15 (Red Hat)': 13, 'EWS-NIC5/18.01': 1, 
'lighttpd/1.4.41': 8, 'Server': 3, 'HP-ChaiSOE/1.0': 37, 'Microsoft-WinCE/6.00': 1, 'Apache/2.2.22 (Fedora)': 2, 'httpd': 2,'Boa/0.94.14rc21': 15, 'debut/1.30': 13, 'Lexmark_Web_Server': 4, 'openresty/1.11.2.4': 1, 'http server 1.0': 1,  'Apache/2.4.6 (CentOS)': 5, 'lwIP/1.3.0': 2, 'RStudio': 2, 'Apache/2.2.15 (CentOS)': 5, 'Microsoft-IIS/7.5': 7, 'Apache/2.4.41 (Fedora)': 3, 'nginx/1.6.2': 1, 'gunicorn/19.3.0': 1, 'WEISIGER-NCE': 1, 'nginx/1.18.0': 6, 'lighttpd/1.4.35': 2, 'Apache/2.2.3 (Red Hat)': 1, 'GitHub.com': 2, 'lighttpd/1.4.32': 2,'$ProjectRevision: 4.0.2.38 $': 2, 'EWS-NIC5/90.99': 1, 'Virata-EmWeb/R6_0_1': 3,
'Apache/2.4.34 (Unix)': 1, 'EWS-NIC5/19.17': 1,'Apache/2.2.29.0 (Win64) PivotalWebServer/5.4.3': 1,'Microsoft-HTTPAPI/2.0': 12, 'Apache/2.2.22 (Ubuntu)': 1, 'SonicWALL SSL-VPN Web Server': 1, 'WindRiver-WebServer/4.7': 2, 'nginx/1.14.2': 4, 'PracFac-NCE-1': 1, 'Soundweb London': 1, 'Canon Http Server 1.00': 1, 'lighttpd/1.4.39': 2, 'Apache/2.4.41 (Ubuntu)': 4, 'Apache/2.4.29 (Unix) OpenSSL/1.0.2o': 2, 'Apache/2.2.29 (Unix) mod_wsgi/3.3': 2, 'GEIST Embedded Web Server (vCB_1072)': 1, 'debut/1.08': 2, 'Microsoft-IIS/8.0': 4, 'EWS-NIC5/99.00': 1, 'Apache-Coyote/1.1': 2, 'EWS-NIC5/19.09': 1, 'SET00108D03CC6E': 1, 'UPS_Server/1.0': 1, 'EWS-NIC5/17.95': 1, 'EIG Embedded Web Server': 1, 'ESERV-10/1.0': 1, 'EWS-NIC5/16.15': 2,
'Apache/2.2.26 (Unix)': 2, 'TornadoServer/6.0.3': 1, 'Mbedthis-Appweb/2.4.2': 2, 'alphapd/2.1.8': 2, 'Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips PHP/7.4.10': 2, 'nginx/1.14.0 (Ubuntu)': 2, 'EWS-NIC4/8.80': 1, 'CANON HTTP Server': 2, 'Microsoft-WinCE/5.0': 1, 'Crestron Webserver': 4, 'GoAhead-Webs': 1, 'MURPHY-NAE-2': 1, 'EWS-NIC4/8.43': 1, 'Embedded HTTP Server.': 2, 'Allegro-Software-RomPager/3.03': 1, 'lighttpd/1.4.37': 4, 'Apache/2.2.17 (Unix)': 1,'Allegro-Software-RomPager/4.62': 1, 'Apache/2.4.6 (Red Hat Enterprise Linux) PHP/7.3.11': 1,'Apache/2.4.37 (Red Hat Enterprise Linux)': 1, 'NetPort Software 1.1': 1, 'Apache/2.4.10 (Debian)': 1, 'Embedded Web Server ver 5.0': 1, 'MURPHY-NAE-1': 1, 
'HP HTTP Server': 22, 'PRAVIS/1.0': 1, 'Apache/2.2.24 (Unix)': 1, 'Microsoft-IIS/5.1': 1, 'Apache/2.4.33': 1, 'nginx/1.19.0': 2, 'Boa/0.94.14rc19': 1, 'Allegro-Software-RomPager/4.34': 2, 'MEDIACTR-NAE-2': 1}
server7 = {'Microsoft-IIS/10.0': 51, 'Apache': 60, 'EPSON_Linux UPnP/1.0 Epson UPnP SDK/1.0': 10, 'Microsoft-IIS/8.0': 4, 'Apache/2.2.15 (Red Hat)': 3, 'nginx/1.12.2': 5, 'nginx/1.15.8': 2, 'Apache/2.4.6 (CentOS)': 2, 'Apache/2.2.15 (CentOS)': 1, 'Microsoft-IIS/8.5': 6, 'Microsoft-WinCE/7.00': 1, 'nginx/1.18.0': 1, 'uhttpd/1.0.0': 3, 'nginx/1.7.10': 2, 'nginx/1.16.1': 1, 'lighttpd/1.4.18': 2, 'GoAhead-Webs': 1, 'lighttpd/1.4.32': 2, 'Apache/2.4.34 (Unix)': 1, 'Apache/2.4.29 (Ubuntu)': 1, 'Apache/2.4.18 (Ubuntu)': 1, 'Apache-Coyote/1.1': 4, 
'nginx/1.17.9': 1, 'EPSON-HTTP/1.0': 2, 'Microsoft-IIS/7.5': 3, 'nginx/1.15.9': 2, 'Virata-EmWeb/R6_2_1': 4, 'lighttpd/1.4.23': 1, 'Apache/2.4.41 (Ubuntu)': 1, 'Jetty(9.4.31.v20200723)': 2}

#Protocol data obtained from censys_query_api.py
proc1 = {'80/http': 651, '443/https': 544, '8080/http': 105, '22/ssh': 204, '25/smtp': 32, '21/ftp': 67, '3306/mysql': 29, '11211/memcached': 1, '53/dns': 13, '16992/http': 1, '47808/bacnet': 3, '5672/amqp': 1, '502/modbus': 1, '20000/dnp3': 1, '1521/oracle': 1, '5432/postgres': 3, '623/ipmi': 1, '995/pop3s': 1, '110/pop3': 1, '587/smtp': 1, '143/imap': 1, '3389/rdp': 1}
proc7 = {'443/https': 172, '80/http': 202, '22/ssh': 50, '5432/postgres': 14, '8080/http': 20, '3389/rdp': 2, '3306/mysql': 13, '21/ftp': 13, '993/imaps': 3, '465/smtp': 2, '995/pop3s': 2, '110/pop3': 2, '143/imap': 3, '53/dns': 8, '587/smtp': 3, '8888/http': 2, '502/modbus': 1, '25/smtp': 3, '47808/bacnet': 2, '1883/mqtt': 1}

#Plotting the Tables
df = pd.DataFrame(os1.items(), columns=["Operating System", "Host"])
print(df)
df = pd.DataFrame(os7.items(), columns=["Operating System", "Host"])
print(df)
df = pd.DataFrame(tls1.items(), columns=["TLS version", "Host"])
print(df)
df = pd.DataFrame(tls7.items(), columns=["TLS version", "Host"])
print(df)
df = pd.DataFrame(server1.items(), columns=["Webserver", "Host"])
print(df)
df = pd.DataFrame(server7.items(), columns=["Webserver", "Host"])
print(df)
df = pd.DataFrame(proc1.items(), columns=["Protocols", "Host"])
print(df)
df = pd.DataFrame(proc7.items(), columns=["Protocols", "Host"])
print(df)


#Plotting the Bar Graph
#Operating System
plt.figure('Operating System')           
plt.bar(os1.keys(), os1.values())
plt.xlabel('Operating System')
plt.ylabel('Hosts')
plt.show()
plt.figure('Operating System')            
plt.bar(os7.keys(), os7.values())
plt.xlabel('Operating System')
plt.ylabel('Hosts')
plt.show()

#Webserver
plt.figure('Webserver')           
plt.bar(server1.keys(), server1.values())
plt.xlabel('Webserver')
plt.xticks(fontsize= 5)
plt.xticks(rotation=270)
plt.ylabel('Hosts')
plt.show()
plt.figure('Webserver')            
plt.bar(server7.keys(), server7.values())
plt.xticks(fontsize= 5)
plt.xticks(rotation=270)
plt.xlabel('Webserver')
plt.ylabel('Hosts')
plt.show()

#Protocols
plt.figure('Protocols')           
plt.bar(proc1.keys(), proc1.values())
plt.xlabel('Protocols')
plt.xticks(fontsize= 5)
plt.xticks(rotation=270)
plt.ylabel('Hosts')
plt.show()
plt.figure('Protocols')            
plt.bar(proc7.keys(), proc7.values())
plt.xticks(fontsize= 5)
plt.xticks(rotation=270)
plt.xlabel('Protocols')
plt.ylabel('Hosts')
plt.show()

#TLS version
plt.figure('TLS version')             
plt.bar(tls1.keys(), tls1.values())
plt.xlabel('TLS version')
plt.ylabel('Hosts')
plt.show()
plt.figure('TLS version')             
plt.bar(tls7.keys(), tls7.values())
plt.xlabel('TLS version')
plt.ylabel('Hosts')
plt.show()
