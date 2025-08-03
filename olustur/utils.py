import qrcode
import qrcode.constants
from PIL import Image, ImageOps


def Qr(url:str, img_path=None):
    if img_path:
        qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white").convert('RGB')
        
        logo = Image.open(img_path).resize((150, 150))

        cerceve_size = 5
        logo = ImageOps.expand(logo, border= cerceve_size, fill= "white")

        pos = (
        (img.size[0] - logo.size[0]) // 2,
        (img.size[1] - logo.size[1]) // 2,
        )
        img.paste(logo, pos)
        return img
    else:
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        return qr.make_image(fill="black", back_color="white")
