import requests

s = requests.session()

url = "https://ringzer0team.com/challenges/126"
cookie = {'PHPSESSID' : 'COOKIE'}


sorted_wordlist = []
wordlist = open('words.txt', 'r').read().split()

for word in wordlist:
    sorted_wordlist.append(sorted(list(word)))

r = s.get(url, cookies=cookie)

contenu = r.text

contenu = contenu.split('\n')

hash = ""

analyze = 0;
for elem in contenu:
    if analyze == 1:
        hash = elem
        analyze = 0
        break
    if "----- BEGIN WORDS -----" in elem:
        analyze = 1

hash = str(hash[:hash.__len__() - 7])
hash = hash[2:]

references = hash.split(',')

print(references)


result = ""

for ref in references:
    if ref in wordlist:
        print('Perfect match with : ' + ref)
        result += ref + ','
    else:
        index = sorted_wordlist.index(sorted(list(ref)))
        match = wordlist[index]
        print('Scrambled with : ' + match)
        result += match + ','

result = result[:result.__len__() - 1]

print(result)

rp = s.post(url+"/"+str(result), cookies=cookie)

open('scramble.html', 'wb').write(rp.content)
