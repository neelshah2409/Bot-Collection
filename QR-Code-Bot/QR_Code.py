import qrcode

location_in = input("Enter Location:")
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data("https://www.google.co.in/maps/place/" + location_in)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("1.png")
