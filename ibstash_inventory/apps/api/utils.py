import hashlib
import qrcode
from PIL import Image, ImageDraw


def generate_code(product_name, product_size, product_number):
    return hashlib.md5((product_name + product_size + str(product_number)).encode('UTF-8')).hexdigest()


def generate_qr_code(hash_code):
    background = Image.new("RGB", (472, 354), (255, 255, 255))
    img = qrcode.make(hash_code)
    img = img.convert('RGB')
    img = img.resize((280, 280))
    bg_w, bg_h = background.size
    img_w, img_h = img.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img, offset)
    draw = ImageDraw.Draw(background)
    draw.text((30, 10), hash_code, fill=(0, 0, 0))
    background.save(f'code_qr/{hash_code}.png')
    return img
