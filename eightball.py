from os import read
from flask import Flask, render_template, request, flash, redirect, url_for
from random import *
import os

readings = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Very doubtful.", "Outlook not so good.", "My sources say no.", "My reply is no.", "Don't count on it."]

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
            Shake_Animation = "animation-name: Shake;animation-duration: 0.5s;transition-timing-function: linear;"
            FadeIn_Animation = "animation-name: FadeIn;animation-duration: 2s;transition-timing-function: linear;animation-fill-mode: forwards;animation-delay: 1.5s;"
            list1 = rotate() 
            photo_retrieve = os.path.join(app.config['UPLOAD_FOLDER'], 'eightballtriangle.png')
            flash(reader())
            return render_template('index.html', shake = Shake_Animation, render_triangle = photo_retrieve, animation = FadeIn_Animation, render_degrees = list1[0], render_offset = list1[1])
        elif request.form.get('eightball') == 'Eightball':
            return redirect(url_for('index'))
        elif request.form.get('about') == 'About':
            return redirect(url_for('about'))            
    elif request.method == 'GET':
        initial_property  = "opacity: 0;"
        photo_retrieve = os.path.join(app.config['UPLOAD_FOLDER'], 'eightballtriangle.png')
        return render_template('index.html', render_triangle = photo_retrieve, animation = initial_property)
@app.route("/about", methods=['POST', 'GET'])
def about():
    if request.method == 'POST':
        if request.form.get('eightball') == 'Eightball':
            return redirect(url_for('index'))
        elif request.form.get('about') == 'About':
            return redirect(url_for('about'))
    elif request.method == 'GET':
        return render_template('about.html')

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
