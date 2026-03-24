from os import *

op = popen('find /var/log -name "boot.log.*"').readlines()


anomalies = {}
for file in op:
    anomalies[file] = []
    recentboot = popen(f"cat {file}").readlines()
    for i in recentboot:
        if "failed" in i.lower():
            anomalies[file].append(i)
for file in anomalies:
    print(file[:-1])
    for error in anomalies[file]:
        print("  " + error[:-1])