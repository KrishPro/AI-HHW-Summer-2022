from tqdm import tqdm
import PIL.Image
import os

data_dir = "Assets"
images_name = os.listdir(data_dir)
images_path = [os.path.join(data_dir, name) for name in images_name]

for image_path in tqdm(images_path):

    image = PIL.Image.open(image_path)

    image = image.convert('RGB')

    image.save(image_path)

