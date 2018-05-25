import requests
import hashlib
import webbrowser

url = 'https://ringzer0team.com/challenges/13'
cookie = {'PHPSESSID': 'COOKIE HERE'}

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

hash = hash[:hash.__len__() - 7]
hash = hash[2:]
print(hash)

print("Traitement...\n")
hash = hash.encode("utf-8")
solution = hashlib.sha512(hash).hexdigest()
print(solution)
print("Sending solution...\n")


rp = s.post(url+"/"+str(solution), cookies=cookie)

open('page.html', 'wb').write(rp.content)

# webbrowser.open_new_tab(url+"/"+str(solution))
