'''
This code creates a QR code for the URL "https://www.example.com" and saves it as a PNG image file called "example.png" in the same directory as the Python script. You can change the URL and the filename to suit your needs.
Note that you'll need to install the qrcode library before you can use it. You can do this using pip:
```
$ pip install qrcode
```

Once you have the library installed, you should be able to use the above code to generate QR codes in your Python scripts.

Reference:
  - https://www.freecodecamp.org/news/python-projects-for-beginners/#qr-code-encoder-decoder-python-project
'''

import qrcode

data = "https://www.example.com"
img = qrcode.make(data)
img.save("utility/qrcode/example.png")