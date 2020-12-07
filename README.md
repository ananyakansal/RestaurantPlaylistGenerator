# Group 3 Project Studio: Dynamic Playlist Generator

## What is it?
The dynamic playlist generator is a web application that creates a music playlist based on contextual data. The intended market for this application is the restaurant industry. With the app, restaurant owners will benefit from personalized, adaptive playlists that should enhance consumer satisfaction, while maintaining autonomy from the restaurant owner. 

## How does it work?
The app relies on user input, the Spotify Web API, and a library of songs with associated metadata.
Users define a list of parameters that map directly to categories within the available metadata such as genre, mood, timbre, instrumental vs vocal, tempo, and danceability. The library of songs used is found at https://multimediaeval.github.io/2018-AcousticBrainz-Genre-Task/, and the AcousticBrainz API (https://acousticbrainz.org) was used to extract the metadata from the library. 

A subset of the total library is created based on the user's preferences. The user has an option to allow the application access to their microphone. If access is granted, songs are queued to the player based on the average sound pressure level. The sound pressure level is mapped to the tempo of the songs in the library subset. When the sound pressure level increases, faster songs are queued, and when the sound pressure level decreases, slower songs are queued. If microphone access is denied, songs are chosen randomly from the library subset. 

The user can change their preferences at any time to generate a new playlist.

The songs are played via the Spotify Web API and Spotify Player SDK. At the app's launch, the user is prompted to login to their Spotify account. As each song is played, a new song is added to the queue by the methods described above.

- link to paper
- embed video

## How to run it

### Package Requirements/Dependencies
The application utilizes the following packages:
- Python3 (https://www.python.org/downloads/)
  - Native packages
    - Json
    - threading
    - time
    - math
    - random
  - External packages
    - requests (https://pypi.org/project/requests/)
    - pandas (https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
    - numpy (https://numpy.org/install/)
    - sklearn (https://scikit-learn.org/stable/install.html)
- Flask (https://flask.palletsprojects.com/en/1.1.x/installation/)
- Pyaudio (https://people.csail.mit.edu/hubert/pyaudio/)

### Running the app
The application should be run via terminal/console and launched in Google Chrome. 

Clone the repository and move it to your desired folder. Navigate to the folder where you downloaded the repository. Set up the application by filling in CLIENT_SECRET field in spotifyAuthentication.py and spotifyPlayback.py. Unzip the file called songDataCSVs.zip

To run the application, run the following python command: $ python3 app.py 
This will prompt a response in terminal that looks like:
[insert screenshot]

The application currently serves at http://127.0.0.1:5000/. After running the python command, open the url in Google Chrome. You should see the application homescreen.

### Using the app
On the home screen, click the login with Spotify button. This will take you to the Spotify login page. Fill out the Spotify login fields and hit login. You will then be routed back to the application player page. 
(If you have saved your Spotify login information in Chrome,  you may be directly routed to the player page)

Complete the form with your preferences, and hit the submit button. 
If your selection was valid, you will see the message "Thank  you!  Your submission has been received". Wait for your selection to be processed. The player is ready when song titles are listed under the Queue header.
If your  selection was invalid, you will see the message "Your current selection is unavailable. Please make a new selection." 

To play through the queue, click the album artwork. The next song will be played automatically at the conclusion of the previous song. To pause the queue, hit the album artwork again. 

If you enabled microphone use, you can check the current sound pressure level with the "Room Noise" field (found above the album artwork). 

To make a new selection, pause the current playback and resubmit the form.

### Closing the app
To close the app, close the browser window and terminate the program in Terminal/Console with ^C

### Troubleshooting


