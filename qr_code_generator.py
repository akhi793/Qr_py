import qrcode

img = qrcode.make("www.apple.com")
img.save=("apple.jpg")

img=qrcode.make("Apple Vison Pro is Revolutionary")
img.save("vis.jpg")

import cv2
d= cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("vis.jpg"))
print(val)