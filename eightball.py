from os import read
from flask import Flask, render_template, request, flash
from random import *
import os

readings = ["No", "Definitely not", "Yes!", "Nope!", "Ask another time.", "Yessir", "Kris is the homie"]

def reader():
    return choice(readings)
   
def rotate():
    degrees = randint(130, 230)
    text_offset = abs(degrees) - 180
    return [degrees, text_offset]

PHOTO_THING = os.path.join('static', 'uploadimg')

app = Flask(__name__)
app.secret_key = "ramen"

app.config['UPLOAD_FOLDER'] = PHOTO_THING

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        if request.form.get('submitbutton') == 'Shake The EightBall':
            #FadeIn_Animation = "animation-name: FadeIn;animation-duration: 2s;transition-timing-function: linear;@keyframes FadeIn 0% opacity: 0;100% opacity: 1;@-moz-keyframes FadeIn 0%; opacity: 0;100% {opacity: 1}}@-o-keyframes FadeIn {0% {opacity: 0}100% {opacity: 1}}@-webkit-keyframes FadeIn {0% {opacity: 0}100% {opacity: 1}}@-ms-keyframes FadeIn {0% {opacity: 0;}100% {opacity: 1;}}"
            list1 = rotate() 
            photo_retrieve = os.path.join(app.config['UPLOAD_FOLDER'], 'eightballtriangle.png')
            flash(reader())
            return render_template('index.html', render_triangle = photo_retrieve, render_degrees = list1[0], render_offset = list1[1])
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
