import os
import requests

url = 'https://www.google.com'
dns = os.popen('nslookup ' + url).read().split('		')[1].split('\n')[0]
print(dns)

#ct logs
print('-----------------SCANNING CT LOGS-----------------')
try:
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
except:
    print('ct scan failed: skipping')
#quieries
print('-----------------RUNNING QUIERIES-----------------')
os.system('dig NS ' + url)
os.system('dig A ' + url)
os.system('dig MX ' + url)
os.system(f'dig AXFR @{dns} {url}')
os.system(f'dnsenum --dnsserver {dns} --enum {url}')
#zone transfer attempt
print('-----------------ZONE TRANSFER ATTEMPT-----------------')

#subdomain bruteforce
print('-----------------SUBDOMAIN BRUTEFORCE-----------------')


#reverse dns
print('-----------------REVERSE DNS-----------------')


#txt records
print('-----------------TXT RECORDS-----------------')
os.system('dig TXT ' + url)