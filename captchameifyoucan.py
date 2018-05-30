# Get image
from BeautifulSoup import BeautifulSoup
import requests

url = 'http://challenge01.root-me.org/programmation/ch8/'
cookie = {'PHPSESSID': 'COOKIE'}

s = requests.Session()
r = s.get(url, cookies=cookie)

html_page = r.content

soup = BeautifulSoup(html_page)
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))

image_64_encode = ""

for elem in images:
    if 'base64' in elem:
        image_64_encode = elem

# Decode image (base64 to image)
import base64

image_64_encode = image_64_encode.split(',')
image_64_encode = image_64_encode[1]

data = base64.b64decode(image_64_encode)
filename = 'captcha.png'
with open(filename, 'wb') as f:
    f.write(data)

# Traitement du captcha
from PIL import Image
from pytesseract import image_to_string

im = Image.open('captcha.png')
pix = im.load()
size = im.size

for x in range(0, size[0]):
    for y in range(0, size[1]):
        if pix[x, y] == (0, 0, 0):
            pix[x, y] = (255, 255, 255)

for x in range(0, size[0]):
    for y in range(0, size[1]):
        if pix[x, y] != (255, 255, 255):
            pix[x, y] = (0, 0, 0)

im.save('output.png')


def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))

    def contrast(c):
        return 128 + factor * (c - 128)

    return img.point(contrast)


zoom_ratio = 1  # Zoom
contrast = 0  # Contraste

image = im
size = image.size

image = image.resize((int(size[0] * zoom_ratio), int(size[1] * zoom_ratio)))
# image.convert('L') # Gray scale

image = change_contrast(image, contrast)
image.save('output.png')

result = image_to_string(Image.open('output.png'))

print(result)

# Send answer
payload = {'cametu': result}
rp = s.post(url, cookies=cookie, data=payload)
open('result.html', 'wb').write(rp.content)
