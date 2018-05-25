import requests
import webbrowser

url = 'https://ringzer0team.com/challenges/56'
cookie = {'PHPSESSID': 'COOKIE'}

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
    if "----- BEGIN HASH -----" in elem:
        analyze = 1

hash = hash[:hash.__len__() - 7]
hash = hash[2:]
print(hash)

# request to http://md5decrypt.net/Api/api.php
decrypterURL = "http://md5decrypt.net/Api/api.php"
ns = requests.Session()

email = 'test1432556477654@yopmail.com'
code = 'c9729d24e19f000d'
hash_type = 'sha1'

# "http://md5decrypt.net/Api/api.php?hash=" + hash + "&hash_type=" + hash_type + "&email=" + email + "&code=" + code

payload = {'hash': hash, 'hash_type': hash_type, 'email': email, 'code': code}
nr = ns.get(decrypterURL, params=payload)

print("Traitement...\n")
solution = nr.text
print(solution + "\n")
print("Sending solution...\n")


#rp = s.post(url+"/"+str(solution), cookies=cookie)
#open('hashmeplease.html', 'wb').write(rp.content)

webbrowser.open_new_tab(url+"/"+str(solution))
