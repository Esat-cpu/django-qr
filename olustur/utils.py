import qrcode

def Qr(url):
    qr = qrcode.QRCode(version= 1, box_size=10, border= 4)
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill= "black", back_color= "white")
