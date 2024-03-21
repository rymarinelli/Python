from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
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
        # Here, you can add the logic to handle the CSV file
        # For example, saving it to a directory or processing its contents
        return 'File uploaded successfully'
    else:
        return redirect(request.url)
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['csv']
if __name__ == '__main__':
    app.run(port=5001)
