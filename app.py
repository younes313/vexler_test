from flask import Flask, render_template, jsonify, redirect, request, url_for
from werkzeug.utils import secure_filename
import os
import PIL
from PIL import Image

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = os.getcwd() + '/static/images' 
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


def allowed_image(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False



@app.route('/', methods=['GET', 'POST'])
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    
    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            if image.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                # image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                img = Image.open(image)
                img = img.resize((800, 800))
                q = img.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                print(q)
                return redirect(url_for('.puzzle', filename=filename))

            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("upload_image.html")


@app.route("/puzzle", methods=["GET", "POST"])
def puzzle():
    filename = request.args['filename']
    return render_template('index.html', filename=filename )




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)
