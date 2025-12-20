import os
import requests

url = 'https://www.google.com'
dns = os.popen('nslookup ' + url).read().split('		')[1].split('\n')[0]
print(dns)

#ct logs
print('-----------------SCANNING CT LOGS-----------------')
res = requests.get('https://crt.sh/json', params={'q': url.split('://')[1]}, timeout=60)
res.raise_for_status()
data = res.json()
domains = set()
for entry in data:
    name_value = entry.get('name_value', '')
    for name in name_value.split('\n'):
        domains.add(name.strip())
for i in sorted(domains):
    print(i)
#quieries
print('-----------------RUNNING QUIERIES-----------------')
os.system('dig ' + url)
os.system('host ' + url)

#zone transfer attempt
print('-----------------ZONE TRANSFER ATTEMPT-----------------')

#subdomain bruteforce
print('-----------------SUBDOMAIN BRUTEFORCE-----------------')


#reverse dns
print('-----------------REVERSE DNS-----------------')


#txt records
print('-----------------TXT RECORDS-----------------')