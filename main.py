from flask import Flask, request, render_template_string, Response
import io
from base64 import b64encode
from zipfile import ZipFile
from PIL import Image, ImageDraw, ImageFont #Import PIL functions

class myTemplate(): #Your template
    def __init__(self, discount, description, image):
        self.discount=discount #Saves Name input as a self object
        self.description=description #Saves Description input as a self object
        self.image=image #Saves Image input as a self object
    def draw(self):
        """
        Draw Function
        ------------------
        Draws the template
        """
        img = Image.open(r'./template.png', 'r').convert('RGB') #Opens Template Image
        if self.image != '':
            pasted = Image.open(self.image) #Opens Selected Image
            # pasted=pasted.resize((278, int(pasted.size[1]*(278/pasted.size[0])))) #Resize image to width fit black area's width
            # pasted=pasted.crop((0, 0, 278, 322)) #Crop height
            img.paste(pasted, (145, 617), pasted) #Pastes image into template
            imgdraw=ImageDraw.Draw(img) #Create a canvas
        fontBold=ImageFont.truetype("./AvenirNext-Bold.ttf", 242) #Loads font
        fontDemiBold=ImageFont.truetype("./AvenirNext-DemiBold.ttf", 242) #Loads font
        imgdraw.text((532.38,606.32), self.discount, (0,0,0), font=fontBold, spacing=-55) #Draws name
        imgdraw.text((654,231), self.description, (0,0,0)) #Draws description

        img.save(r'./out.png') #Saves output



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    return render_template_string("""
        <form method="POST" action="/download" enctype="multipart/form-data">
          <label for="name">Imagen:</label>
          <input type="file" name="image" accept="image/png, image/gif, image/jpeg" />
          <label for="name">Descuento:</label>
          <input type="number" name="discount" min="10" max="99"/>
          <label for="name">Description:</label>
          <input type="text" name="description"/>
          <input type="checkbox" id="upto" name="upto" checked>
          <label for="upto">Hasta?</label>
          <button type="submit">Submit</button>
        </form>
    """)

@app.route('/download', methods=['POST'])

def download():
    if request.files:
        image = request.files['image']
        amaztemp=myTemplate(request.form.get('discount'), request.form.get('description'), image)
        amaztemp.draw()

        zip_file_bytes_io = io.BytesIO()

        with ZipFile(zip_file_bytes_io, 'w') as zip_file:
            zip_file.write(r'./out.png', 'out.png')
            zip_file_bytes_io.seek(0)
        return Response(zip_file_bytes_io.getvalue(),
            mimetype='application/zip',
            headers={'Content-Disposition': 'attachment;filename=kit-campaña.zip'})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

