import hashlib
import qrcode


def generate_code(product_name, product_size, product_number):
    return hashlib.md5((product_name + product_size + str(product_number)).encode('UTF-8')).hexdigest()


def generate_qr_code(hash_code):
    img = qrcode.make(hash_code)
    img = img.convert('RGB')
    img.save('test.pdf')
    return img
