from flask import Flask, request, redirect, render_template, session
from backend.predict import predict_image
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    results = None
    try:
        results = session['results']
    except:
        pass
    return render_template('home.html', results=results)
@app.route('/api/sendimage', methods=['POST'])
def send_image():
    request.files['pic_upload'].save('image.png')
    pred = predict_image()
    session['results'] = pred
    return redirect('/')
app.run(host='0.0.0.0')