from flask import Flask, render_template, redirect, request, url_for
import spotifyAuthentication
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html', title="Home")

@app.route("/callback/")
def callback():
    return redirect(spotifyAuthentication.getAuth())

@app.route("/player/")
def player():
    userToken = spotifyAuthentication.getUserToken(request.args['code'])
    token = {'userToken': userToken[0]}
    return render_template('player.html', token=token)

    
if __name__ == "__main__":
    app.run(debug=True, port=5000)