import time
import os
from concurrent.futures import ProcessPoolExecutor
from PIL import Image, ImageFilter

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]

def create_thumbnail(filename, size=(50,50),thumb_dir ='thumbs'):
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur())
    img.thumbnail(size)
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')
    print(f'Файл {filename} обработан...')


if __name__ == '__main__':
    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        executor.map(create_thumbnail, filenames)
   
    finish = time.perf_counter()

    print(f'Выполнение заняло {finish-start: .2f} секунд.')