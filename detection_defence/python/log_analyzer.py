from os import *

op = popen('find /var/log -name "boot.log.*"').readlines()


anomalies = {}
for file in op:
    anomalies[file] = []
    recentboot = popen(f"cat {file}").readlines()
    for i in recentboot:
        if "failed" in i.lower():
            anomalies[file].append(i)
anomalies["journalctl"] = popen('journalctl -p err --since "1 hour ago"').readlines()
for file in anomalies:
    if file == "journalctl":
        for i in anomalies["journalctl"]:
            print(i)
    print(file[:-1])
    for error in anomalies[file]:
        print("  " + error[:-1])