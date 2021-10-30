from os import read
from flask import Flask, render_template, request, flash
from random import *
import os

readings = ["No", "Definitely not", "Yes!", "Nope!", "Ask another time.", "Yessir", "Kris is the homie"]

def reader():
    return choice(readings)
   
def rotate():
    degrees = randint(-180, -90)
    text_offset = 135 - abs(degrees)
    return [degrees, text_offset]


PHOTO_THING = os.path.join('static', 'uploadimg')

app = Flask(__name__)
app.secret_key = "ramen"

app.config['UPLOAD_FOLDER'] = PHOTO_THING

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        if request.form.get('submitbutton') == 'Shake The EightBall':
            list1 = rotate() 
            photo_retrieve = os.path.join(app.config['UPLOAD_FOLDER'], 'triangle.png')
            flash(reader())
            return render_template('index.html', render_triangle = photo_retrieve, render_degrees = list1[0], render_offset = list1[1])
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
