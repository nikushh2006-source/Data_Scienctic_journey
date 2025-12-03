import qrcode as qr
from PIL import Image as img
qr = qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=5)
qr.add_data("https://www.linkedin.com/in/nikita-sharma-166626323/")
qr.make(fit=True)
img =qr.make_image(fill_color ='red',back_color ='yellow')
img.save("Linkdin_Profile_Nikita.png")