import qrcode
from PIL import Image

qr= qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=3)
qr.add_data("hello thi is a update qr code")
qr.make(True)
Img=qr.make_image(fill_color="red",back_color="blue")
Img.save("advence qr code.png")