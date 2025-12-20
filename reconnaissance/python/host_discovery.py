import os

if os.popen("nmap --version").read()[:4] != "Nmap":
    print(os.system("sudo apt install nmap"))

op = os.popen('ip a | grep "inet "').readlines()
for i in op:
    if "scope host" in i:
        op.remove(i)
for i in op:
    print(f'scanning: {i[i.index("inet"):]}')
    ip = i[i.index('inet')+5:i.index('brd')]
    os.system(f'nmap -sn {ip}')
