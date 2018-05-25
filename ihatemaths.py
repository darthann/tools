import requests
import hashlib
import webbrowser

url = 'https://ringzer0team.com/challenges/32'
cookie = {'PHPSESSID': 'moftbuo19s43monbqgejl55dn0'}

s = requests.Session()
r = s.get(url, cookies=cookie)


contenu = r.text

contenu = contenu.split('\n')

hash = ""

analyze = 0;
for elem in contenu:
    if analyze == 1:
        hash = elem
        print(hash)
        analyze = 0
    if "----- BEGIN MESSAGE -----" in elem:
        analyze = 1

hash = str(hash[:hash.__len__() - 11])
print(hash)

temp = hash.split('+')
deci = temp[0]
temp2 = temp[1].split('-')
hexa = int(temp2[0], 16)
bina = int(temp2[1], 2)

solution = int(deci) + hexa - bina
print("result is " + str(solution))

webbrowser.open_new_tab(url+"/"+str(solution))