import base64
import requests

url = 'https://ringzer0team.com/challenges/16'
cookie = {'PHPSESSID': 'COOKIE'}

s = requests.Session()
r = s.get(url, cookies=cookie)

contenu = r.text
contenu = contenu.split('\n')

key = ""
message= ""
keyflag = 0;
msgflag = 0;
for elem in contenu:
    if keyflag == 1:
        key = elem
        keyflag = 0
    if msgflag == 1:
        message = elem
        msgflag = 0
        break
    if "----- BEGIN XOR KEY -----" in elem:
        keyflag = 1
    if "----- BEGIN CRYPTED MESSAGE -----" in elem:
        msgflag = 1

key = key[:key.__len__() - 7]
key = key[2:]

message = message[:message.__len__() - 7]
message = message[2:]

print('key : ' + key)
print('message : ' + message)

# xor between byte and string
def sxor(s1,s2):
    return ''.join(chr(a ^ ord(b)) for a,b in zip(s1,s2))

# Decode message
message = base64.b64decode(message)

size = message.__len__()
n = size%10 + int(size/10) - 1 # Parcourir le message en n étapes

keylength = 10
result = ""
for i in range(0, key.__len__() - keylength):
    temp_key = key[i:i+keylength]
    solution = ""
    for i in range(0, n):
        solution += sxor(message[i * 10:], temp_key)
    if solution.isalnum():
        result = solution
        break

print('result : ' + result)

rp = s.post(url + '/' + result, cookies=cookie)
open('xorme.html', 'wb').write(rp.content)
