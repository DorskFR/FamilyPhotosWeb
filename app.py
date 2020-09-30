import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import FamilyScan

UPLOAD_FOLDER = 'static/uploads/'

application = app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/')
def upload_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['image']

    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filename, ext = sanitize_filename(filename)
        filename = filename + '.' + ext
        flash(f'Image {filename} successfully uploaded and displayed')
        return render_template('index.html', filename=filename)

    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

@app.route('/filter/<filename>/<filter>', methods=['POST'])
def apply_filter(filename, filter):

    if filename and allowed_file(filename):
        filename = secure_filename(filename)
        filename, ext = sanitize_filename(filename)
    else:
        flash('Cannot apply filter')
        return redirect(request.url)

    filename, maskname = FamilyScan.main(app.config['UPLOAD_FOLDER'], filename, ext, filter, crop=False)
    flash(f'Filter applied to image {filename} successfully')

    return render_template('index.html', filename=filename, maskname=maskname, filter=filter)

@app.route('/crop/<filename>/<filter>', methods=['POST'])
def crop_image(filename, filter):

    if filename and allowed_file(filename):
        filename = secure_filename(filename)
        filename, ext = sanitize_filename(filename)
    else:
        flash('Cannot apply filter')
        return redirect(request.url)

    filename, maskname = FamilyScan.main(app.config['UPLOAD_FOLDER'], filename, ext, filter, crop=True)
    flash(f'Image {filename} successfully cropped and displayed')

    return render_template('index.html', filename=filename)


def sanitize_filename(filename):
    #print(f"Received Filename is {filename}")
    filters = ['sobel', 'hsv', 'canny', 'crop']
    cleaned = False
    for filter in filters:
        filter = '-' + filter
        if len(filename.split(filter)) > 1:
            ext = filename.split(filter)[len(filename.split(filter))-1].split('.')[1]
            filename = filename.replace(ext, '')[:-1]
            filename = filename.replace(filter, '')
            cleaned = True
    if not cleaned:
        ext = filename.split('.')[len(filename.split('.'))-1]
        filename = filename.replace(ext, '')[:-1]
    #print(f"Returning Filename is {filename} and ext is {ext}")
    return filename, ext

if __name__ == "__main__":
    app.run()