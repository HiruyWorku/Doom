import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'

sp_oauth = SpotifyOAuth(
    client_id='04d185d70436427fbcb531f9c372876a',
    client_secret='c5198baa697644fb8642a0b18876b2a4',
    redirect_uri='http://localhost:5000/callback',
    scope='user-library-read user-read-recently-played'
)

import pandas as pd

def get_recent_tracks(sp):
    # Fetch recently played tracks (limit is 50)
    results = sp.current_user_recently_played(limit=5)
    
    # List to store track info and features
    tracks_data = []
    
    # Iterate through each track in the response
    for item in results['items']:
        track = item['track']
        
        # Fetch audio features for the track using the track ID
        features = sp.audio_features(track['id'])[0]
        
        if features:
            # Append the track details and audio features
            tracks_data.append({
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'valence': features['valence'],            # Happiness/positivity
                'energy': features['energy'],              # Intensity/energy level
                'danceability': features['danceability'],  # Rhythmic ease of dancing
                'tempo': features['tempo'],                # Beats per minute (BPM)
                'speechiness': features['speechiness'],    # Spoken word percentage
                'acousticness': features['acousticness'],  # Acoustic sound quality
                'instrumentalness': features['instrumentalness']  # Instrumental percentage
            })
    
    # Convert the list of dictionaries to a pandas DataFrame
    return pd.DataFrame(tracks_data)

def categorize_mood(row):
    """
    Categorizes a track's mood based on its audio features.
    Mood categories can be adjusted as needed based on "vibe" features like valence, energy, etc.
    """
    
    valence = row['valence']
    energy = row['energy']
    danceability = row['danceability']
    acousticness = row['acousticness']
    instrumentalness = row['instrumentalness']
    
    # Example mood categorization logic:
    
    if valence > 0.7 and energy > 0.7:
        return 'Happy and Energetic'
    elif valence > 0.7 and energy < 0.4:
        return 'Chill and Uplifting'
    elif valence < 0.4 and energy > 0.7:
        return 'Angry or Intense'
    elif valence < 0.4 and energy < 0.4:
        return 'Sad or Melancholic'
    elif danceability > 0.6 and valence > 0.6:
        return 'Danceable and Upbeat'
    elif acousticness > 0.5 and instrumentalness > 0.5:
        return 'Ambient or Acoustic'
    else:
        return 'Neutral or Mixed Mood'

####THIS NNE



@app.route('/')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session['token_info'] = token_info
    return redirect(url_for('recent_tracks'))

@app.route('/recent_tracks')
def recent_tracks():
    token_info = session.get('token_info')
    sp = spotipy.Spotify(auth=token_info['access_token'])

    # Fetching recent tracks
    df = get_recent_tracks(sp)
    
    # Print the raw data for debugging
    print(df)

    # Categorize mood
    df['mood'] = df.apply(categorize_mood, axis=1)
    
    # Print categorized moods for debugging
    print(df[['name', 'artist', 'mood']])

    return df[['name', 'artist', 'mood']].to_html()

if __name__ == '__main__':
    app.run(debug=True)
