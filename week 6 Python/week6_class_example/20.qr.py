
#this code is to make a qrcode

import os
import qrcode as np

img = np.make("hey world") #makes the qr code and put it into a object for PIL

img.save("qr.png", "PNG") #saves it as png to dir



