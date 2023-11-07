import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,  # Set the border to 4 modules
)

qr.add_data("All hail python")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="black")
img.save("wsqr.png")
