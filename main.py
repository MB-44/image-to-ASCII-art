from PIL import Image 
from argparse import ArgumentParser, Namespace
import sys, random, math
import numpy as np 

# img = Image.open("sample_image.png").convert('L')
# img.save('sample_grayscale_image.png')

greyScale01 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
greyScale02 = '@%#*+=-:. '

def averageToGet(image):

    im = np.array(image)
    width, height = im.shape

    return np.average(im.reshape(width * height))

def convert(fileName, cols, scale, moreLevels):
    
    global greyScale01, greyScale02

    image = Image.open(fileName).convert('L')

    WIDTH, HEIGHT = image.size[0], image.size[1]
    print("Input Image dimensions are %d x %d" % (WIDTH, HEIGHT))

    width = WIDTH / cols
    height = HEIGHT / cols

    rows = int(HEIGHT / height)

    print("cols: %d, rows: %d " % (cols,rows))
    print("tile dims: %d x %d" % (width, height))

    # if image size is too small - exit it
    if cols > WIDTH or rows > HEIGHT:
        print("Image too small for specified cols!")
        exit(0)
    
    # ascii is the list of character strings
    # let's generate a list of dimensions
    aImage = []

    for index01 in range(rows):
        y1 = int(index01 * height)
        y2 = int((index01 + 1) * height)

        if index01 == (rows - 1):
            y2 = HEIGHT
        
        aImage.append("")

        for index02 in range(cols):
            x1 = int(index02 * width)
            x2 = int((index02 + 1) * width)

            if index02 == (cols - 1):
                x2 = WIDTH

            img = image.crop((x1, y1, x2, y2))

            avg = int(averageToGet(img))

            if moreLevels:
                greyScalValue = greyScale01[int((avg*69)/255)]
            else: 
                greyScalValue = greyScale02[int((avg*9)/255)]

            aImage[index01] += greyScalValue
    return aImage


def main():
    parser = ArgumentParser(description="Program to converts Image into ASCII art")

    parser.add_argument("--file",dest='imageFile', required=True)
    parser.add_argument('--scale',dest='scale',required=True)
    parser.add_argument('--out',dest='outFile', required=True)
    parser.add_argument('--cols',dest='cols', required=True)
    parser.add_argument('--morelevels', dest='morelevels',action='store_true')

    args: Namespace = parser.parse_args()

    imageFile = args.imageFile

    outFile = 'outfile.txt'
    if args.outFile:
        outFile = args.outFile

    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    
    cols = 80
    if args.cols:
        cols = int(args.cols)
    
    print("Generating.....")

    aImage = convert(imageFile,cols,scale, args.moreLevels)

    with open(outFile,"w") as file:
        for row in aImage:
            file.write(row + "\n")
    
    print("ASCII art written to %s" % outFile)



if __name__ == "__main__":
    main()