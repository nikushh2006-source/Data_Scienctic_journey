import qrcode as qr
img = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=177s")
img.save("QR_Code.png")