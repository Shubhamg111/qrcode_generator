# pip install pyqrcode 
# pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode

S="https://www.youtube.com"

# generate the qr code
url=pyqrcode.create(S)


# create and save svg file named myqr.svg
# url.svg("myqr.svg",scale=8)

# create and save png file named myqr.png
url.png('myqr2.png',scale=6)

