from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os

# Initialize your Flask application instance
app = Flask(__name__)

# Configuration settings
UPLOAD_FOLDER = '/home/rymarinelli/Python/regression_app/uploads'
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # Optional: increase file size limit

# Ensure UPLOAD_FOLDER exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define your Flask routes
@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # Define filename here
        try:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'
        except Exception as e:
            print(f"Failed to save file: {e}")
            return "Failed to upload file due to an internal error."
    else:
        return redirect(request.url)

@app.route('/list-uploads')
def list_uploads():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    csv_files = [f for f in files if f.endswith('.csv')]
    return render_template('list_uploads.html', files=csv_files)


# Run the application if this file is executed as the main program
if __name__ == '__main__':
    app.run()

