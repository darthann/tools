import requests

url = 'https://ringzer0team.com/challenges/119'
cookie = {'PHPSESSID': 'COOKIE'}

s = requests.Session()
r = s.get(url, cookies=cookie)

open('beforeascii.html', 'wb').write(r.content)

contenu = r.text

contenu = contenu.split('\n')

hash = ""

analyze = 0;
for elem in contenu:
    if analyze == 1:
        hash = elem
        analyze = 0
    if "----- BEGIN MESSAGE -----" in elem:
        analyze = 1

hash = hash[:hash.__len__() - 7]
hash = hash[2:]

data = hash
print(data)

compteur = 0
for i in range(0, data.__len__()):
    if data[i] == '>':
        compteur += 1

print("compteur = " + str(compteur))
content = ""
i = 0
tab = []

for k in range(0, compteur):
    while data[i] != '>':
        content += data[i]
        i += 1
    i += 1
    tab.append(content)
    content = ""

result = ""

for i in range(0, tab.__len__()):
    checked = 0
    # if pattern, i + 5
    # zero : <br />&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;<br />
    if "&nbsp;xxx&nbsp;" in tab[i] and  "x&nbsp;&nbsp;&nbsp;x" in tab[i + 1] and "x&nbsp;&nbsp;&nbsp;x" in tab[i + 2] and "x&nbsp;&nbsp;&nbsp;x" in tab[i + 3] and "&nbsp;xxx&nbsp;" in tab[i + 4] and checked == 0:
        result += '0'
        i += 5
        checked = 1
    # un : &nbsp;xx&nbsp;&nbsp;<br />x&nbsp;x&nbsp;&nbsp;<br />&nbsp;&nbsp;x&nbsp;&nbsp;<br />&nbsp;&nbsp;x&nbsp;&nbsp;<br />xxxxx<br />
    if "&nbsp;xx&nbsp;&nbsp;" in tab[i] and  "x&nbsp;x&nbsp;&nbsp;" in tab[i + 1] and "&nbsp;&nbsp;x&nbsp;&nbsp;" in tab[i + 2] and "&nbsp;&nbsp;x&nbsp;&nbsp;" in tab[i + 3] and "xxxxx" in tab[i + 4] and checked == 0:
        result += '1'
        i += 5
        checked = 1
    # deux : &nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x&nbsp;<br />&nbsp;&nbsp;xx&nbsp;<br />&nbsp;x&nbsp;&nbsp;&nbsp;<br />xxxxx<br />
    if "&nbsp;xxx&nbsp;" in tab[i] and  "x&nbsp;&nbsp;&nbsp;x&nbsp;" in tab[i + 1] and "&nbsp;&nbsp;xx&nbsp;" in tab[i + 2] and "&nbsp;x&nbsp;&nbsp;&nbsp;" in tab[i + 3] and "xxxxx" in tab[i + 4] and checked == 0:
        result += '2'
        i += 5
        checked = 1
    # quatre : <br />&nbsp;x&nbsp;&nbsp;&nbsp;x<br />x&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />
    if "&nbsp;x&nbsp;&nbsp;&nbsp;x" in tab[i] and  "x&nbsp;&nbsp;&nbsp;&nbsp;x" in tab[i + 1] and "&nbsp;xxxxx" in tab[i + 2] and "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x" in tab[i + 3] and "&nbsp;&nbsp;&nbsp;&nbsp;x" in tab[i + 4] and checked == 0:
        result += '9'
        i += 5
        checked = 1
    # cinq : <br />xxxxx<br />x&nbsp;&nbsp;&nbsp;&nbsp;<br />&nbsp;xxxx<br />&nbsp;&nbsp;&nbsp;&nbsp;x<br />xxxxx<br />
    if "xxxxx" in tab[i] and  "x&nbsp;&nbsp;&nbsp;&nbsp;" in tab[i + 1] and "&nbsp;xxxx" in tab[i + 2] and "&nbsp;&nbsp;&nbsp;&nbsp;x" in tab[i + 3] and "xxxxx" in tab[i + 4] and checked == 0:
        result += '5'
        i += 5
        checked = 1
    # huit : <br />&nbsp;xxx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;&nbsp;xx&nbsp;<br />x&nbsp;&nbsp;&nbsp;x<br />&nbsp;xxx&nbsp;<br />
    if "&nbsp;xxx&nbsp;" in tab[i] and  "x&nbsp;&nbsp;&nbsp;x" in tab[i + 1] and "&nbsp;&nbsp;xx&nbsp;" in tab[i + 2] and "x&nbsp;&nbsp;&nbsp;x" in tab[i + 3] and "&nbsp;xxx&nbsp;" in tab[i + 4] and checked == 0:
        result += '8'
        i += 5
        checked = 1

print(result)

# open('ascii.html', 'wb').write(r.content)

rp = s.post(url+"/"+ result, cookies=cookie)
open('afterascii.html', 'wb').write(rp.content)