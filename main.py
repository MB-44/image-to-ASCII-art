from PIL import Image 

img = Image.open("sample_image.png").convert('L')
img.save('sample_grayscale_image.png')