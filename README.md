# tools
few scripts and useful commands

# scan
netdiscover -r 192.168.10.130/24
nmap -A -sS 192.168.10.135
nikto -h http://192.168.10.135/site
wapiti http://192.168.10.134/site
wordpress : wpscan --url http://192.168.10.135/site
