from PIL import Image
import os

def resize_image(image_path, width, height, new_name):
    img = Image.open(image_path)
    resized_img = img.resize((width, height))
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    save_path = os.path.join(desktop_path, new_name + '.png')
    resized_img.save(save_path)
    return save_path


def rotate_image(image_path, angle, new_name):
    img = Image.open(image_path)
    rotated_img = img.rotate(angle)
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    save_path = os.path.join(desktop_path, new_name + '.png')
    rotated_img.save(save_path)
    return save_path
