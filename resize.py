# import the modules
import os
from os import listdir
from PIL import Image

def resize_by_percentage(image, outfile, percentage):
    with Image.open (image) as im:
        width, height = im.size
        resized_dimensions = (int(width * percentage), int(height * percentage))
        resized = im.resize(resized_dimensions)
        resized.save(outfile)

# get the path/directory
folder_dir = "F:/images/2023/2023_07_Slovinsko_Vyber"
for image in os.listdir(folder_dir):
    resize_by_percentage(f'{folder_dir}/{image}', f'{folder_dir}/30_{image}', 0.3)
    print(f'{folder_dir}/30_{image}')
