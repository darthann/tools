from PIL import Image
from pyzbar.pyzbar import decode

im = Image.open('qr3.png')
pix = im.load()
size = im.size


def carre_noir(refx, refy):
    for x in range(refx, refx + 72 + 1):
        for y in range(refy, refy + 72 + 1):
            pix[x, y] = (0, 0, 0)


def bande_blanche_verticale_cote_gauche(startx, starty, endy):
    for x in range(startx, startx + 10):
        for y in range(starty, endy + 1):
            pix[x, y] = (255, 255, 255)


def bande_blanche_horizontale_cote_gauche(starty, startx, endx):
    for y in range(starty, starty + 10):
        for x in range(startx, endx + 1):
            pix[x, y] = (255, 255, 255)


def schema_cote_gauche_haut(refx, refy):
    bande_blanche_horizontale_cote_gauche(refx + 9, refx + 9 * 2, refy - 9 * 2)
    bande_blanche_horizontale_cote_gauche(refy - 9 * 3, refx + 9 * 2, refy - 9 * 2)
    bande_blanche_horizontale_cote_gauche(refy - 9, refx, refy - 9)
    bande_blanche_verticale_cote_gauche(refy - 9, refx, refy)
    bande_blanche_verticale_cote_gauche(refx + 9, refx + 9, refy - 9 * 2) # Petite
    bande_blanche_verticale_cote_gauche(refy - 9 * 3, refx + 9, refy - 9 * 2) # Petite


def bande_blanche_verticale_cote_droit(startx, starty, endy):
    for x in range(startx, startx + 10):
        for y in range(starty, endy + 1):
            pix[x, y] = (255, 255, 255)


def bande_blanche_horizontale_cote_droit(startx, starty, endx):
    for y in range(starty, starty + 10):
        for x in range(startx, endx + 1):
            pix[x, y] = (255, 255, 255)


def schema_cote_droit():
    bande_blanche_verticale_cote_droit(245 + 18, 18 + 9, 90 - 18)
    bande_blanche_verticale_cote_droit(18 + 9 + 245 - 72 + 27, 18 + 9, 90 - 18)
    bande_blanche_verticale_cote_droit(18 + 9 + 245 - 72 + 9, 18, 90 - 9)
    bande_blanche_horizontale_cote_droit(245 - 36, 72 + 9, 281)
    bande_blanche_horizontale_cote_droit(227, 27, 281 - 9)
    bande_blanche_horizontale_cote_droit(227, 63, 281 - 9)


def schema_cote_gauche_bas():
    bande_blanche_horizontale_cote_gauche(209, 18, 90)
    bande_blanche_horizontale_cote_gauche(209 + 18, 18 + 9, 90 - 18)
    bande_blanche_horizontale_cote_gauche(281 - 18, 18 + 9, 90 - 18)
    bande_blanche_verticale_cote_gauche(81, 209, 281)
    bande_blanche_verticale_cote_gauche(81 - 18, 209 + 18, 281 - 9)
    bande_blanche_verticale_cote_gauche(18 + 9, 209 + 18, 281 - 9)


# Haut gauche
carre_noir(18, 18)
schema_cote_gauche_haut(18, 90)

# Haut droite
carre_noir(209, 18)
schema_cote_droit()

# Bas gauche
carre_noir(18, 209)
schema_cote_gauche_bas()

print(decode(im))

im.save('output.png')
