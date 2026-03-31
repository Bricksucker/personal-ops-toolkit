from os import *

# Collect values first (cleaner + safer)
hostname = popen("hostname")
user = popen("whoami")
uptime = popen("uptime -p")
os = popen(f"grep PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d " + '"' + '/' + '"')
kernel = popen("uname -r")
cpu = popen("lscpu | grep 'Model name' | cut -d: -f2 | xargs")
memory = popen("free -h | awk '/Mem:/ {print $3 " + '"' + '/' + '"' " $2}'")
disk = popen("df -h / | awk 'NR==2 {print $3 " + '"' + '/' + '"' " $2}")
ip = popen("hostname -I | xargs")
external_ip = popen("curl -s ifconfig.me")

print(popen("ping -c 1 8.8.8.8").read())

"""
if ping -c 1 8.8.8.8 > /dev/null 2>&1; then
    internet_val=true
else
    internet_val=false
fi

# Output JSON
printf "{\n"
printf '  "hostname": "%s",\n' "$hostname_val"
printf '  "user": "%s",\n' "$user_val"
printf '  "uptime": "%s",\n' "$uptime_val"
printf '  "os": "%s",\n' "$os_val"
printf '  "kernel": "%s",\n' "$kernel_val"
printf '  "cpu": "%s",\n' "$cpu_val"
printf '  "memory": "%s",\n' "$memory_val"
printf '  "disk": "%s",\n' "$disk_val"
printf '  "ip": "%s",\n' "$ip_val"
printf '  "external_ip": "%s",\n' "$external_ip_val"
printf '  "internet": %s\n' "$internet_val"
printf "}\n"

while true; do
  ./sysinfo.sh > /sysinfo.json
  sleep 3
done
"""