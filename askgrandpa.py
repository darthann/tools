from PIL import Image


def loaddictionnary():
    image = Image.open('modele.png')
    pixls = image.load()
    x_space = 26
    y_space = 75
    dictionnary = []
    for x in range(80):
        temp = ''
        for y in range(12):
            if pixls[85 + x * x_space, y * y_space + 70] > (170, 170, 170):
                temp += 'x'
            else:
                temp += 'o'
        if temp != 'oooooooooooo':
            dictionnary.append(temp)
    dictionnary.append('oooooooooooo')

    return dictionnary


def readimage(dico, name):
    im = Image.open(name + '.jpg')
    pix = im.load()
    x_sp = 52
    y_sp = 152
    x_tab = []
    for x in range(80):
        temp = ''
        for y in range(12):
            if pix[155 + x * x_sp, 160 + y * y_sp] == (0, 0, 0):
                temp += 'x'
            else:
                temp += 'o'
        x_tab.append(temp)

    references = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#,$.-@%*<-/+_)Ç|&>:;¬\'?\"=!(,. '

    result = ''
    for char in x_tab:
        result += references[dico.index(char)]

    print(result)


file_names = ['programming', 'yolo', 'my', 'card', 'punch', 'grandpa']
dictionnaire = loaddictionnary()

for filename in file_names:
    readimage(dictionnaire, filename)
