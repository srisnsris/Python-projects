import pyqrcode
import png

def qrcode(data):
    q = pyqrcode.create(data)
    q.png('QR Code.png', scale=6)
    print('QR Code genearted')
    
data = "https://www.google.com/"
qrcode(data)
