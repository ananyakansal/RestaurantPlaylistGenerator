from flask import Flask, render_template, redirect, request
import spotifyAuthentication
import json

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(spotifyAuthentication.getAuth())

@app.route("/callback/")
def callback():
    userToken = spotifyAuthentication.getUserToken(request.args['code'])
    token = {'userToken': userToken[0]}
    return render_template('player.html', token=token)

    
if __name__ == "__main__":
    app.run(debug=True, port=5000)