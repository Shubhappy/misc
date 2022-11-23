# from PIL import Image
# import io
 
 
# photo = 'Mxpertz logo.jpg'
 
# #open the image
# img = Image.open(photo, mode='r')
 
# # resize the image
# img = img.resize((70,47))
     
# byteIO = io.BytesIO()
# img.save(byteIO, format='png')
# byteArr = byteIO.getvalue()
# img.show()

import io
import base64
from PIL import Image

base64_str = 'iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=='

buffer = io.BytesIO()
imgdata = base64.b64decode(base64_str)
img = Image.open(io.BytesIO(imgdata))
new_img = img.resize((2, 2))  # x, y
new_img.save(buffer, format="PNG")
img_b64 = base64.b64encode(buffer.getvalue())
print(str(img_b64)[2:-1])
