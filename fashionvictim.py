import os
from PIL import Image

# Split the gif
def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.save('%s/%s-%s.gif' % (outFolder, os.path.basename(inGif), nframes), 'GIF')
        nframes += 1
        try:
            frame.seek(nframes)
        except EOFError:
            break;
    return True

extractFrames('tv.gif', 'output')

# xor the images on pixels
# normally : for k in range (0, nframes)
for k in range (0, 31):
    im = Image.open('output/tv.gif-' + str(k) + '.gif')
    pix = im.load()

    # size : (492, 360)
    # white : 1
    # black : 0

    for i in range (0, 31):
        imT = Image.open('output/tv.gif-' + str(i) + '.gif')
        pixT = imT.load()
        for x in range (0, 492):
            for y in range (0, 360):
                if (pix[x, y] != pixT[x, y]):
                    pixT[x, y] = 1
                else:
                    pixT[x, y] = 0
        imT.save('output/int/image-' + str(k) + '-' + str(i) + '.gif')


