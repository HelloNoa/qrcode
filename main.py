import qrcode

# myQR = qrcode.make("https://hellonoa.dev")
# myQR.save("/Users/noa/PycharmProjects/qrcode/filename_temp01.png")

qrText = "https://hellonoa.dev"

qr = qrcode.QRCode(
    # version=4,
    version=1,
    # error_correction=qrcode.constants.ERROR_CORRECT_L,
    # error_correction=qrcode.constants.ERROR_CORRECT_M,
    # error_correction=qrcode.constants.ERROR_CORRECT_Q,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(qrText)
qr.make(fit=True)
import qrcode.image.svg

qrSVG = qrcode.QRCode(
    image_factory=qrcode.image.svg.SvgImage,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
)
qrSVG.add_data(qrText)
qrSVG.make(fit=True)

imgSVG = qrSVG.make_image(attrib={'fill': 'rgb(255, 248, 231)'})
# imgSVG = qrSVG.make_image(attrib={'stroke': 'red'})
imgSVG.save("firstH.svg")

img = qr.make_image(back_color="transparent", fill_color=(255, 248, 231))
# img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
img.save("filename_tempH.png")
