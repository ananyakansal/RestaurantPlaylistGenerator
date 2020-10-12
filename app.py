from flask import Flask, render_template, redirect, request
import spotifyAuthentication

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(spotifyAuthentication.getAuth())

@app.route("/callback/")
def callback():
    spotifyAuthentication.getUserToken(request.args['code'])
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)