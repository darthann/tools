import requests

url = 'http://challenge01.root-me.org/programmation/ch1/'
cookie = {'PHPSESSID': 'COOKIE'}

s = requests.Session()
r = s.get(url, cookies=cookie)

content = r.text.split('\n')

formula = content[0] # (a + Un) +/- (n * b)
u0 = content[1]
element = content[2]

formula = formula.split('U<sub>n+1</sub>')[1]

record = 0
j = 0
tab = []
tab.append("")
for i in range(0, formula.__len__()):
    if formula[i] == '[':
        record = 1
    if formula[i] == ']':
        record = 0
        j += 1
        tab.append("")
    if record == 1:
        tab[j] += formula[i]

a = tab[0].split('+')[0].split(' ')[1]
b = tab[1].split('*')[1].split(' ')[1]
operator = formula.split(' ')[7]

a = int(a)
b = int(b)

# (a + Un) +/- (n * b)
if operator == '-':
    def calcul(u, n):
        temp = (a + u) - (n * b)
        return temp
elif operator == '+':
    def calcul(u, n):
        temp = (a + u) + (n * b)
        return temp

u0 = int(u0.split(' ')[2])

element = int(element.split('<')[2].split('>')[1])

formula = "[" + str(a) + " + " + str(u0) + "] " + operator + " [n * " + str(b) + "]"
print(formula)
print("U0 = " + str(u0))

u = u0
for n in range (0, element):
    u = calcul(u, n) # Un+1

result = str(u)

rp = s.get(url+"/ep1_v.php?result="+ result, cookies=cookie)
open('result.html', 'wb').write(rp.content)