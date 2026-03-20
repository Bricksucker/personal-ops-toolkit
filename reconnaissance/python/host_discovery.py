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
    scaninit = os.popen(f'nmap -sn {ip}')
    for line in scaninit.readlines():
        if "Nmap scan" in line:
            ipt = line.split(" ")[-1][:-1]
            print("scanning " + ipt)
            scan80 = os.popen("nmap -p 80,443 " + ipt).read()
            if "80/tcp  closed" in scan80 and "443/tcp closed" in scan80:
                print(ipt + " not a host")
            else:
                print(f"\n------------------------------------------------IP {ipt} IS A HOST------------------------------------------------\n")
                print(scan80)
