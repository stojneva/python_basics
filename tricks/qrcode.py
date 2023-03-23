import pyqrcode
import png
from pyqrcode import QRcode

address = 'https://softuni.bg/trainings/resources/video/78796/video-07-january-2023-%D0%BC%D0%B0%D1%80%D0%B8%D0%BE-%D0%B7%D0%B0%D1%85%D0%B0%D1%80%D0%B8%D0%B5%D0%B2-raw-version-programming-basics-with-python-january-2023/3992'
url = pyqrcode.create(address)
url.png('example.png', scale = 8)