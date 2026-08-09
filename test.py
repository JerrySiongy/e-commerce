from rembg import remove
from PIL import Image

input_path = "static/logo.jpeg"
output_path ="static/logo2.png"

with open(input_path, 'rb') as inp:
    input_data = inp.read()

output_data = remove(input_data)

with open(output_path, 'wb') as out:
    out.write(output_data)



