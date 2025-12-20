import os
import requests

url = 'https://www.google.com'
mid_url = url.split('://')[1]
dns = os.popen('nslookup ' + url).read().split('		')[1].split('\n')[0]
temp = mid_url.split('.')[1:]
sht_url = ''
for i in temp:
    sht_url += i + '.'
sht_url = sht_url[:-1]

#ct logs
print('-----------------SCANNING CT LOGS-----------------')
try:
    with requests.session() as res:
        res.get('https://crt.sh/json', params={'q': mid_url}, timeout=60)
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
    requests.delete

#quieries
print('-----------------RUNNING QUIERIES-----------------')
os.system('dig NS ' + url)
os.system('dig A ' + url)
os.system('dig MX ' + url)
os.system(f'dnsenum --dnsserver {dns} --enum {url}')
#zone transfer attempt
print('-----------------ZONE TRANSFER ATTEMPT-----------------')
os.system('curl https://api.hackertarget.com/zonetransfer/?q=' + sht_url)

#subdomain bruteforce
print('-----------------SUBDOMAIN BRUTEFORCE-----------------')
with open('resolvers.txt', 'w') as resolvers:
    resolvers.write(dns)
os.system('massdns -r ./resolvers.txt /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt')
#reverse dns
print('-----------------REVERSE DNS-----------------')


#txt records
print('-----------------TXT RECORDS-----------------')
os.system('dig TXT ' + url)