import requests
import hashlib

url = 'https://ringzer0team.com/challenges/57'
cookie = {'PHPSESSID': 'COOKIE'}

s = requests.Session()
r = s.get(url, cookies=cookie)

contenu = r.text

contenu = contenu.split('\n')

hash = ""
salt= ""
hashflag = 0;
saltflag = 0;
for elem in contenu:
    if hashflag == 1:
        hash = elem
        hashflag = 0
    if saltflag == 1:
        salt = elem
        saltflag = 0
        break
    if "----- BEGIN HASH -----" in elem:
        hashflag = 1
    if "----- BEGIN SALT -----" in elem:
        saltflag = 1

hash = hash[:hash.__len__() - 7]
hash = hash[2:]
print(hash)

salt = salt[:salt.__len__() - 7]
salt = salt[2:]
print(salt)

result = ""

for i in range(0, 10001):
    temp = hashlib.sha1(str(i).encode('utf-8') + salt.encode('utf-8')).hexdigest()
    if temp == hash:
        print('Match !')
        result = str(i)
        break

print('Answer is : ' + result)

rp = s.post(url + '/' + result, cookies=cookie)

open('hashbreakreloaded.html', 'wb').write(rp.content)

